from states.basestate import BaseState

class EndState(BaseState):
    def __init__(self, stateMachine):
        super().__init__(stateMachine)
        self.state_machine.logger.log("Stop")

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