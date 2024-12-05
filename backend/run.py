"""
Main entry point for the Flask application.
This script creates and runs the Flask application using the factory pattern.
"""

from app import create_app

# Create Flask application instance
app = create_app()

if __name__ == '__main__':
    # Run the application in debug mode when executed directly
    # Debug mode enables:
    # - Automatic reloading when code changes
    # - Detailed error pages
    # - Debug console in browser
    app.run(debug=True)
