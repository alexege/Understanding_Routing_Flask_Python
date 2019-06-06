from flask import Flask  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return 'Hello World!'
@app.route('/dojo')
def success():
    return "Dojo"
@app.route('/say/<name>') 
def hello(name):
    print(name)
    return "Hi " + name + "!"
@app.route('/repeat/<integer>/<strng>')
def repeat_message(integer, strng):
    return int(integer) * strng + "\n"
if __name__=="__main__":
    app.run(debug=True)