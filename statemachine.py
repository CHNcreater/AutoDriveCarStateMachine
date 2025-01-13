from states.basestate import BaseState
from states.startstate import StartState

class StateMachine():
    def __init__(self):
        self.states = {}
        self.transitions = {}
        self.curState = StartState(self)
        self.target1 = None #target mark, such as "A/B/C"
        self.target2 = None #target mark, such as "1/2/3"

    def change_state(self, state: BaseState):
        pass

    def set_target(self, target1, target2):
        """set the target mark

        Args:
            target (_type_): _description_
        """
        self.target1 = target1
        self.target2 = target2

    def drive(self, args):
        """send drive command to the car

        Args:
            args (_type_): _description_
        """
        pass

    def run(self, target):
        """run the state machine
        """
        self.target = target
        change_state(StartState)
        pass

    def auto_drive(self):
        """auto drive the car
        """
        self.curState.auto_drive()

#Example
#state_machine = StateMachine()