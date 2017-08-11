import re
from flask import Flask, render_template, request, session, redirect, flash
from datetime import datetime, date, time
app = Flask(__name__)
app.secret_key = 'keepitonlock'

@app.route('/')
def home():
    session.clear() # clear sessions to reset the form
    return render_template('index.html')


@app.route('/registration', methods=['POST'])
def register():

    errors = 0
    email_regex = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
    password_regex = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).+$')
    birthday = datetime.strptime(request.form['birthdate'], "%m/%d/%Y")


# First and Last Name cannot contain any numbers

    if any(char.isdigit() for char in request.form['firstname']) == True:
        flash("First name cannot contain a number")
        errors += 1
    elif len(request.form['firstname']) == '': # has no characters filled in
        flash("Please enter a first name")
        errors += 1
    else:
        session['firstname']=request.form['firstname']

    if any(char.isdigit() for char in request.form['lastname']) == True:
        flash("Last name cannot contain a number")
        errors += 1
    elif len(request.form['firstname']) == '':
        flash("Please enter a last name") # has no characters filled in
        errors += 1
    else:
        session['lastname']=request.form['lastname']

# Password should be more than 8 characters

    if len(request.form['password']) < 1: # has no characters filled in
        flash("Password must be at least 8 characters")
        errors += 1
    elif len(request.form['password']) < 8:
        errors += 1
        flash("Please enter a password")
    else:
        session['password']=request.form['password']

# Birthday must be in the past
    if request.form['birthdate'] == '':
        flash('Please enter a birthday')
        errors += 1
    elif datetime.now() > birthday:
        flash('Birthday must be in the past')
        errors += 1
    else:
        session['birthdate']=request.form['birthdate']

# Password and password confirmation should match

    if len(request.form['confirmpwd']) != len(request.form['password']):
        flash("Password does not match")
        errors += 1
    elif not password_regex.match(request.form['password']):
        flash("Password must contain at least one lowercase letter, one uppercase letter and one number")
    else:
        session['confirmpwd']=request.form['confirmpwd']


# Email should be a valid email

    if request.form['emailaddress'] == '':
        flash("Email cannot be blank")
        errors += 1
    elif not email_regex.match(request.form['emailaddress']):
        flash("Not a valid email address")
    else:
        session['emailaddress']=request.form['emailaddress']


    #See if there are any errors
    if errors > 0:
        return render_template('index.html')
    else:
        return render_template('registration.html')

app.run(debug=True)
