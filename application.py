from flask import Flask
application = Flask(__name__)

@application.route('/')
def hello_world():
    return "<h1>NAUFIL SIR G.O.T.A</h1><p>Version 2.0: Second Page.</p>"

if __name__ == '__main__':
    application.run(debug=True)
