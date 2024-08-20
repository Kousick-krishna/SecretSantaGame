from file_handler import FileHandler
from assignment import SecretSantaAssigner

def main():
    employees = FileHandler.read_employees('data/employees.csv')
    last_year_assignments = FileHandler.read_last_year_assignments('data/last_year_assignments.csv')
    
    try:
        assignments = SecretSantaAssigner.assign_secret_santa(employees, last_year_assignments)
        FileHandler.write_assignments(assignments, 'data/current_year_assignments.csv')
        print("Secret Santa assignments completed successfully!")
    except ValueError as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()
