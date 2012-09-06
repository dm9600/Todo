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
    %for x in currentTodoList:
    <div>
      <span>
	{{x.todo}}
      </span>
      <span>
	{{x.priority}}
      </span>
    </div>
    %end
  </body>
</html>