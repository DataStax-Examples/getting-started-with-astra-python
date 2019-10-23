class SpacecraftTemperature(object):

    def __init__(self, spacecraft_name, journey_id, temp, temp_unit, reading_time):
        self.spacecraft_name = spacecraft_name
        self.journey_id = journey_id
        self.temp = temp
        self.temp_unit = temp_unit
        self.reading_time = reading_time

    def to_string(self):
        return 'SpacecraftTemperature [spacecraft_name={sc_n}, journey_id={j_id}, temperature={t},  temperature_unit={tu}, ' \
               'reading_time={r}]'.format(sc_n=self.spacecraft_name, j_id=self.journey_id, t=self.temp,
                                          tu=self.temp_unit, r=self.reading_time)
