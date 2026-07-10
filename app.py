from flask import Flask

# Create a Flask application instance
app = Flask(__name__)

# root routing 
@app.route('/')
def home():
	return  "Hello World"

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000, debug=True)
