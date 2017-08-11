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
# All fields are required and must not be blank
    # if len(request.form['firstname']) < 1:
    #     flash("First name cannot be left blank")
    # elif len(request.form['lastname']) < 1:
    #     flash("Last name cannot be left blank")
    # elif len(request.form['email']) < 1:
    #     flash("Email cannot be left blank")
    # elif len(request.form['password']) < 1:
    #     flash("Password cannot be left blank")
    # elif len(request.form['confirmpwd']) < 1:
    #     flash("Please confirm your password")
    # else:
    #     # return render_template('index.html', firstname=session['firstname'], lastname=session['lastname'], email=session['email'], password=session['password'], confirmpwd=session['confirmpwd'])
    #     return render_template('registration.html', form_data=request.form)

    # return redirect('/')

# First and Last Name cannot contain any numbers

    if len(request.form['firstname']) != 0: # defines a string
        flash("First name cannot contain a number")
    elif len(request.form['firstname']) < 1: # has no characters filled in
        flash("Please enter a first name")
    else:
        return render_template('registration.html', firstname=session['firstname'])

    if len(request.form['lastname']) != 0: # defines a string
        flash("Last name cannot contain a number")
    elif len(request.form['firstname']) < 1:
        flash("Please enter a last name") # has no characters filled in
    else:
        return render_template('registration.html', lastname=session['lastname'])

# Password should be more than 8 characters

    if len(request.form['password']) > 8:
        flash("Password exceeds 8 characters")
    else:
        return render_template('registration.html', password=session['password'])

# Password and password confirmation should match

    if len(request.form['confirmpwd']) != len(request.form['password']):
        flash("Password does not match")
    else:
        return render_template('registration.html', password=session['password'])


# Email should be a valid email

email = request.form['email']

def isValidEmail(email):
	if len(email) > 7:
		if re.match(request.form['email'], email) != None:
			return True
        else:
    	       return False
               flash("Email address is not valid")

if isValidEmail(email) == True :
    print ("This is a valid email address")
else:
	print ("This is not a valid email address")



app.run(debug=True)
