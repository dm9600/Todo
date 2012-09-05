from bottle import *
import todo

#You can bind multiple routes to one function, but not vice versa
@get('/add_todo')
def add_todo():
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
run(host='localhost', port=8080, debug=True, reloader=False)



