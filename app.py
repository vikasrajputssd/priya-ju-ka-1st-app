from flask import Flask, render_template, request, redirect
import csv
from datetime import datetime
import os

app = Flask(__name__)

LOG_FILE = 'data/logs.csv'

if not os.path.exists(LOG_FILE):
    with open(LOG_FILE, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Time', 'Place of Mind', 'Emotion', 'What Was Bigger Than Name'])

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        place = request.form['place']
        emotion = request.form['emotion']
        distraction = request.form['distraction']
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        with open(LOG_FILE, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([now, place, emotion, distraction])

        return redirect('/')

    return render_template('index.html')
    
if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, redirect
import csv
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    data = {
        'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        'location': request.form['location'],
        'thoughts': request.form['thoughts'],
        'distraction': request.form['distraction'],
        'emotion': request.form['emotion'],
        'realization': request.form['realization']
    }
    with open('data/logs.csv', 'a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(data.values())
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
