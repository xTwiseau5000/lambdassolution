from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def start():
    return render_template('home.html')


@app.route('/2')
def hello_world():
    return 'hello world'

@app.route('/birthday')
def birfday():
    return 'October 30 1911'

@app.route('/greeting/<name>')
def saying_hi(name):
    return 'hello, %s' % name

#xtra Credit
@app.route('/add/<int:p>/<int:o>')
def add(p, o):
    x = p + o
    return str(x)

@app.route('/multiply/<int:p>/<int:o>')
def multiply(p, o):
    x = p * o
    return str(x)

@app.route('/subtract/<int:p>/<int:o>')
def subtract(p, o):
    x = p - o
    return str(x)

@app.route('/favoritefoods')
def favoritefoods():
    favoritefoodlist = ['Chicken', 'BLT', 'Cereal']
    return jsonify(favoritefoodlist)

'''
this was the lesson
@app.route('/about')
def index():
    return app.send_static_file('about.html')

@app.route('/killer')
def killer():
    return app.send_static_file('killer.html')

@app.route('/contact')
def contact():
    return app.send_static_file('contact.html')'''
