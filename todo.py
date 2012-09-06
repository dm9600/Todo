from bottle import *
from TodoList import *

#You can bind multiple routes to one function, but not vice versa

@get('/new_list')
def new_list():
    view = template('todo.tpl', name="boo")
    return view

@post('/new_list')
def new_list_post():
    list_name = request.forms.get('list_name')
    new_list = newTodoList2(list_name)
    
    sample_todo = Todo(1, "blah")
    new_list.addTodo(sample_todo)
    new_list.addTodo(sample_todo)
    saveTodoList2(new_list)
    return "You've successfully added a new list with name " + list_name

@post('/view_existing_list')
def view_existing_list():
    list_name = request.forms.get('existing_list')
    currentTodoList = loadTodoList(list_name).todolist
    view = template("view_existing_list.tpl", currentTodoList=currentTodoList, list_name=list_name)
    return view
    

@get('/add_todo')
def add_todo():
    newTodoList()
    return template('todo.tpl')

@post('/add_todo')
def add_todo_post():
    todo = request.forms.get('Todo')
    priority = request.forms.get('Priority')
    return 'boo'
    

@route('/hello')
def hello():
    return 'Hello Worl'

#Starts the web server
run(host='localhost', port=6080, debug=True, reloader=False)



