from flask import Flask, render_template, jsonify
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/birthday')
def birthday():
    return 'September 12 1981'

@app.route('/user/<name>')
def user_name(name):
    return 'Hello %s!' % name

@app.route('/add/<int:n1>/<int:n2>')
def add(n1,n2):
    result = n1+n2
    return str(result)

@app.route('/multiply/<int:n1>/<int:n2>')
def multiply(n1,n2):
    result = n1*n2
    return str(result)

@app.route('/substract/<int:n1>/<int:n2>')
def substract(n1,n2):
    result = n1-n2
    return str(result)

@app.route('/favoritefoods')
def favoritefoods():
    list = ['pizza', 'sushi', 'hamburgers']
    return jsonify(list)
