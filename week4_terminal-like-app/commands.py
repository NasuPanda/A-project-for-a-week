from dataclasses import dataclass

@dataclass
class Command:
    name: str
    handler: callable # A function to execute the command
