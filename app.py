from flask import Flask

# Create an instance of the Flask class
app = Flask(__name__)

# Define a route for the home page
@app.route('/')
def home():
    return "Hello, AWS DevOps from Python!"

# Run the application
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
