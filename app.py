from flask import Flask

# Initialize the Flask application
# We tell Flask to look for our HTML/CSS/JS files in the current folder ('.')
app = Flask(__name__, static_url_path='', static_folder='.')

# Create the main route for your game
@app.route('/')
def home():
    # This sends your existing index.html to the user's browser
    return app.send_static_file('index.html')

# This starts the server
if __name__ == '__main__':
    # Render assigns a specific port, so we bind to 0.0.0.0 to make it accessible
    app.run(host='0.0.0.0', port=10000)
