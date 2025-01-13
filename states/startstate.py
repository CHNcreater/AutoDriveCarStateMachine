from states.basestate import BaseState
from states.autodrivingstate import AutoDrivingState

class StartState(BaseState):
    def __init__(self):
        super().__init__()

    def move_forward(self):
        print("Moving forward")

    def turn_direction(self):
        print("Turning direction")

    def u_turn(self):
        print("Making a U-turn")

    def input_target(self, target1, target2):
        self.state_machine.set_target(target1, target2)
        self.state_machine.change_state(AutoDrivingState(self.state_machine))
        self.state_machine.auto_drive()
