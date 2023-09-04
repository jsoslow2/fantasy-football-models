from flask import Flask
import os

# Import routes at the bottom to avoid circular imports
app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'fallback_key')

from app import routes