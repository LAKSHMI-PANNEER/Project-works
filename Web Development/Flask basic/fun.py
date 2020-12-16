from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello World!</h1>'

@app.route('/information')
def inform():
    return '<h1>WELCOME!</h1>'

@app.route('/information/<cno>')
def info(cno):
    return '<h1>This is {} class!</h1>'.format(cno)

@app.route('/cname')
def course_name():
    return 'OPEN SOURCE TECHNOLOGIES'

@app.route('/<name>')
def name(name):
    return "This is a page for {}!".format(name)

@app.route('/student/<name>')
def student(name):
    return "The student name is " + str(name)

if __name__ == '__main__':
    app.run()

