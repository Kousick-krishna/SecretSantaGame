import random
from typing import List
from models import Employee, SecretSantaAssignment

class SecretSantaAssigner:
    @staticmethod
    def assign_secret_santa(employees: List[Employee], last_year_assignments: List[SecretSantaAssignment]) -> List[SecretSantaAssignment]:
        employee_pool = employees.copy()
        assignments = []

        last_year_map = {(assignment.employee.name, assignment.employee.email): 
                         (assignment.secret_child.name, assignment.secret_child.email) for assignment in last_year_assignments}

        for employee in employees:
            valid_children = [e for e in employee_pool if e != employee and (employee.name, employee.email) != last_year_map.get((employee.name, employee.email))]
            if not valid_children:
                raise ValueError(f"No valid secret child could be assigned to {employee.name}")
            
            secret_child = random.choice(valid_children)
            employee_pool.remove(secret_child)
            assignments.append(SecretSantaAssignment(employee, secret_child))

        return assignments
