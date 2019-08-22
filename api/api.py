from flask import Blueprint, request, jsonify

api = Blueprint('api', 'api', url_prefix="https://api.planet.com/basemaps/v1/mosaics?api_key=6979f6deb8674a6cb343a275b6196586)