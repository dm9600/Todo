#A simple todo webapp
#by David Mai
#Current task: implement flash messages

import bottle
from bottle import *
from TodoList import *
from validators import *
from beaker.middleware import SessionMiddleware
from bottle_flash import *
import pdb

@get('/new_list')
def new_list():
    session = bottle.request.environ.get('beaker.session')

    #Initialize Messages
    session["messages"]=[""]

    #Create the template with the messages set
    view = template('todo.tpl', name="boo", messages = session["messages"])
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
    session = bottle.request.environ.get('beaker.session')
    if not "messages" in session:
        session["messages"] = []
    
    #Get the name of the requested list
    list_name = request.forms.get('existing_list')

    #If the file exists (from validator.py)
    if does_file_exist(list_name + ".ser"):
        #Load the list
        currentTodoList = loadTodoList(list_name).todolist
        return_value = template("view_existing_list.tpl", currentTodoList=currentTodoList, list_name=list_name, messages=session["messages"])
        
        #Save the current list name in session
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
    if not "messages" in session:
        session["messages"] = []
        
    current_list = TodoList([], "nothing")

    #Get todo and priority from request, and create todo object
    todo_to_add = request.forms.get("todo")
    priority_to_add = request.forms.get("priority")

    #Validate the priority
    #Checks if it's a number and it's between 1 and 5
    if not is_valid_priority(priority_to_add) :
        pdb.set_trace()
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
    else:
        session["messages"].append(is_valid_priority(priority))
        return_value = template("todo.tpl", messages=session["messages"])
        return
        
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
    #Get file and filename
    list_file = request.files["file"].file
    filename = request.files["file"].filename

    #Convert file into TodoList object
    current_list = loadFromFile2(list_file, filename)
    session = bottle.request.environ.get('beaker.session')
    saveTodoList2(current_list)

    #Set the current list
    session["current_list"] = current_list.listName
    return_value = template("view_existing_list.tpl", currentTodoList=current_list.todolist, list_name=current_list.listName)
    return return_value

@get('/export_to_file')
def export_to_file():
    
    #Load list from session
    session = bottle.request.environ.get('beaker.session')
    current_list = loadTodoList(session["current_list"])

    #Get the list as a file
    return_value = outputAsFile2(current_list, session["current_list"])

    #Set the response type as a file attachment
    response.content_type='text/plain'
    response.headers['Content-Disposition']= 'attachment; filename=\"' + current_list.listName + '.txt\"'
    
    return return_value
    
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

#Initialize messages
def initialize_messages(session):
    if not "messages" in session:
        session["messages"] = [""]
        
app = SessionMiddleware(bottle.app(), session_opts)
run(app=app, host='localhost', port=6080, debug=True, reloader=False)



