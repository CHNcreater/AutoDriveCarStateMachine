from states.basestate import BaseState
from states.autodrivingstate import AutoDrivingState

class StartState(BaseState):
    def __init__(self, stateMachine):
        super().__init__(state_machine=stateMachine)

    def auto_drive(self):
        print("Start State auto drive is called")
