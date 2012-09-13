<?xml version="1.0" encoding="iso-8859-1"?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.1//EN"
"http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
  <head>
    <title>View Existing List</title>
  </head>
  <body>
    <h1>
      {{list_name}}
    </h1>
    <form action="/remove_todo" method="post">
      %for x in currentTodoList:
      <div>
	<span>
	  <input type="submit" name="todo_index" value = {{currentTodoList.index(x) + 1}} />
	</span>
	<span>
	  {{x.todo}}
	</span>
	<span>
	  {{x.priority}}
	</span>
      </div>
      %end
    </form>
    <form action="/add_todo" method="post">
      <div>
	Todo: <input type="text" name="todo" value="Randomtxt"/>
	Priority: <input type="text" name="priority" value="Randomtxt"/>
	<input type="submit" value="Add Todo"/>
      </div>
    </form>
    <form action="/export_to_file" method="post">
    </form>
  </body>
</html>