from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import SubmitField, IntegerField

app = Flask(__name__,template_folder='templates')

app.config['SECRET_KEY'] = 'mysecretkey'

class InfoForm(FlaskForm):

    n = IntegerField('Enter a number:')
    m=SubmitField('Odd/Even')
    
@app.route('/', methods=['GET', 'POST'])

def index():
    form = InfoForm()
    if form.validate_on_submit():
        n = form.n.data
        
        m = n % 2
        if m > 0:
            m="odd"
        else:
            m="even"
            
    return render_template('odd.html', **locals())

if __name__ == '__main__':
    app.run(debug=True)
