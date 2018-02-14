class Task:
    def __init__(self, name, duration, precedence=5, prereqs=None, finish=None):
        self.name       = name
        self.duration   = duration
        self.precedence = precedence
        self.prereqs    = prereqs
        self.finish     = finish

    def __str__(self):
        return '{} {} min'.format(self.name, self.duration)
        # return '{} {} {} {} {}'.format(self.name,
        #                                self.duration,
        #                                self.precedence,
        #                                self.prereqs,
        #                                self.finish)
    def __repr__(self):
        return '<{}>'.format(str(self))
