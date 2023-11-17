from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', title='Flask Book', message='Welcome to my Flask Book!')

if __name__ == '__main__':
    app.run(debug=True)
