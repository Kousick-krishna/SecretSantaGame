
from dataclasses import dataclass

@dataclass
class Employee:
    name: str
    email: str

@dataclass
class SecretSantaAssignment:
    employee: Employee
    secret_child: Employee
