import sys
sys.path.append("..")
from states.basestate import BaseState
from states.endstate import EndState
from actions.drivecar import navigate_on_autopilot

class ReturningState(BaseState):
    def __init__(self, stateMachine):
        super().__init__(stateMachine)

    def move_forward(self):
        pass

    def turn_direction(self):
        pass

    def u_turn(self):
        pass

    def input_target(self):
        pass

    def auto_drive(self):
        self.state_machine.logger.log("Enter ReturningState and complete task")
        isArrived = False
        i = 0
        while not isArrived and i < 5:
            # isArrived = navigate_on_autopilot()
            i += 1
        self.state_machine.change_state(EndState(self.state_machine))