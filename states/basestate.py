class BaseState():
    def __init__(self, state_machine):
        self.state_machine = state_machine

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
        pass