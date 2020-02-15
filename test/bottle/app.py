

from bottle import error
from bottle import static_file
from bottle import route, run,template

@route('/hello')
def hello():
    return "Hello World!"


@route('/hello/<name>')
def greet(name='Stranger'):
    return template('Hello {{name}}, how are you?', name=name)



# @route('/static/<filename>')
# def server_static(filename):
#     return static_file(filename, root='/Users/xinxi/Documents/sndd/dockerflask/')

@route('/static/<filepath:path>')
def server_static(filepath):
    print(filepath)
    return static_file(filepath, root='/Users/xinxi/Documents/sndd/dockerflask/')



@error(404)
def error404(error):
    return 'Nothing here, sorry'


run(host='localhost', port=8080, debug=True)