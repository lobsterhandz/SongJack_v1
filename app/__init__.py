from flask import Flask

# Task 1: Initialize Flask App
app = Flask(__name__)

# Task 2: Import Routes
from app.routes import *

# Task 3: Configuration
app.config['UPLOAD_FOLDER'] = 'songs/'  # Folder for storing local audio files
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # Limit file upload size to 16MB

# Task 4: Finalize Setup
if __name__ == '__main__':
    app.run(debug=True)
