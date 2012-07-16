#TodoList version 1.0
#by dm9600
#A simple todo list program
#1) Implement all the remaining functions (modifyTodo)
#2) Implement I/O functions

import pickle

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
            exitProgram()

    #If the user decides to see an existing list
    elif response == "b":
        print "Please enter in your list's name"
        listName = raw_input(">")
        currentTodoList = loadTodoList(listName)
        viewTodoList(currentTodoList)

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
            saveTodoList(todoList)
            exit()
    else:
        print "whatever"
    return

def viewTodoList(TodoList):
    print "Here are the current todos on the list: "
    for todo in TodoList.todolist:
        print todo.getPriority() + ": " + todo.getTodo()
    print "What would you like to do?"
    print "a) Add a todo"
    print "b) Remove a todo"
    print "c) Sort list descending"
    print "d) Save list"
    print "e) "
    print "e) Exit"
    
    response = raw_input(">")
    if response == "a":
        addTodo(TodoList)
    elif response == "b":
        print "Please enter the index of the todo to remove"
        index = int(raw_input(">"))
        removeTodo(TodoList, index)
    elif response == "c":
        TodoList.sortTodos()
        print "TodoList has been sorted"
        viewTodoList(TodoList)
    elif response == "d":
        saveTodoList(TodoList)
    elif response == "e":
        exitProgram()

    return

#Removes a todo based on a TodoList and the index of the todo on the list
def removeTodo(TodoList, index):
    #Removes the todo from the list, as well as set it to the variable removedTodo
    removedTodo = TodoList.todolist.pop(0)
    print "You've removed the following todo from your todolist: " + removedTodo.getTodo()
    print "with priority: " + removedTodo.getPriority()
    #Return to view flow when finished
    viewTodoList(TodoList)
    return

def modifyTodo(TodoList, index):
    print "You've selected the todo " + TodoList.todolist[int(index)].todo
    print "What would you like to do with this todo?"
    return
def loadFromFile():
    return
def outputAsFile():
    return
def modifyTodoList(listName):
    return
def exitProgram():
    print "Goodbye User"

def saveTodoList(TodoList):    
    #Creates the filename for the TodoList
    filename = TodoList.listName + ".ser"

    #Defines the file that'll be written. "w" indicates it's writeable
    yourfile = file(filename, "w")
    
    #Serialize the file
    pickle.dump(TodoList, yourfile)
    print "You've saved your list to " + filename
    return

def loadTodoList(listName):
    #Defines the file to look for
    yourfile = file(listName + ".ser", "r")
    
    #Loads the targetted file
    currentTodoList = pickle.load(yourfile)  
    print "You've loaded the TodoList " + listName
    return currentTodoList

class TodoList:
    todolist = "empty"
    listName = "no name"
    
    #Constructor
    def __init__(self, todolist, listName):
        self.todolist = todolist
        self.listName = listName

    #Method for adding todos
    def addTodo(self, todo):
        if self.todolist == "empty":
            self.todolist = [todo]
        elif isinstance(self.todolist, list):            
            self.todolist.append(todo)
    
    #Sorting the list by priority
    def sortTodos(self):
        self.todolist = sorted(self.todolist, key=lambda todo: todo.priority)

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
        

