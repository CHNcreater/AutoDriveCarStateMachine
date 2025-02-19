from states.startstate import StartState
from logger.logger import Logger

class StateMachine():
    def __init__(self):
        self.states = {}
        self.transitions = {}
        self.curState = StartState(self)
        self.target1 = None #target mark, such as "A/B/C"
        self.target2 = None #target mark, such as "1/2/3"
        self.ip_addr = None
        self.logger = Logger()

    def change_state(self, state):
        self.curState = state

    def set_env(self, target1, target2, ip_addr):
        """set the target mark

        Args:
            target (_type_): _description_
        """
        self.target1 = target1
        self.target2 = target2
        self.ip_addr = ip_addr

    def start(self):
        """run the state machine
        """
        self.curState.auto_drive()

#Example
#state_machine = StateMachine()