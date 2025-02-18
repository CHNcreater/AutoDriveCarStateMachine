from states.basestate import BaseState
from states.startstate import StartState

class StateMachine():
    def __init__(self):
        self.states = {}
        self.transitions = {}
        self.curState: BaseState = StartState(self)
        self.target1 = None #target mark, such as "A/B/C"
        self.target2 = None #target mark, such as "1/2/3"
        self.ip_addr = None

    def change_state(self, state: BaseState):
        pass

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

def start(target1, target2, ip_addr):
    stateMachine = StateMachine()
    stateMachine.set_env(target1=target1, target2=target2, ip_addr=ip_addr)
    stateMachine.start()

if __name__ == '__main__':
    start(1,2,3)

#Example
#state_machine = StateMachine()