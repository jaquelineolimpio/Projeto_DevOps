from flask import Flask, request, jsonify
from app.models import User, SessionLocal

app = Flask(__name__)

@app.route("/users", methods=["GET"])
def get_users():
    session = SessionLocal()
    users = session.query(User).all()
    session.close()
    return jsonify([{"id": u.id, "name": u.name, "email": u.email} for u in users])

@app.route("/users", methods=["POST"])
def create_user():
    data = request.json
    session = SessionLocal()
    new_user = User(name=data["name"], email=data["email"])
    session.add(new_user)
    session.commit()
    session.close()
    return jsonify({"message": "Usuário criado!"}), 201
