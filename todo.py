#A simple todo webapp
#by David Mai
#Current task: finish load_from_file

import bottle
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

    #Get the list name, and make a new list, save
    list_name = request.forms.get('list_name')
    new_list = newTodoList2(list_name)
    saveTodoList2(new_list)

    #Save the current list name in session
    session = bottle.request.environ.get('beaker.session')
    if not "current_list" in session:
        session["current_list"] = list_name
        print list_name + " was saved in session"

    #Reroute to view_existing_list
    if isinstance(new_list, TodoList) and isinstance(list_name, str):
        return_value = template("view_existing_list.tpl", currentTodoList=new_list.todolist, list_name=list_name)
    else:
        return_value = "Not a valid list or list name"

    return return_value

@post('/view_existing_list')
def view_existing_list():
    #Get the name of the requested list
    list_name = request.forms.get('existing_list')

    #If the file exists (from validator.py)
    if does_file_exist(list_name + ".ser"):
        #Load the list
        currentTodoList = loadTodoList(list_name).todolist
        return_value = template("view_existing_list.tpl", currentTodoList=currentTodoList, list_name=list_name)
        
        #Save the current list name in session
        session = bottle.request.environ.get('beaker.session')
        if not "current_list" in session:
            session["current_list"] = list_name
            print list_name + " was saved in session"
    else:
        return_value = "list was not found"
    return return_value

@post('/add_todo')
def add_todo():

    #Get the session and set default current_list
    session = bottle.request.environ.get('beaker.session')
    current_list = TodoList([], "nothing")

    #Get todo and priority from request, and create todo object
    todo_to_add = request.forms.get("todo")
    priority_to_add = request.forms.get("priority")
    todo = Todo(priority_to_add, todo_to_add)

    #If current_list is defined...
    if "current_list" in session:
        
        #Load the list name from session, and load list
        list_name = session["current_list"]
        current_list = loadTodoList(list_name)

        #Add the todo object to the todolist, and save
        current_list.addTodo(todo)
        saveTodoList2(current_list)
        return_value = template("view_existing_list.tpl", currentTodoList=current_list.todolist, list_name=list_name)
    else:
        #Shouldn't ever get here
        print session
        return_value = "no list in session"
    
    return return_value

@post("/remove_todo")
def remove_todo():

    #Load list from session, define default values
    index = int(float(request.forms.get("todo_index")))
    session = bottle.request.environ.get('beaker.session')
    current_list = TodoList(list(), "default listname")
    return_value = "default value"
    list_name = "none assigned"
    
    if "current_list" in session:
        list_name = session["current_list"]

        #Remove the todo from the list and save
        current_list = removeTodo2(loadTodoList(list_name), index - 1)
        saveTodoList2(current_list)
        return_value = template("view_existing_list.tpl", currentTodoList=current_list.todolist, list_name=list_name)

    return return_value

@post('/load_from_file')
def load_from_file():
    list_file = request.files["file"].file
    filename = request.files["file"].filename

    TodoList_from_file = loadFromFile2(list_file, filename)
    for todo in list_file.readlines():
        print todo
    return 
    
@route('/hello')
def hello():
    return 'Hello Worl'

#Starts the web server
session_opts = {
    'session.type': 'file',
    'session.cookie_expires': 300,
    'session.data_dir': './data',
    'session.auto': True
}
app = SessionMiddleware(bottle.app(), session_opts)
run(app=app, host='localhost', port=6080, debug=True, reloader=False)



