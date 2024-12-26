class BaseState():
    def __init__(self, state_machine):
        self.state_machine = state_machine

    def on_enter(self):
        pass

    def on_exit(self):
        pass

    def update(self, dt):
        pass

    def handle_event(self, event):
        pass