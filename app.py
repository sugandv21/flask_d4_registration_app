from flask import Flask, render_template, flash
from forms import RegistrationForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here' 

@app.route('/')
def home():
    return render_template('layout/home.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f"Welcome, {form.full_name.data}!", "success")
    return render_template('layout/register.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
