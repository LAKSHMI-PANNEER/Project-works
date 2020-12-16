from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import SubmitField, IntegerField

app = Flask(__name__,template_folder='templates')

app.config['SECRET_KEY'] = 'mysecretkey'

class InfoForm(FlaskForm):

    n = IntegerField('Enter a number:')
    factorial = SubmitField('Factorial')
    
@app.route('/', methods=['GET', 'POST'])

def index():
    form = InfoForm()
    if form.validate_on_submit():
        n = form.n.data
        
        fact = 1
        for i in range(1,n+1):
            fact = fact*i

    return render_template('factorial.html', **locals())

if __name__ == '__main__':
    app.run(debug=True)
