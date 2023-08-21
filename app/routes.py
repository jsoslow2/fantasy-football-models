from app import app
from flask import render_template, session, redirect, url_for
from draft_optimizer import draft_optimize

@app.route('/')
@app.route('/draft', methods=['GET', 'POST'])
def draft():
    # Ensure the session variables exist
    if 'yourTeam' not in session:
        session['yourTeam'] = []
    if 'draftedOverall' not in session:
        session['draftedOverall'] = []
        
    # Call the optimizer
    optimized_players = draft_optimize(session['yourTeam'], session['draftedOverall'])
    
    return render_template('draft.html', players=optimized_players)




@app.route('/pick_player/<player_name>', methods=['POST'])
def pick_player(player_name):
    yourTeam = session.get('yourTeam', [])
    yourTeam.append(player_name)
    session['yourTeam'] = yourTeam
    return redirect(url_for('draft'))

# Additional routes to handle other user actions like drafting players by others can be added similarly.