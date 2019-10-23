class SpacecraftJourneyCatalog(object):

    def __init__(self, spacecraft_name, journey_id, start, end, active, summary):
        self.spacecraft_name = spacecraft_name
        self.journey_id = journey_id
        self.start = start
        self.end = end
        self.active = active
        self.summary = summary

    def to_string(self):
        return 'SpacecraftJourneyCatalog [spacecraft_name={sc_n}, journey_id={j_id}, start={s}, end={e}, ' \
               'active={a}, summary={sum}]'.format(sc_n=self.spacecraft_name, j_id=self.journey_id, s=self.start,
                                                   e=self.end, a=self.active, sum=self.summary)
