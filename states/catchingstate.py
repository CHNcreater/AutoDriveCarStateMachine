from states.basestate import BaseState
from states.returningstate import ReturningState

class CatchingState(BaseState):
    def __init__(self, stateMachine):
        super().__init__(state_machine=stateMachine)

    def move_forward(self):
        pass

    def turn_direction(self):
        pass

    def u_turn(self):
        pass

    def input_target(self):
        pass

    def auto_drive(self):
        pass

    def catching(self):
        self.state_machine.logger.log("Enter CatchingState and Perform catching")
        # Get cathing result True or False
        isCatched = True
        if isCatched:
            self.state_machine.logger.log("Start to returning back to start point")
            self.state_machine.change_state(ReturningState(self.state_machine))
            self.state_machine.curState.auto_drive()