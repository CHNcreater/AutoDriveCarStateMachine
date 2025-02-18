import sys
sys.path.append("..")
from states.basestate import BaseState
from states.catchingstate import CatchingState
from actions.drivecar import navigate_on_autopilot

class AutoDrivingState(BaseState):
    def __init__(self):
        super().__init__()

    def move_forward(self):
        pass

    def turn_direction(self):
        pass

    def u_turn(self):
        pass

    def input_target(self):
        pass

    def auto_drive(self):
        isArrived = False
        while not isArrived:
            isArrived = navigate_on_autopilot()
        self.state_machine.change_state(CatchingState(self.state_machine))