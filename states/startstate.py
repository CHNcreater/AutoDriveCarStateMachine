from states.basestate import BaseState

class StartState(BaseState):
    def __init__(self):
        super().__init__()
        self.name = 'start'
        self.transitions = {
            'next': 'state1'
        }

    def on_enter(self):
        print('Entering start state')

    def on_exit(self):
        print('Exiting start state')

    def next(self):
        self.transition('next')