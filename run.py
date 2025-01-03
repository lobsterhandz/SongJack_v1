# run.py - Entry Point for Flask App

from app import app

# Task 1: Start Flask Application
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
