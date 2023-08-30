from bottle import route, run, template

# @route('/hello/<name>')
# def index(name):
#     return template('<b>Hello {{name}}</b>!', name=name)

@route("/")
def get_index():
    return template("<b>Hello, there {{name}}!!!</b>", name="index")

pets = [
    {'id':1, "name":"Dorothy", "kind":"dog"},
    {'id':2, "name":"Casey", "kind":"dog"},
    {'id':3, "name":"Flipper", "kind":"fish"},
    {'id':4, "name":"Cowabelle", "kind":"cow"}
]

@route("/hello/<name>")
def get_hello(name):
    return template("hello.tpl", name=name)

@route("/pets")
def get_hello():
    return template("pets.tpl", pets=pets)

run(host='localhost', port=8080)