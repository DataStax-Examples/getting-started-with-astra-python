from dao.data_type_util import format_timestamp, uuid_from_string
from cql_file_util import get_cql_schema_string_from_file
from cassandra.query import BoundStatement, BatchStatement, BatchType


class LocationUDT(object):

    def __init__(self, x_coordinate, y_coordinate, z_coordinate):
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.z_coordinate = z_coordinate


class SpacecraftLocationDAO(object):

    table_name = "spacecraft_location_over_time"

    type_name = "location_udt"

    create_stmt = get_cql_schema_string_from_file(table_name)

    create_location_type_stmt = get_cql_schema_string_from_file(type_name)

    insert_stmt = 'INSERT INTO {table_name} (spacecraft_name, journey_id, location, location_unit, reading_time) ' \
                  'VALUES (:spacecraft_name,:journey_id,:location,:location_unit,:reading_time);'.format(table_name=table_name)

    select_stmt = 'SELECT * FROM {table_name} WHERE spacecraft_name = :spacecraft_name AND journey_id = :journey_id;' \
                  ''.format(table_name=table_name)

    def __init__(self, _session):
        self._session = _session
        self.maybe_create_location_type()
        self.maybe_create_schema()
        self.insert_prep_stmt = _session.prepare(self.insert_stmt)
        self.select_prep_stmt = _session.prepare(self.select_stmt)
        self.page_state = None

    def maybe_create_schema(self):
        self._session.execute(self.create_stmt)

    def maybe_create_location_type(self):
        self._session.execute(self.create_location_type_stmt)

    def write_readings(self, spacecraft_name, journey_id, data):
        batch = BatchStatement()
        batch.batch_type = BatchType.UNLOGGED

        for row in data:
            batch.add(self.insert_prep_stmt.bind({
                'spacecraft_name': spacecraft_name,
                'journey_id': uuid_from_string(journey_id),
                'location': LocationUDT(row['location']['x_coordinate'],
                                        row['location']['y_coordinate'],
                                        row['location']['y_coordinate']),
                'location_unit': row['location_unit'],
                'reading_time': format_timestamp(row['reading_time'])}
            ))

        self._session.execute(batch)

    def get_location_readings_for_journey(self, spacecraft_name, journey_id, page_size=25, page_state=None):
        stmt = BoundStatement(self.select_prep_stmt, fetch_size=int(page_size)).bind({
            'spacecraft_name': spacecraft_name,
            'journey_id': uuid_from_string(journey_id)}
        )
        result = self._session.execute(stmt, paging_state=page_state.decode('hex') if page_state else None)

        return result
