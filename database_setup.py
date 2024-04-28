# database_setup.py

import sqlite3

def create_database():
    conn = sqlite3.connect('exam_scheduler.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS students (
                        student_id INTEGER PRIMARY KEY,
                        name TEXT
                    )''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS classes (
                        class_id INTEGER PRIMARY KEY,
                        class_name TEXT
                    )''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS subjects (
                        subject_id INTEGER PRIMARY KEY,
                        subject_name TEXT
                    )''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS exams (
                        exam_id INTEGER PRIMARY KEY,
                        subject_id INTEGER,
                        FOREIGN KEY (subject_id) REFERENCES subjects(subject_id)
                    )''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS classrooms (
                        classroom_id INTEGER PRIMARY KEY,
                        capacity INTEGER
                    )''')

    students = [('Kalia',), ('Bholu',), ('Chutki',), ('Dholu',)]
    cursor.executemany("INSERT INTO students (name) VALUES (?)", students)

    classes = [('Class A',), ('Class B',), ('Class C',)]
    cursor.executemany("INSERT INTO classes (class_name) VALUES (?)", classes)

    subjects = [('Math',), ('Science',), ('History',)]
    cursor.executemany("INSERT INTO subjects (subject_name) VALUES (?)", subjects)

    classrooms = [(1, 30), (2, 25), (3, 35)]
    cursor.executemany("INSERT INTO classrooms (classroom_id, capacity) VALUES (?, ?)", classrooms)

    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_database()
