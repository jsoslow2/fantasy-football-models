from app import app
from flask import render_template, session, redirect, url_for
from draft_optimizer import draft_optimize

@app.route('/')
@app.route('/draft', methods=['GET', 'POST'])
def draft():
    # Retrieve session data
    draftedOverall = session.get('draftedOverall', [])
    yourTeam = session.get('yourTeam', [])

    # Call your draft_optimize function
    players_df = draft_optimize(yourTeam=yourTeam, draftedOverall=draftedOverall)
    
    # Convert DataFrame to list of dictionaries for rendering in template
    players = players_df.to_dict(orient='records')

    players = [
        {"name": "Player 1", "position": "RB", "predicted_points": 120},
        {"name": "Player 2", "position": "WR", "predicted_points": 100},
        # ... add more players as needed
    ]

    return render_template('draft.html', players=players)

@app.route('/pick_player/<player_name>', methods=['POST'])
def pick_player(player_name):
    yourTeam = session.get('yourTeam', [])
    yourTeam.append(player_name)
    session['yourTeam'] = yourTeam
    return redirect(url_for('draft'))

# Additional routes to handle other user actions like drafting players by others can be added similarly.