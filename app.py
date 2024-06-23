from flask import Flask

# Create a Flask application instance
app = Flask(__name__)

# Define a route and a view function
@app.route('/')
def hello():
    return 'Hello, World!'

# Run the application if executed directly
if __name__ == '__main__':
    app.run(debug=True)
