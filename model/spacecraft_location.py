class SpacecraftLocation(object):

    def __init__(self, spacecraft_name, journey_id, location, location_unit, reading_time):
        self.spacecraft_name = spacecraft_name
        self.journey_id = journey_id
        self.location = location
        self.location_unit = location_unit
        self.reading_time = reading_time

    def to_string(self):
        return 'SpacecraftLocation [spacecraft_name={sc_n}, journey_id={j_id}, location={loc}, location_unit={lu}, ' \
               'reading_time={r}]'.format(sc_n=self.spacecraft_name, j_id=self.journey_id, loc=self.location,
                                          lu=self.location_unit, r=self.reading_time)
