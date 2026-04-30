from flask import Flask, request, redirect

app = Flask(__name__)

tasks = []

@app.route('/')
def home():
    task_list = ""
    for i, task in enumerate(tasks):
        task_list += f"<li>{task} <a href='/delete/{i}'>Delete</a></li>"

    return f'''
    <h1>To-Do App</h1>
    <form action="/add" method="post">
        <input type="text" name="task" placeholder="Enter task">
        <button type="submit">Add</button>
    </form>
    <ul>{task_list}</ul>
    '''

@app.route('/add', methods=['POST'])
def add():
    task = request.form.get('task')
    tasks.append(task)
    return redirect('/')

@app.route('/delete/<int:index>')
def delete(index):
    tasks.pop(index)
    return redirect('/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)