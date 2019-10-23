from uuid import UUID
from datetime import datetime

from cql_file_util import get_cql_schema_string_from_file
from cassandra.query import BoundStatement


class SpacecraftPressureDAO(object):

    table_name = "spacecraft_pressure_over_time"

    create_stmt = get_cql_schema_string_from_file(table_name)

    insert_stmt = 'INSERT INTO {table_name} (spacecraft_name, journey_id, pressure, pressure_unit, reading_time) ' \
                  'VALUES (:spacecraft_name,:journey_id,:pressure,:pressure_unit,:reading_time);'.format(table_name=table_name)

    select_stmt = 'SELECT * FROM {table_name} WHERE spacecraft_name = :spacecraft_name AND journey_id = :journey_id;' \
                  ''.format(table_name=table_name)

    def __init__(self, _session):
        self._session = _session
        self.maybe_create_schema()
        self.insert_prep_stmt = _session.prepare(self.insert_stmt)
        self.select_prep_stmt = _session.prepare(self.select_stmt)
        self.page_state = None

    def maybe_create_schema(self):
        self._session.execute(self.create_stmt)

    def write_reading(self, spacecraft_name, journey_id, pressure, pressure_unit, reading_time):
        journey_id = UUID('{u}'.format(u=journey_id))
        pressure = float(pressure)
        reading_time = datetime.strptime(reading_time.replace('0000', '').replace('+', '').strip(), '%Y-%m-%dT%H:%M:%S')

        def handle_success(results):
            print 'Successfully wrote row'

        def handle_error(exception):
            raise Exception('Failed to write row: ' + exception)

        insert_future = self._session.execute_async(self.insert_prep_stmt.bind({
            'spacecraft_name': spacecraft_name,
            'journey_id': journey_id,
            'pressure': pressure,
            'pressure_unit': pressure_unit,
            'reading_time': reading_time}
        ))

        insert_future.add_callbacks(handle_success, handle_error)

    def get_pressure_readings_for_journey(self,  spacecraft_name, journey_id, page_size, page_state=None):
        journey_id = UUID('{u}'.format(u=journey_id))

        stmt = BoundStatement(self.select_prep_stmt, fetch_size=int(page_size)).bind({
            'spacecraft_name': spacecraft_name,
            'journey_id': journey_id}
        )
        result = self._session.execute(stmt, paging_state=page_state)

        return result
