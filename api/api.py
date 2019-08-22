import models
from flask import Blueprint, request, jsonify
from playhouse.shortcuts import model_to_dict
import requests

api = Blueprint('api', 'api', url_prefix="/api/v1")
# app = Flask(__name__, template_folder='.')
        
@api.route('/', methods=['GET'])
def get_all_imgs():
  params = {
    'api_key': '{6979f6deb8674a6cb343a275b6196586}',
  }
  r = requests.get(
      'https://api.planet.com/basemaps/v1/mosaics',
      params=params)
  return render_template('movies.html', movies=json.loads(r.text)['movies'])
    except models.DoesNotExist:
        return jsonify(data={}, status={"code": 401, "message": " There was an error getting the resource"})