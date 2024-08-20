import unittest
from models import Employee, SecretSantaAssignment
from assignment import SecretSantaAssigner

class TestSecretSantaAssigner(unittest.TestCase):
    def test_assign_secret_santa(self):
        employees = [
            Employee('Alice', 'alice@example.com'),
            Employee('Bob', 'bob@example.com'),
            Employee('Charlie', 'charlie@example.com')
        ]
        
        last_year_assignments = [
            SecretSantaAssignment(employees[0], employees[1]),
            SecretSantaAssignment(employees[1], employees[2]),
            SecretSantaAssignment(employees[2], employees[0])
        ]

        assignments = SecretSantaAssigner.assign_secret_santa(employees, last_year_assignments)
        self.assertEqual(len(assignments), 3)
        self.assertNotEqual(assignments[0].secret_child, employees[1])

if __name__ == '__main__':
    unittest.main()
