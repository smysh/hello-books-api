from app import db
from app.models.genre import Genre
from flask import Blueprint, jsonify, abort, make_response, request

genre_bp = Blueprint("genre_bp", __name__, url_prefix="/genres")