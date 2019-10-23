from flask import Blueprint, request, jsonify
from cassandra.util import min_uuid_from_time
from datetime import datetime, timedelta
from service.apollo_service import apollo_service

spacecraft_journey_controller = Blueprint('spacecraft_journey_controller', __name__)


@spacecraft_journey_controller.route('/api/spacecrafts')
def get_all_journeys():
    return apollo_service.get_all_spacecraft_journeys()


@spacecraft_journey_controller.route('/api/spacecrafts/<spacecraft_name>', methods=['GET', 'POST'])
def journeys_for_spacecraft(spacecraft_name):
    if request.method == 'POST':
        now = datetime.utcnow()
        journey_id = min_uuid_from_time(now)
        start = now
        end = now + timedelta(seconds=1000)
        active = True
        summary = request.get_data(as_text=True)

        apollo_service.create_new_journey_for_spacecraft(spacecraft_name, journey_id, start, end, active, summary)

        return jsonify({'journey_id': journey_id}), 200

    if request.method == 'GET':
        result = apollo_service.get_all_journeys_for_spacecraft(spacecraft_name)

        return jsonify(result.current_rows), 200




