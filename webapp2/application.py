from bottle import route, run, template

# @route('/hello/<name>')
# def index(name):
#     return template('<b>Hello {{name}}</b>!', name=name)

@route("/")
def get_index():
    return "Hello, there!"

@route("/hello/<name>")
def get_hello(name):
    return template("hello.tpl", name=name) 

pets = [
    {'id':1, "name":"Dorothy", "kind":"dog"},
    {'id':2, "name":"Casey", "kind":"dog"},
    {'id':3, "name":"Flipper", "kind":"fish"},
    {'id':4, "name":"Cowabelle", "kind":"cow"}
]

@route("/pets")
def get_pets():
    return template("pets.tpl", pets=pets) 



run(host='localhost', port=8080)
