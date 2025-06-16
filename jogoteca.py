from flask import Flask

app = Flask(__name__)

@app.route('/inicio')
def index():
    return '<h2>Olá Mundo!</h2>'
app.run()