class SpacecraftPressure(object):

    def __init__(self, spacecraft_name, journey_id, pressure, pressure_unit, reading_time):
        self.spacecraft_name = spacecraft_name
        self.journey_id = journey_id
        self.pressure = pressure
        self.pressure_unit = pressure_unit
        self.reading_time = reading_time

    def to_string(self):
        return 'SpacecraftPressure [spacecraft_name={sc_n}, journey_id={j_id}, pressure={p}, pressure_unit={pu}, ' \
               'reading_time={r}]'.format(sc_n=self.spacecraft_name, j_id=self.journey_id, p=self.pressure,
                                          pu=self.pressure_unit, r=self.reading_time)
