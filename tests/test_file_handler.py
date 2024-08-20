import unittest
from file_handler import FileHandler
from models import Employee, SecretSantaAssignment
import os

class TestFileHandler(unittest.TestCase):

    def setUp(self):
        # Set up test files
        self.test_employee_file = 'test_employees.csv'
        self.test_assignment_file = 'test_assignments.csv'
        
        with open(self.test_employee_file, 'w') as f:
            f.write("Employee_Name,Employee_EmailID\n")
            f.write("Alice,alice@example.com\n")
            f.write("Bob,bob@example.com\n")

        with open(self.test_assignment_file, 'w') as f:
            f.write("Employee_Name,Employee_EmailID,Secret_Child_Name,Secret_Child_EmailID\n")
            f.write("Alice,alice@example.com,Bob,bob@example.com\n")
            f.write("Bob,bob@example.com,Alice,alice@example.com\n")

    def tearDown(self):
        # Clean up test files
        os.remove(self.test_employee_file)
        os.remove(self.test_assignment_file)

    def test_read_employees(self):
        employees = FileHandler.read_employees(self.test_employee_file)
        self.assertEqual(len(employees), 2)
        self.assertEqual(employees[0].name, "Alice")
        self.assertEqual(employees[1].email, "bob@example.com")

    def test_read_last_year_assignments(self):
        assignments = FileHandler.read_last_year_assignments(self.test_assignment_file)
        self.assertEqual(len(assignments), 2)
        self.assertEqual(assignments[0].employee.name, "Alice")
        self.assertEqual(assignments[0].secret_child.name, "Bob")

    def test_write_assignments(self):
        employees = [Employee('Alice', 'alice@example.com'), Employee('Bob', 'bob@example.com')]
        assignments = [SecretSantaAssignment(employees[0], employees[1]), SecretSantaAssignment(employees[1], employees[0])]
        
        FileHandler.write_assignments(assignments, self.test_assignment_file)
        
        written_assignments = FileHandler.read_last_year_assignments(self.test_assignment_file)
        self.assertEqual(written_assignments[0].secret_child.name, 'Bob')
        self.assertEqual(written_assignments[1].secret_child.email, 'alice@example.com')

if __name__ == '__main__':
    unittest.main()
