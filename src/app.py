import os
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
target_metadata = db.metadata

db_url = os.getenv("DATABASE_URL")
if db_url is not None:
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url.replace("postgres://", "postgresql://")
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////tmp/test.db"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/user', methods=['GET'])
def handle_user():
    response_body = {
        "msg": "Hello, this is your GET /user response "
    }
    return jsonify(response_body), 200

@app.route('/follower', methods=['GET'])
def handle_follower():
    response_body = {
        "msg": "Hello, this is your GET /follower response "
    }
    return jsonify(response_body), 200

@app.route('/comment', methods=['GET'])
def handle_comment():
    response_body = {
        "msg": "Hello, this is your GET /comment response "
    }
    return jsonify(response_body), 200

@app.route('/post', methods=['GET'])
def handle_post():
    response_body = {
        "msg": "Hello, this is your GET /post response "
    }
    return jsonify(response_body), 200

@app.route('/media', methods=['GET'])
def handle_media():
    response_body = {
        "msg": "Hello, this is your GET /media response "
    }
    return jsonify(response_body), 200

# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
