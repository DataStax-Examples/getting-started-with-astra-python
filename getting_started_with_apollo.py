from flask import Flask

from controller.credentials_controller import credentials_controller
from controller.spacecraft_journey_controller import spacecraft_journey_controller
from controller.spacecraft_instruments_controller import spacecraft_instruments_controller

app = Flask(__name__)

app.register_blueprint(credentials_controller)
app.register_blueprint(spacecraft_journey_controller)
app.register_blueprint(spacecraft_instruments_controller)

if __name__ == '__main__':
    app.run()
