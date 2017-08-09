import random, datetime
from flask import Flask, render_template, request, session, redirect
app = Flask(__name__)
app.secret_key = 'keepitonlock'

@app.route('/')
def home():
    session.clear() # clear sessions to reset the game
    return render_template('index.html')


@app.route('/process_money', methods=['POST'])
def calculate_gold():
    earned = 0
    msg = ''
    timestamp =  datetime.datetime.now().strftime("%Y/%m/%d %I:%M %p")
    if request.form['building'] == 'farm':
        earned = random.randint(10,21)
        msg += 'Earned {} golds from the farm! {}'.format(earned,timestamp)
    elif request.form['building'] == 'cave':
        earned = random.randint(5,11)
        msg += 'Earned {} golds from the cave! {}'.format(earned,timestamp)
    elif request.form['building'] == 'house':
        earned = random.randint(2,6)
        msg += 'Earned {} golds from the house! {}'.format(earned,timestamp)
    elif request.form['building'] == 'casino':
        earned = random.randint(0,51)
        if earned <= 1:
            msg += 'Entered a casino and lost {} golds...Ouch! {}'.format(earned,timestamp)
        else:
            msg += 'Entered a casino and took {} golds...Feel lucky! {}'.format(earned,timestamp)

    try:
        # update gold balance by earned amount
        session['gold'] += earned
    except KeyError:  # there was no gold balance found, so start it
        session['gold'] = earned

    try:
        # update activity textarea by concatenating msg
        session['activity'] += msg + '\n'
    except KeyError:
        session['activity'] = msg + '\n'

    return render_template('index.html', gold=session['gold'], activities=session['activity'])

app.run(debug=True)
