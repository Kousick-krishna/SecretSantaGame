# Secret Santa Assignment

## Description

This project automates the Secret Santa assignment process among employees. The program reads employee information and last year's Secret Santa assignments from CSV files, assigns a new Secret Santa pair for the current year while ensuring that no employee is assigned to themselves or the same Secret Santa as the previous year.

## Project Structure

SecretSanta/
│
├── src/
│ ├── init.py
│ ├── models.py
│ ├── assignment.py
│ ├── file_handler.py
│ └── main.py
│
├── tests/
│ ├── init.py
│ ├── test_assignment.py
│ ├── test_file_handler.py
│ └── test_main.py
│
├── data/
│ ├── employees.csv
│ └── last_year_assignments.csv
│
├── README.md



## Installation

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd SecretSanta
   Install the required packages:
   bash
   pip install -r requirements.txt
   Usage
   Prepare the CSV files:

Place your employee data in data/employees.csv.
Place last year's Secret Santa assignments in data/last_year_assignments.csv.
Run the main script:

python src/main.py
This will generate a new CSV file, data/current_year_assignments.csv, containing the current year's Secret Santa assignments.

# Testing
To ensure that everything is working correctly, you can run the unit tests:

python -m unittest discover tests
# Error Handling
The program includes error handling for:

Invalid input data
Issues with file reading or writing
Assignment conflicts (e.g., no valid assignments available)
# Documentation
models.py: Contains data models for Employee and SecretSantaAssignment.
assignment.py: Handles the logic for assigning Secret Santa pairs.
file_handler.py: Manages reading and writing CSV files.
main.py: The entry point of the application.
test_assignment.py: Unit tests for assignment.py.
test_file_handler.py: Unit tests for file_handler.py.
test_main.py: Unit tests for main.py.
Version Control
This project is maintained using Git. Ensure you commit your changes and push them to your repository regularly.

# License
This project is licensed under the MIT License - see the LICENSE file for details.
