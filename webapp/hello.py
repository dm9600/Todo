from bottle import *

@route('/')
@route('/hello/<name>')
def greet(name='Stranger'):
    return 'Hello %s, how are you?' % name

@route('/object/<id:int>')
def callback(id):
    return 'Hello int'

@route('/object/<name:re:[a-z]+>')
def callback(name):
    return 'Hello alpha'

@route('/login2')
def login():
    username = request.forms.get('username')
    password = request.forms.get('password')
    if True:
        response.set_cookie("account", username, secret='key')
    else:
        return "Login failed."

@route('/counter')
def counter():
    count = int(request.cookies.get('counter', '1'))
    count += 1
    response.set_cookie('counter', str(count))
    return 'You visited this page %d times' % count

@route('/restricted')
def restricted_area():
    username = request.get_cookie("account", secret='key')
    if username:
        return "Hello %s. Welcome back." % username
    else:
        return "You are not logged in. Access denied."

@get('/login') # or @route('/login')
def login_form():
    return '''<form method="POST" action="/login">
                <input name="name"     type="text" />
                <input name="password" type="password" />
                <input type="submit" />
              </form>'''

@post('/login')
def login_submit():
    name = request.forms.get('name')
    password = request.forms.get('password')
    return name + password

@route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='./css/styles.css')

@route('/img/<filename:path>')
#def send_image(filename):
 #   return static_file(filename, root='./img/')

@route('/img/<filename:re:.*\.jpg>#')
def send_image(filename):
    return static_file(filename, root='./img/', mimetype='image/jpg')

@route('/download/<filename:path>')
def download(filename):
    return static_file(filename, root='./img/', download=filename)

@error(404)
def error404(error):
    return 'Nothing here, sorry'

@route('/restricted')
def restricted():
    abort(401, "Sorry, access denied.")

@route('/wrong/url')
def wrong():
    redirect("/img/zen_palate.jpg")

@route('/hello')
def hello_again():
    if request.get_cookie("visited"):
        return "Welcome back! Nice to see you again"
    else:
        response.set_cookie("visited", "yes")
        return "konichiwa"

@route('/is_ajax')
def is_ajax():
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return 'This is an AJAX request'
    else:
        return 'This is a normal request'

@get('/upload') # or @route('/login')
def login_form():
   return '''<input name="name"     type="text" />
                <input name="file" type="data" />
                <input type="submit" />
              </form>'''
    
@post('/upload')
def do_upload():
    name = request.forms.name
    data = request.files.data
    if name and data and data.file:
        raw = data.file.read()
        filename = data.filename
        return "Hello %s! You uploaded %s (%d bytes)." %(name, filename, len(raw))
    return "You missed a field."

@route('/my_ip')
def show_ip():
    ip = request.environ.get('REMOTE_ADDR')
    # or ip = request.get('REMOTE_ADDR')
    # or ip = request['REMOTE_ADDR']'
    return "Your IP is: %s" % ip

@route('jello')
@route('/jello/<name>')
def hello(name='World'):
    return dict(name=name)

@route('xello')
@route('/xello/<name>')
def hello(name='World'):
    return template('hello_template', name=name)

    
run(host='localhost', port=8080, debug=True, reloader=True)
