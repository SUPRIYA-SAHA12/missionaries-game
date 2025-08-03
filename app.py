from flask import Flask, render_template, request, redirect, session, url_for

app = Flask(__name__)
app.secret_key = 'secret_key_for_session'

@app.route('/')
def index():
    # Initialize game state if not already
    if 'missionaries_on_right' not in session:
        session['missionaries_on_right'] = 3
        session['cannibals_on_right'] = 3
        session['missionaries_on_left'] = 0
        session['cannibals_on_left'] = 0
        session['boat_side'] = "Right"
        session['message'] = ""

    return render_template('index.html',
                           missionaries_on_left=session['missionaries_on_left'],
                           cannibals_on_left=session['cannibals_on_left'],
                           missionaries_on_right=session['missionaries_on_right'],
                           cannibals_on_right=session['cannibals_on_right'],
                           boat_side=session['boat_side'],
                           message=session['message'])

@app.route('/move', methods=['POST'])
def move():
    missionaries = int(request.form['missionaries'])
    cannibals = int(request.form['cannibals'])

    missionaries_on_right = session['missionaries_on_right']
    cannibals_on_right = session['cannibals_on_right']
    missionaries_on_left = session['missionaries_on_left']
    cannibals_on_left = session['cannibals_on_left']
    boat_side = session['boat_side']

    if (missionaries + cannibals) != 1 and (missionaries + cannibals) != 2:
        session['message'] = 'Invalid move: Only 1 or 2 people can move'
        return redirect(url_for('index'))

    if boat_side == 'Right':
        if missionaries_on_right < missionaries or cannibals_on_right < cannibals:
            session['message'] = 'Invalid move: Not enough people on right side'
            return redirect(url_for('index'))

        missionaries_on_right -= missionaries
        cannibals_on_right -= cannibals
        missionaries_on_left += missionaries
        cannibals_on_left += cannibals
        boat_side = 'Left'

    else:
        if missionaries_on_left < missionaries or cannibals_on_left < cannibals:
            session['message'] = 'Invalid move: Not enough people on left side'
            return redirect(url_for('index'))

        missionaries_on_left -= missionaries
        cannibals_on_left -= cannibals
        missionaries_on_right += missionaries
        cannibals_on_right += cannibals
        boat_side = 'Right'

    # Check for losing condition
    if (missionaries_on_right > 0 and cannibals_on_right > missionaries_on_right) or \
       (missionaries_on_left > 0 and cannibals_on_left > missionaries_on_left):
        session.clear()
        session['message'] = "You lost!"
        return redirect(url_for('index'))

    # Check for winning condition
    if missionaries_on_left == 3 and cannibals_on_left == 3:
        session.clear()
        session['message'] = "You won!"
        return redirect(url_for('index'))

    # Update session variables
    session['missionaries_on_right'] = missionaries_on_right
    session['cannibals_on_right'] = cannibals_on_right
    session['missionaries_on_left'] = missionaries_on_left
    session['cannibals_on_left'] = cannibals_on_left
    session['boat_side'] = boat_side
    session['message'] = ""

    return redirect(url_for('index'))

@app.route('/reset')
def reset():
    session.clear()
    return redirect(url_for('index'))

if __name__=="__main__":
    app.run(debug=True)
