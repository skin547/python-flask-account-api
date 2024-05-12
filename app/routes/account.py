from flask import request, jsonify
from app import db, bcrypt
from app.models import Account
from app.routes import account_bp
from app.utils import validate_password

@account_bp.route('/create', methods=['POST'])
def create_account():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    if not (username and password):
        return jsonify(success=False, reason="Missing username or password"), 400

    if not (3 <= len(username) <= 32):
        return jsonify(success=False, reason="Invalid username length"), 400

    if not validate_password(password):
        return jsonify(success=False, reason="Invalid password"), 400

    if Account.query.filter_by(username=username).first():
        return jsonify(success=False, reason="Username already exists"), 400

    hashed_pw = bcrypt.generate_password_hash(password).decode('utf-8')
    new_account = Account(username=username, password_hash=hashed_pw)
    db.session.add(new_account)
    db.session.commit()

    return jsonify(success=True), 201

@account_bp.route('/verify', methods=['POST'])
def verify_account():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    account = Account.query.filter_by(username=username).first()

    if not account or not bcrypt.check_password_hash(account.password_hash, password):
        return jsonify(success=False, reason="Invalid credentials"), 401

    return jsonify(success=True), 200
