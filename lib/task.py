class Task:
    def __init__(self, name, duration, precedence=5, prereqs=None, finish=None):
        self.name       = name
        self.duration   = duration
        self.precedence = precedence
        self.prereqs    = prereqs
        self.finish     = finish
