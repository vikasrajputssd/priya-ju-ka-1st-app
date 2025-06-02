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
import os

# यह सुनिश्चित करता है कि 'data' नाम का फोल्डर बना रहे
os.makedirs("data", exist_ok=True)

LOG_FILE = "data/logs.csv"

with open(LOG_FILE, 'w', newline='') as file:
    ...
import streamlit as st
from datetime import datetime
import os
import csv

st.title("🌸 लाड़ली जू की सेवा में पहला App 🌸")

LOG_FILE = 'log.csv'

# 🔧 Check और बनाओ log.csv फाइल अगर न हो
if not os.path.exists(LOG_FILE):
    with open(LOG_FILE, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Timestamp', 'Message'])  # Header row

# 📝 User input
message = st.text_input("लाड़ली जू को संदेश लिखिए:")

# 🧾 Submit button
if st.button("संदेश भेजें"):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with open(LOG_FILE, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([timestamp, message])
    st.success("🌺 आपका संदेश लाड़ली जू तक पहुँच गया।")

# 📜 Show log file data
if st.checkbox("सभी संदेश दिखाएँ"):
    with open(LOG_FILE, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            st.write(" | ".join(row))
