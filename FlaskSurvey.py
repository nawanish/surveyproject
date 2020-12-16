from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = '9e987ce989c729ba1a0c69b7cbcfce97'

posts = [
    {
        'author': 'Nawanish',
        'title': 'Peaky Blinders',
        'content': 'First post content'
    },
    {
        'author': 'Nawanish',
        'title': 'Peaky Blinders 2',
        'content': 'First post content'
    }
]

@app.route("/")
@app.route("/home")         #homepage route
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")        #aboutpage route
def about():
    return render_template('about.html', title='About')

@app.route("/register", methods=['GET', 'POST'])        #registration route
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('/home)'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login")           #loginpage route
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)


if __name__== '__main__':    #condition true if we run the script directly
    app.run(debug=True)