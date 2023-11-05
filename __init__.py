import os
from flask import Flask, render_template


sensors = [
    {
        'sensor_id': '1',
        'name': 'Sensor A',
        'description': 'Acceleration sensor'
    },
    {
        'sensor_id': '2',
        'name': 'Sensor B',
        'description': 'Torque sensor'
    },
    {
        'sensor_id': '3',
        'name': 'Sensor C',
        'description': 'Speed sensor'
    },
]


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY='dev',
        #DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # route to homepage
    @app.route('/')
    def home():
        return render_template('home.html', sensors=sensors)
    
    # route to tracking page
    @app.route('/tracking')
    def tracking():
        return render_template('tracking.html')

    return app