from cql_file_util import get_cql_schema_string_from_file


class SpacecraftJourneyCatalogDAO(object):

    table_name = "spacecraft_journey_catalog"

    create_stmt = get_cql_schema_string_from_file(table_name)

    insert_stmt = 'INSERT INTO {table_name} (spacecraft_name, journey_id, start, end, active, summary) ' \
                  'VALUES (:spacecraft_name,:journey_id,:start,:end,:active,:summary);'.format(table_name=table_name)

    select_all_journeys_stmt = 'SELECT * FROM {table_name};'.format(table_name=table_name)

    select_all_journeys_for_spacecraft_stmt = 'SELECT * FROM {table_name} WHERE spacecraft_name = :spacecraft_name;' \
                                              ''.format(table_name=table_name)

    select_single_journey_for_spacecraft_stmt = 'SELECT * FROM {table_name} ' \
                                                'WHERE spacecraft_name = :spacecraft_name AND journey_id = :journey_id;' \
                                                ''.format(table_name=table_name)

    def __init__(self, _session):
        self._session = _session
        self.maybe_create_schema()
        self.insert_prep_stmt = _session.prepare(self.insert_stmt)
        self.select_all_prep_stmt = _session.prepare(self.select_all_journeys_stmt)
        self.select_all_for_spacecraft_prep_stmt = _session.prepare(self.select_all_journeys_for_spacecraft_stmt)
        self.select_single_for_spacecraft_prep_stmt = _session.prepare(self.select_single_journey_for_spacecraft_stmt)

    def maybe_create_schema(self):
        self._session.execute(self.create_stmt)

    def write_journey(self, spacecraft_name, journey_id, start, end, active, summary):

        def handle_success(results):
            pass

        def handle_error(exception):
            raise Exception('Failed to write row: ' + exception)

        insert_future = self._session.execute_async(self.insert_prep_stmt.bind({
            'spacecraft_name': spacecraft_name,
            'journey_id': journey_id,
            'start': start,
            'end': end,
            'active': active,
            'summary': summary}
        ))

        insert_future.add_callbacks(handle_success, handle_error)

    def get_all_journeys(self):
        result = self._session.execute(self.select_all_prep_stmt)
        return result

    def get_all_journeys_for_spacecraft(self, spacecraft_name):
        result = self._session.execute(self.select_all_for_spacecraft_prep_stmt.bind({
            'spacecraft_name': spacecraft_name}
        ))
        return result

    def get_single_journey_for_spacecraft(self, spacecraft_name, journey_id):
        result = self._session.execute(self.select_single_for_spacecraft_prep_stmt.bind({
            'spacecraft_name': spacecraft_name,
            'journey_id': journey_id}
        ))

        return result
