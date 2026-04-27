from flask import Blueprint, jsonify
from db import create_user,get_user_by_username
auth_bp = Blueprint("auth",__name__)

@auth_bp.route("/test")
def test():
    return jsonify({"message":"Auth route working "})

@auth_bp.route("/create")
def create():
    create_user("deva","deva","user")
    return jsonify({"message":"success"})

@auth_bp.route("/fetch")
def fetch():
    user = get_user_by_username("deva")
    return jsonify({"message":"success","user":user})

    