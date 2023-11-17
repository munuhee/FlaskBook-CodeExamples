from flask import Flask

# Create a Flask app
app = Flask(__name__)

# Importing routes after app initialization
from app import routes
