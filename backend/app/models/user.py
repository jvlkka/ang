"""
User model module that defines the database structure and methods for user management.
Handles user data storage, password hashing, and data serialization.
"""

from app import db
from datetime import datetime
import bcrypt

class User(db.Model):
    """
    User model class representing the users table in the database.
    
    Attributes:
        id (int): Primary key for user identification
        name (str): User's full name
        email (str): User's email address (unique)
        password_hash (str): Hashed version of user's password
        created_at (datetime): Timestamp of account creation
    """
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)  # User's name cannot be empty
    email = db.Column(db.String(120), unique=True, nullable=False)  # Unique email required
    password_hash = db.Column(db.String(128), nullable=False)  # Store hashed password
    created_at = db.Column(db.DateTime, default=datetime.utcnow)  # Automatically set creation time
    
    def set_password(self, password):
        """
        Hash and set the user's password using bcrypt.
        
        Args:
            password (str): Plain text password to be hashed
        """
        salt = bcrypt.gensalt()  # Generate a random salt
        self.password_hash = bcrypt.hashpw(password.encode('utf-8'), salt)
    
    def check_password(self, password):
        """
        Verify if the provided password matches the stored hash.
        
        Args:
            password (str): Plain text password to check
            
        Returns:
            bool: True if password matches, False otherwise
        """
        return bcrypt.checkpw(password.encode('utf-8'), self.password_hash)
    
    def to_dict(self):
        """
        Convert user object to dictionary for API responses.
        Excludes sensitive information like password_hash.
        
        Returns:
            dict: User data in dictionary format
        """
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'created_at': self.created_at.isoformat()
        }
