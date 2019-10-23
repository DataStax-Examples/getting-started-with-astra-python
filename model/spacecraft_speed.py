class SpacecraftSpeed(object):

    def __init__(self, spacecraft_name, journey_id, speed, speed_unit, reading_time):
        self.spacecraft_name = spacecraft_name
        self.journey_id = journey_id
        self.speed = speed
        self.speed_unit = speed_unit
        self.reading_time = reading_time

    def to_string(self):
        return 'SpacecraftSpeed [spacecraft_name={sc_n}, journey_id={j_id}, speed={s}, speed_unit={su}, ' \
               'reading_time={r}]'.format(sc_n=self.spacecraft_name, j_id=self.journey_id, s=self.speed,
                                          su=self.speed_unit, r=self.reading_time)
