from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, PasswordField, SubmitField
from wtforms.validators import InputRequired, EqualTo, Length


app = Flask(__name__)

app.secret_key = 'jisungparkfromspace'

posts = [

    {
        "id": 1,
        "name": "James",
        "Due_date": "Monday"
    },

    {
        "id": 2,
        "name": "Paul",
        "Due_date": "Tuesday"
    },

    {
        "id": 3,
        "name": "Chris",
        "Due_date": "Wednesday"
    },

    {
        "id": 4,
        "name": "Jake",
        "Due_date": "Friday"
    },

]


class SignUpForm(FlaskForm):
    username = StringField(label="Username", validators= [InputRequired(message="Username should not be blank"), 
                Length(min = 5, max = 40, message="Username should be between 5 and 40 characters")])
    email = StringField(label="Email", validators=[InputRequired(message= "Email should not be blank"),
                Length(max=50, message="Email should have less than 50 characters")])
    password = PasswordField(label="Password", validators=[InputRequired(message="Password should not be left blank"),
                Length(min = 5, max=50, message="Password should be between 5 and 50 characters")])
    confirm_password = PasswordField(label="Confirm Password", validators=[InputRequired(message="Password should not be left blank"),
                        Length(min = 5, max=50, message="Password should be between 5 and 50 characters"), 
                        EqualTo('password', message= "Passwords do not match")])
    submit = SubmitField(label="Sign up")


class LoginForm(FlaskForm):
    email = StringField(label="Email", validators=[InputRequired(message= "Email should not be blank"),
                Length(max=50, message="Email should have less than 50 characters")])

    password = PasswordField(label="Password", validators=[InputRequired(message="Password should not be left blank"),
                Length(min = 5, max=50, message="Password should be between 5 and 50 characters")])

    submit = SubmitField(label="Login")
    
    


@app.route('/')
def index():
    title = "Home Page"
    context = {
        'title': title,
        'posts': posts
    }
    return render_template("index.html", **context)


@app.route('/about')
def about_page():
    title = "About Page"
    context = {
        'title': title
    }
    return render_template('about.html', **context)


@app.route('/login')
def login():
    title = "Login Page"
    form = LoginForm()
    context = {
        'title': title,
        'form': form
    }


    return render_template('login.html', **context)


@app.route('/contacts')
def contacts_page():
    title = "Contacts Page"
    context = {
        'title': title
    }
    return render_template('contacts.html', **context)

@app.route('/signup', methods = ["GET", "POST"])
def signup():
    form = SignUpForm()

    if request.method == "POST":
        if form.validate_on_submit():
            return "User signed up successfully"

    context = {
        'form': form
    }

    return render_template('signup.html', **context)



if __name__ == "__main__":
    app.run(debug = True)