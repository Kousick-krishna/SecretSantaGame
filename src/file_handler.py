import csv
from typing import List
from models import Employee, SecretSantaAssignment

class FileHandler:
    @staticmethod
    def read_employees(file_path: str) -> List[Employee]:
        employees = []
        with open(file_path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                employees.append(Employee(row['Employee_Name'], row['Employee_EmailID']))
        return employees

    @staticmethod
    def read_last_year_assignments(file_path: str) -> List[SecretSantaAssignment]:
        assignments = []
        with open(file_path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                employee = Employee(row['Employee_Name'], row['Employee_EmailID'])
                secret_child = Employee(row['Secret_Child_Name'], row['Secret_Child_EmailID'])
                assignments.append(SecretSantaAssignment(employee, secret_child))
        return assignments

    @staticmethod
    def write_assignments(assignments: List[SecretSantaAssignment], file_path: str):
        with open(file_path, 'w', newline='') as csvfile:
            fieldnames = ['Employee_Name', 'Employee_EmailID', 'Secret_Child_Name', 'Secret_Child_EmailID']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for assignment in assignments:
                writer.writerow({
                    'Employee_Name': assignment.employee.name,
                    'Employee_EmailID': assignment.employee.email,
                    'Secret_Child_Name': assignment.secret_child.name,
                    'Secret_Child_EmailID': assignment.secret_child.email
                })
