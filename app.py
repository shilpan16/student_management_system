from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Database connection function
def connect_db():
    conn = sqlite3.connect('students.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM students")
    students = cur.fetchall()
    conn.close()
    return render_template('index.html', students=students)

@app.route('/add_student', methods=['GET', 'POST'])
def add_student():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        age = request.form['age']
        conn = connect_db()
        cur = conn.cursor()
        cur.execute("INSERT INTO students (name, email, age) VALUES (?, ?, ?)", (name, email, age))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))
    return render_template('add_student.html')

if __name__ == '__main__':
    app.run(debug=True)
