from app import app
from flask import render_template, session, redirect, url_for, request, jsonify
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

    return render_template('draft.html', players=optimized_players.sort_values(by='valueOverNextRound', ascending = False))



@app.route('/select_player', methods=['POST'])
def select_player():
    player_name = request.args.get('name')
    print(f"Selecting player: {player_name}")  # Debug print
    if player_name:
        # Add the player to the draftedOverall list
        drafted = session.get('draftedOverall', [])
        drafted.append(player_name)
        session['draftedOverall'] = drafted

    print(session['draftedOverall'])

    return "OK", 200


@app.route('/get_optimized_players', methods=['GET'])
def get_optimized_players():
    optimized_players = draft_optimize(session['yourTeam'], session['draftedOverall'])
    # Convert the DataFrame to a list of dictionaries for JSON serialization
    data = optimized_players.sort_values(by='valueOverNextRound', ascending=False).to_dict(orient='records')
    return jsonify(data)