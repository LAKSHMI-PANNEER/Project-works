from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import SubmitField, IntegerField

app = Flask(__name__,template_folder='templates')

app.config['SECRET_KEY'] = 'mysecretkey'

class InfoForm(FlaskForm):

    n = IntegerField('Enter a number:')
    sum = SubmitField('Sum')
    
@app.route('/', methods=['GET', 'POST'])

def index():
    form = InfoForm()
    if form.validate_on_submit():
        n = form.n.data
        
        sum=0
        for n in range(0,n+1):
            sum=sum+n

    return render_template('sum.html', **locals())

if __name__ == '__main__':
    app.run(debug=True)
