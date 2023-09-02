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
    if 'ppr' not in session:
        session['ppr'] = 1
    if 'teams' not in session:
        session['teams'] = 10
        
    # Call the optimizer
    optimized_players = draft_optimize(session['yourTeam'], session['draftedOverall'], session['ppr'], session['teams'])

    return render_template('draft.html', players=optimized_players.sort_values(by='valueOverNextRound', ascending = False), teams = session['teams'])



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


#run every time a player OPTIMIZES
@app.route('/get_optimized_players', methods=['GET'])
def get_optimized_players():
    optimized_players = draft_optimize(session['yourTeam'], session['draftedOverall'], session['ppr'], session['teams'])
    # Convert the DataFrame to a list of dictionaries for JSON serialization
    data = optimized_players.sort_values(by='valueOverNextRound', ascending=False).to_dict(orient='records')

    print(session['ppr'])
    print(session['teams'])
    return jsonify(data)


@app.route('/add_to_your_team', methods=['POST'])
def add_to_your_team():
    player_name = request.args.get('name')
    print(f"Adding player to Your Team: {player_name}")  # Debug print
    if player_name:
        # Add the player to the yourTeam list
        session['yourTeam'].append(player_name)

    print(session['yourTeam'])

    return "OK", 200



#run to clear the session
@app.route('/reset_session', methods=['POST'])
def reset_session():
    session.clear()
    return jsonify(status="success")


@app.route('/save_settings', methods=['POST'])
def save_settings():
    data = request.get_json()
    ppr = data.get('ppr', 1)  # default to 1 if not provided
    teams = int(data.get('teams', 10))  # default to 10 if not provided

    session['ppr'] = ppr
    session['teams'] = teams
    return jsonify(success=True)


@app.route('/revert_player', methods=['POST'])
def revert_player():
    player_name = request.args.get('name')
    print(f"Reverting player: {player_name}")  # Debug print
    if player_name:
        # Remove the player from the draftedOverall list
        drafted = session.get('draftedOverall', [])
        if player_name in drafted:
            drafted.remove(player_name)
        session['draftedOverall'] = drafted

    print(session['draftedOverall'])

    return "OK", 200