"""
Authentication routes module handling user registration, login, and profile access.
Implements secure user authentication using JWT tokens and provides API endpoints
for user management.
"""

from flask import Blueprint, request, jsonify
from app.models.user import User
from app import db
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity

# Create a Blueprint for authentication routes
auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/api/register', methods=['POST'])
def register():
    """
    Handle user registration.
    
    Expects JSON payload with:
        - name: user's full name
        - email: user's email address
        - password: user's chosen password
    
    Returns:
        JSON response with:
        - Success: user data and access token
        - Error: error message and appropriate status code
    """
    data = request.get_json()
    
    # Validate required fields in request
    if not all(k in data for k in ['name', 'email', 'password']):
        return jsonify({'error': 'Missing required fields'}), 400
    
    # Check for existing user with same email
    if User.query.filter_by(email=data['email']).first():
        return jsonify({'error': 'Email already registered'}), 409
    
    # Create and save new user
    user = User(name=data['name'], email=data['email'])
    user.set_password(data['password'])
    
    db.session.add(user)
    db.session.commit()
    
    # Generate access token for immediate login
    access_token = create_access_token(identity=user.id)
    
    return jsonify({
        'message': 'Registration successful',
        'access_token': access_token,
        'user': user.to_dict()
    }), 201

@auth_bp.route('/api/login', methods=['POST'])
def login():
    """
    Handle user login.
    
    Expects JSON payload with:
        - email: user's email
        - password: user's password
    
    Returns:
        JSON response with:
        - Success: access token and user data
        - Error: error message with 401 status
    """
    data = request.get_json()
    
    # Validate login credentials presence
    if not all(k in data for k in ['email', 'password']):
        return jsonify({'error': 'Missing email or password'}), 400
    
    # Find and verify user
    user = User.query.filter_by(email=data['email']).first()
    
    if user and user.check_password(data['password']):
        # Generate access token on successful authentication
        access_token = create_access_token(identity=user.id)
        return jsonify({
            'access_token': access_token,
            'user': user.to_dict()
        })
    
    return jsonify({'error': 'Invalid email or password'}), 401

@auth_bp.route('/api/user', methods=['GET'])
@jwt_required()  # Requires valid JWT token
def get_user():
    """
    Retrieve current user's profile data.
    Requires valid JWT token in Authorization header.
    
    Returns:
        JSON response with:
        - Success: user profile data
        - Error: error message if user not found
    """
    current_user_id = get_jwt_identity()
    user = User.query.get(current_user_id)
    
    if not user:
        return jsonify({'error': 'User not found'}), 404
    
    return jsonify(user.to_dict())
