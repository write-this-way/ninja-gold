import re
from flask import Flask, render_template, request, session, redirect, flash
app = Flask(__name__)
app.secret_key = 'keepitonlock'

@app.route('/')
def home():
    session.clear() # clear sessions to reset the form
    return render_template('index.html')


@app.route('/registration', methods=['POST'])

def register():

# First and Last Name cannot contain any numbers

    if len(request.form['firstname']) != 0: # defines a string
        flash("First name cannot contain a number")
    elif len(request.form['firstname']) < 1: # has no characters filled in
        flash("Please enter a first name")
    else:
        return render_template('registration.html', firstname=session['firstname'], form_data=request.form)

    if len(request.form['lastname']) != 0: # defines a string
        flash("Last name cannot contain a number")
    elif len(request.form['firstname']) < 1:
        flash("Please enter a last name") # has no characters filled in
    else:
        return render_template('registration.html', lastname=session['lastname'], form_data=request.form)

# Password should be more than 8 characters

    if len(request.form['password']) < 1: # has no characters filled in
        flash("Password exceeds 8 characters")
    elif len(request.form['password']) < 8:
        flash("Please enter a password")
    else:
        return render_template('registration.html', password=session['password'], form_data=request.form)

# Password and password confirmation should match

    if len(request.form['confirmpwd']) != len(request.form['password']):
        flash("Password does not match")
    else:
        return render_template('registration.html', confirmpwd=session['confirmpwd'], form_data=request.form)


# Email should be a valid email

    email = request.form['emailaddress']

    # def isValidEmail(email):
    if re.match(email) == None:
		flash("Email address is not valid")
    else:
        return render_template('registration.html', emailaddress=session['emailaddress'], form_data=request.form)



app.run(debug=True)
