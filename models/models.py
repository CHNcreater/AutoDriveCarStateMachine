from dataclasses import dataclass
from dataclasses_json import dataclass_json

@dataclass
@dataclass_json
class ActionModel:
    action: str

if __name__ == '__main__':
    action = ActionModel()
    action.action = "move forward"
    print(action.to_json())
    