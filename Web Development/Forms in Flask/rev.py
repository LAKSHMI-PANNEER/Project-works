from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField

app = Flask(__name__,template_folder='templates')
app.config['SECRET_KEY'] = 'mysecretkey'

class InfoForm(FlaskForm):
    name = StringField('Enter a name:')
    submit = SubmitField('Reverse')

@app.route('/', methods=['GET', 'POST'])
def index():
    name = False
    form = InfoForm()
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
        reversedstring=''.join(reversed(name))
    return render_template('rever.html', **locals())

if __name__ == '__main__':
    app.run(debug=True)





