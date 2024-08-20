import unittest
from unittest.mock import patch
from file_handler import FileHandler
from assignment import SecretSantaAssigner
from main import main
from models import Employee, SecretSantaAssignment

class TestMain(unittest.TestCase):

    @patch('file_handler.FileHandler.read_employees')
    @patch('file_handler.FileHandler.read_last_year_assignments')
    @patch('file_handler.FileHandler.write_assignments')
    def test_main(self, mock_write_assignments, mock_read_last_year_assignments, mock_read_employees):
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
        mock_read_employees.return_value = employees
        mock_read_last_year_assignments.return_value = last_year_assignments

        main()
        self.assertTrue(mock_write_assignments.called)

if __name__ == '__main__':
    unittest.main()
