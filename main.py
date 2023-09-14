from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap
from datetime import datetime

app = Flask(__name__)
Bootstrap(app)
tasks = []

@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

@app.route('/add_task', methods=['POST'])
def add_task():
    task_text = request.form.get('task')
    if task_text:
        current_time = datetime.now()
        tasks.append((task_text, current_time))
    return redirect('/')

@app.route('/delete_task/<int:index>')
def delete_task(index):
    if 0 <= index < len(tasks):
        del tasks[index]
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)

