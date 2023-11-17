from app import app

# Define a route for the homepage
@app.route('/')
def index():
    return "Hello, Flask! This is the homepage."
