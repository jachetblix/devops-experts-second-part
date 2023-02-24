from flask import Flask, request, jsonify
from db_connector import DBConnector
from pypika import Query, Table, Field
from datetime import datetime
from model import users
import os
import signal

app = Flask(__name__)


def get_user(user_id):
    try:
        result = users.get_user(user_id)
    except Exception as e:
        return jsonify({'status': 'error', 'reason': str(e)}), 500
    if not result:
        return jsonify({'status': 'error', 'reason': 'no such id'}), 500
    return jsonify({'status': 'ok', 'user_name': result[0]}), 200


def create_user(user_id):
    data = request.json
    user_name = data.get('user_name')
    if not user_name:
        return jsonify({'status': 'error', 'reason': 'No username was specified'}), 500
    try:
        users.create_user(user_id, user_name)
    except Exception as e:
        if e.args[0] == 1062:
            return jsonify({'status': 'error', 'reason': 'id already exists'}), 500
        return jsonify({'status': 'error', 'reason': str(e)}), 500
    return jsonify({'status': 'ok'}), 200


def update_user(user_id):
    data = request.json
    user_name = data.get('user_name')
    if not user_name:
        return jsonify({'status': 'error', 'reason': 'username was not specified'})
    try:
        users.update_user(user_id, user_name)
    except Exception as e:
        return jsonify({'status': 'error', 'reason': str(e)}), 500
    return jsonify({'status': 'ok'}), 200


def delete_user(user_id):
    try:
        users.delete_user(user_id)
    except Exception as e:
        print(e)
        return jsonify({'status': 'error', 'reason': str(e)}), 500
    return jsonify({'status': 'ok'}), 200


user_rest_routes = {'POST': create_user, 'PUT': update_user, 'DELETE': delete_user, 'GET': get_user}


@app.route('/users/<user_id>', methods=['PUT', 'GET', 'POST', 'DELETE'])
def user_rest_route(user_id):
    return user_rest_routes[request.method](user_id)



@app.route('/stop_server')
def stop_server():
    os.kill(os.getpid(), signal.CTRL_C_EVENT)
    return 'Server stopped'


@app.errorhandler(404)
def resource_not_found(e):
    return jsonify(error=str(e)), 404

app.run(host='0.0.0.0', debug=True, port=5000)
