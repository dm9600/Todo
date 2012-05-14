#TodoList version 1.0
#by David Mai
#A simple todo list program
#Todo: saveTodo

#The function that starts up the program
def newTodoList():
    
    #The initial menu
    print "Hello User, would you like to create a new Todo List or modify an existing one?"
    print "a) Create new List"
    print "b) View existing list"
    response = raw_input(">")

    #If the user decides to create a new list
    if response == "a":
        print "Please give your new list a name"
        listName = raw_input(">")
        newList = TodoList("empty", listName)
        print "You have created a new list with name " + listName + ". Would you like to:"
        print "a) Add a todo"
        print "b) exit"
        response = raw_input(">")
        
        #If the user wants to add an item to their newly created list
        if response == "a":
            addTodo(newList)
        #Exit
        elif response == "b":
            print "Goodbye User"

    #If the user decides to see an existing list
    elif response == "b":
        print "Please enter in your list's name"
        listName = raw_input(">")
        viewTodoList(listName)

def addTodo(todoList):
    #Todo item
    print "Please enter something you need to do"    
    newTodoItem = raw_input(">")

    #Todo priority
    print "Now enter in a priority for your todo"
    newPriority = raw_input(">")
    print newPriority

    #Raw input comes out as a string, so it needs to get cast first
    if int(newPriority) > 0 and int(newPriority) <= 10:
        newTodo = Todo(newPriority, newTodoItem)
        todoList.addTodo(newTodo)        
        print "You've created a new Todo: " + newTodoItem + " with a priority of " + newPriority + ". What would you like to do now?"
        print "a) View my list"
        print "b) Save and quit"
        response = raw_input(">")

        #Based on the user response, call the appropriate functions
        if response == "a":
            viewTodoList(todoList)
        elif response == "b":
            saveTodoList():
            exit():
    else:
        print "whatever"
    return

def viewTodoList(TodoList):
    return
def removeTodo(index):
    return
def modifyTodo(index):
    return
def modifyTodoList(listName):
    return
def saveTodoList(TodoList):
    return
def loadTodoList(listName):
    return

class TodoList:
    todolist = "empty"
    listName = "no name"

    def __init__(self, todolist, listName):
        self.todolist = todolist
        self.listName = listName

    def addTodo(self, todo):
        if self.todolist == "empty":
            self.todolist = [todo]
        elif isinstance(self.todolist, list) == true:            
            self.todolist.append(todo)

    def todoComparator(todo1, todo2):
        return todo1.getPriority() - todo2.getPriority

    def sortTodos(self):
        self.todolist = self.todolist.sort(todoComparator)

class Todo:
    priority = 0
    todo = "nothing"

    def __init__(self, priority, todo):
        self.priority = priority
        self.todo = todo

    def setPriority(self, priority):
        self.priority = priority
        
    def getPriority(self):
        return self.priority

    def setTodo(self, todo):
        self.todo = todo
        
    def getTodo(self):
        return self.todo
        

