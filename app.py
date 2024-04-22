# app.py

from flask import Flask, render_template
from backend import ExamScheduler

app = Flask(__name__)
scheduler = ExamScheduler()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/schedule')
def schedule():
    # Schedule exams
    scheduler.schedule_exams()
    # Update database
    scheduler.update_database()
    # Render schedule template
    return render_template('schedule.html')

if __name__ == '__main__':
    app.run(debug=True)
