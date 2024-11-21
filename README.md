# Student Management System

A simple Flask-based application to manage student records.

## Features
- Add students with name, email, and age.
- View all students in a table.

## Technologies Used
- **Flask** for the backend
- **SQLite** for the database
- **HTML/CSS** for the frontend

## How to Run
1. Clone the repository:
   git remote add origin https://github.com/shilpan16/student_management_system.git
2. Navigate to the project directory:
   cd student-management-system
3. Install dependencies:
   pip install -r requirements.txt
4. Create the database:
   sqlite3 students.db < schema.sql sqlite3 students.db < data.sql
5. Run the application:
   python app.py
6. Open the app in your browser at `http://127.0.0.1:5000/`.

## License
This project is licensed under the MIT License.
