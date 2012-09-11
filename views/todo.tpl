<?xml version="1.0" encoding="iso-8859-1"?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.1//EN"
"http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
  <head>
    <title>New List</title>
  </head>
  <body>
    <form action="/new_list" method="post">
      <div>
	New List: <input type="text" name="list_name" value="Randomtxt" />
	<input type="submit" value="Submit" />
      </div>
    </form>
    <form action="/view_existing_list" method="post">
      <div>
	Existing List: <input type="text" name="existing_list" value="Randomtxt"/>
	<input type="submit" value="Submit"/>
      </div>
    </form>
    <form action="/load_from_file" method="post" enctype="multipart/form-data">
      <div>
	Load File: <input type="file" name="file" />
	<input type="submit" value="Submit"/>
      </div>
    </form>
  </body>
</html>
