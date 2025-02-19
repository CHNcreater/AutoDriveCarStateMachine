from states.basestate import BaseState
from states.autodrivingstate import AutoDrivingState


class StartState(BaseState):
    def __init__(self, stateMachine):
        super().__init__(state_machine=stateMachine)

    def auto_drive(self):
        self.state_machine.logger.log(
            f"Start State auto drive is called, target1:{self.state_machine.target1}, target2:{self.state_machine.target2}, camera_ip_addr:{self.state_machine.ip_addr}, mosquitto_ip_addr: {self.state_machine.mosquitto}"
        )
        self.state_machine.change_state(AutoDrivingState(self.state_machine))
        self.state_machine.curState.auto_drive()
