from states.basestate import BaseState
class StateMachine():
    def __init__(self):
        self.states = {}
        self.transitions = {}
        self.curState = None
        self.target = None #target mark, such as "A2"

    def change_state(self, state: BaseState):
        pass

    def drive(self, args):
        """send drive command to the car

        Args:
            args (_type_): _description_
        """
        pass

#Example
#state_machine = StateMachine()