import random
from flask import Flask, render_template, request, session, redirect
app = Flask(__name__)
app.secret_key = 'keepitonlock'

@app.route('/')
def home():
    if 'total' not in session:
        session['total'] = 0
    if 'activity' not in session:
        session['activity'] = None


    return render_template('index.html', total=session['total'], activities=session['activity'])


@app.route('/process_money', methods=['POST'])
def calculate_gold():

    hidden_input = request.form['hidden']

    if hidden_input == 'farm':
        farm = random.randrange(10, 21)
        session['total'] += farm
    elif hidden_input == 'cave':
        cave = random.randrange(5, 11)
        session['total'] += cave
    elif hidden_input == 'house':
        house = random.randrange(2, 6)
        session['total'] += cave
    elif hidden_input == 'cave':
        casino = random.randrange(0, 50)
        chance = random.randrange(1,2)
        if chance == 1:
            return 'earn'
            session['total'] += casino
        else:
            return 'lose'
            session['total'] -= casino

    return render_template('process_money.html')
    # return redirect('/')

app.run(debug=True)
