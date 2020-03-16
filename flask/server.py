import sys
sys.path.insert(0, '../sensehat_dashboard/pi')
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index() :
	return render_template('sensehat.html')

@app.route('/wrong')
def wrong() :
	return 'You are at the wrong page'

host = '192.168.0.196'
port = 8000

if __name__ == '__main__':
	app.run(host=host, port=port, debug=True)
