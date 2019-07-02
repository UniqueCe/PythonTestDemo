from flask import Flask
# from flask_salalchemy import SQLAlchemy

app = Flask(__name__)
# app.config['']
# db = SQLAlchemy(app)

@app.route('/')
def hello_world():
    return 'Hellow World Debug'

if __name__ == '__main__':
    app.run()
