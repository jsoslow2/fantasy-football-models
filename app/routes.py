from app import app
from flask import render_template


@app.route('/')
@app.route('/draft')
def draft():
    # Mock data for demonstration. Replace this with your actual data.
    players = [
        {"name": "Player 1", "position": "RB", "predicted_points": 120},
        {"name": "Player 2", "position": "WR", "predicted_points": 100},
        # ... add more players as needed
    ]

    return render_template('draft_template.html', players=players)
