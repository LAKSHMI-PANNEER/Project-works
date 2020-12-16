from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import SubmitField, IntegerField

app = Flask(__name__,template_folder='templates')

app.config['SECRET_KEY'] = 'mysecretkey'

class InfoForm(FlaskForm):

    n = IntegerField('Enter a number:')
    prime = SubmitField('Prime/Not')
    
@app.route('/', methods=['GET', 'POST'])

def index():
    form = InfoForm()
    if form.validate_on_submit():
        n = form.n.data
        
        for i in range(2,n):
            if (n % i) == 0:
                prime="Not Prime"
                break
        else:
            prime="Prime"

    return render_template('prime.html', **locals())

if __name__ == '__main__':
    app.run(debug=True)
