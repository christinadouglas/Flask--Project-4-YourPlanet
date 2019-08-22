from flask import Blueprint, request, jsonify

api = Blueprint('api', 'api', url_prefix="https://api.planet.com/basemaps/v1/mosaics")