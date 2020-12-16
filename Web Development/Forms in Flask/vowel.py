from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField

app = Flask(__name__,template_folder='templates')
app.config['SECRET_KEY'] = 'mysecretkey'

class InfoForm(FlaskForm):
    name = StringField('Enter a name:')
    submit = SubmitField('Count_Vowel')

@app.route('/', methods=['GET', 'POST'])
def index():
    name = False
    count = 0
    form = InfoForm()
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
        for i in name:
            if i=="a" or i=="e" or i=="o" or i == "u" or i == "i":
                count = count+1
    return render_template('vow.html', **locals())

if __name__ == '__main__':
    app.run(debug=True)





