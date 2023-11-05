
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Welcome to the Food Security App'







# Debug mode for development
if __name__ == '__main__':
    app.run(debug=True) 
