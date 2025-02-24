class CommandManager:
    def __init__(self):
        self.history = []
        self.command = None

    def add(self, command):
        self.command = command
        self.history.append(self.command)

    def execute(self):
        # we can refactor this command manager to a threat, which contains a task queue.
        # when user adds new task, this thread will pick up one task to execute
        self.command.execute()