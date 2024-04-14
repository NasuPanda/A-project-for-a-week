from dataclasses import dataclass

# TODO Having timestamp
# TODO Having filesize

@dataclass
class File:
    name: str

@dataclass
class Directory:
    name: str
    contents: list[str] # List of files and/or subdirectories
