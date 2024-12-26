class StateMachine():
    def __init__(self):
        self.states = {}
        self.transitions = {}
        self.curState = None