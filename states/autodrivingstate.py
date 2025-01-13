from states.basestate import BaseState
from states.catchingstate import CatchingState
from actions.drivecar import drive_car

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
            isArrived = drive_car()
        self.state_machine.change_state(CatchingState(self.state_machine))