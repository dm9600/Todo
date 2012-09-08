from bottle import *
from TodoList import *
from validators import *
from beaker.middleware import SessionMiddleware

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

    if isinstance(new_list, TodoList) and isinstance(list_name, str):
        return_value = template("view_existing_list.tpl", currentTodoList=new_list.todolist, list_name=list_name)
    else:
        return_value = "Not a valid list or list name"

    return return_value

@post('/view_existing_list')
def view_existing_list():
    list_name = request.forms.get('existing_list')
    if does_file_exist(list_name + ".ser"):
        abort(404, "The list " + list_name + " already exists")
    else:
        currentTodoList = loadTodoList(list_name).todolist
        return_value = template("view_existing_list.tpl", currentTodoList=currentTodoList, list_name=list_name)        
    return return_value

@post('/add_todo')
def add_todo(todo, priority):
    return

@route('/hello')
def hello():
    return 'Hello Worl'

#Starts the web server
app = Bottle()
run(app=app, host='localhost', port=6080, debug=True, reloader=False)



