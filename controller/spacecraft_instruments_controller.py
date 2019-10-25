import codecs
from flask import Blueprint, request
from flask_cors import CORS

from service.apollo_service import apollo_service

spacecraft_instruments_controller = Blueprint('spacecraft_instruments_controller', __name__)

CORS(spacecraft_instruments_controller)


@spacecraft_instruments_controller.route('/api/spacecraft/<spacecraft_name>/<journey_id>/instruments/location',
                                         methods=['GET', 'POST'])
def location_reading_for_spacecraft_journey(spacecraft_name, journey_id):
    if request.method == 'POST':
        apollo_service.save_location_reading_for_spacecraft_journey(spacecraft_name, journey_id, request.get_json())
        return {'success': True}, 200

    if request.method == 'GET':
        result = apollo_service.get_location_readings_for_spacecraft_journey(spacecraft_name, journey_id,
                                                                             request.args.get('pagesize', 25),
                                                                             request.args.get('pagestate', None))

        resp = {'pageSize': request.args.get('pagesize', 25),
                'pageState': codecs.encode(result.paging_state, 'hex').decode('UTF-8') if result.paging_state else None,
                'data': result.current_rows}

        return resp, 200


@spacecraft_instruments_controller.route('/api/spacecraft/<spacecraft_name>/<journey_id>/instruments/pressure',
                                         methods=['GET', 'POST'])
def pressure_reading_for_spacecraft_journey(spacecraft_name, journey_id):
    if request.method == 'POST':
        apollo_service.save_pressure_reading_for_spacecraft_journey(spacecraft_name, journey_id, request.get_json())
        return {'success': True}, 200

    if request.method == 'GET':
        result = apollo_service.get_pressure_readings_for_spacecraft_journey(spacecraft_name, journey_id,
                                                                             request.args.get('pagesize', 25),
                                                                             request.args.get('pagestate', None))

        resp = {'pageSize': request.args.get('pagesize', 25),
                'pageState': codecs.encode(result.paging_state, 'hex').decode('UTF-8') if result.paging_state else None,
                'data': result.current_rows}

        return resp, 200


@spacecraft_instruments_controller.route('/api/spacecraft/<spacecraft_name>/<journey_id>/instruments/speed',
                                         methods=['GET', 'POST'])
def speed_reading_for_spacecraft_journey(spacecraft_name, journey_id):
    if request.method == 'POST':
        apollo_service.save_speed_reading_for_spacecraft_journey(spacecraft_name, journey_id, request.get_json())
        return {'success': True}, 200

    if request.method == 'GET':
        result = apollo_service.get_speed_readings_for_spacecraft_journey(spacecraft_name, journey_id,
                                                                          request.args.get('pagesize', 25),
                                                                          request.args.get('pagestate', None))

        resp = {'pageSize': request.args.get('pagesize', 25),
                'pageState': codecs.encode(result.paging_state, 'hex').decode('UTF-8') if result.paging_state else None,
                'data': result.current_rows}

        return resp, 200


@spacecraft_instruments_controller.route('/api/spacecraft/<spacecraft_name>/<journey_id>/instruments/temperature',
                                         methods=['GET', 'POST'])
def temperature_reading_for_spacecraft_journey(spacecraft_name, journey_id):
    if request.method == 'POST':
        apollo_service.save_temperature_reading_for_spacecraft_journey(spacecraft_name, journey_id, request.get_json())
        return {'success': True}, 200

    if request.method == 'GET':
        result = apollo_service.get_temperature_readings_for_spacecraft_journey(spacecraft_name, journey_id,
                                                                                request.args.get('pagesize', 25),
                                                                                request.args.get('pagestate', None))

        resp = {'pageSize': request.args.get('pagesize', 25),
                'pageState': codecs.encode(result.paging_state, 'hex').decode('UTF-8') if result.paging_state else None,
                'data': result.current_rows}

        return resp, 200




