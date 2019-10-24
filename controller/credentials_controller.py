from flask import Blueprint, request

from service.apollo_service import apollo_service

credentials_controller = Blueprint('credentials_controller', __name__)


@credentials_controller.route("/api/credentials", methods=['GET', 'POST'])
def connect():
    if request.method == 'POST':
        apollo_service.save_credentials(request.args['username'], request.args['password'],
                                        request.args['keyspace'], request.args['file'])
        apollo_service.connect()

        return {'connected': True}, 200

    if request.method == 'GET':

        resp = {'success': apollo_service.check_connection()}

        if resp['success'] is True:
            status_code = 200
        else:
            status_code = 401

        return resp, status_code


@credentials_controller.route("/api/credentials/test", methods=['POST'])
def test_credentials():
    test_connection = apollo_service.test_credentials(request.args['username'], request.args['password'],
                                                      request.args['keyspace'], request.args['file'])

    resp = {'success': test_connection}

    if resp['success'] is True:
        status_code = 200
    else:
        status_code = 401

    return resp, status_code





