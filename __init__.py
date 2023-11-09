import os
from flask import Flask, render_template, request, jsonify

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
        return render_template('home.html')
    
    # route to tracking page
    @app.route('/tracking')
    def tracking():
        return render_template('tracking.html', sensors=sensors)

    # Endpoint to create a new tracking entry
    @app.route('/addTrackingEntry', methods=["POST"])
    def add_TrackingEntry():
        index = request.json['index']
        sensors[int(index)]['tracking'].append({
            "name": request.json['name'],
            "date": request.json['date'],
            "description": request.json['message']
            })

        return "Entry added."

    return app

sensors = [
    {
        'sensor_id': '402981394',
        'name': 'Sensor A',
        'description': 'Acceleration sensor',
        'tracking': [ {'name': 'Murat', 'date': "11.11.2023", 'description': "Testlauf"}, {'name': 'Viktor', 'date': "15.11.2023", 'description': "Testlauf1"} ]
    },
    {
        'sensor_id': '567923252',
        'name': 'Sensor B',
        'description': 'Torque sensor',
        'tracking': [ {'name': 'Murat', 'date': "11.11.2023", 'description': "Testlauf"}, {'name': 'Daniel', 'date': "15.11.2023", 'description': "Testlauf1"} ]
    },
    {
        'sensor_id': '686992967',
        'name': 'Sensor C',
        'description': 'Speed sensor',
        'tracking': [ {'name': 'Benedict', 'date': "11.11.2023", 'description': "Testlauf3"}, {'name': 'Murat', 'date': "11.11.2023", 'description': "Testlauf"}, {'name': 'Thomas', 'date': "15.11.2023", 'description': "Testlauf1"} ]
    },
        {
        'sensor_id': '757848050',
        'name': 'Sensor D',
        'description': 'Speed sensor',
        'tracking': [ {'name': 'Benedict', 'date': "11.11.2023", 'description': "Testlauf3"}, {'name': 'Murat', 'date': "11.11.2023", 'description': "Testlauf"}, {'name': 'Thomas', 'date': "15.11.2023", 'description': "Testlauf1"} ]
    },
        {
        'sensor_id': '574057074',
        'name': 'Sensor E',
        'description': 'Acceleration sensor',
        'tracking': [ {'name': 'Benedict', 'date': "11.11.2023", 'description': "Testlauf3"}, {'name': 'Murat', 'date': "11.11.2023", 'description': "Testlauf"}, {'name': 'Thomas', 'date': "15.11.2023", 'description': "Testlauf1"} ]
    },
        {
        'sensor_id': '847526847',
        'name': 'Sensor F',
        'description': 'Speed sensor',
        'tracking': [ {'name': 'Benedict', 'date': "11.11.2023", 'description': "Testlauf3"}, {'name': 'Murat', 'date': "11.11.2023", 'description': "Testlauf"}, {'name': 'Thomas', 'date': "15.11.2023", 'description': "Testlauf1"} ]
    },
        {
        'sensor_id': '378490481',
        'name': 'Sensor G',
        'description': 'Torque sensor',
        'tracking': [ {'name': 'Benedict', 'date': "11.11.2023", 'description': "Testlauf3"}, {'name': 'Murat', 'date': "11.11.2023", 'description': "Testlauf"}, {'name': 'Thomas', 'date': "15.11.2023", 'description': "Testlauf1"} ]
    },
        {
        'sensor_id': '448170495',
        'name': 'Sensor H',
        'description': 'Speed sensor',
        'tracking': [ {'name': 'Benedict', 'date': "11.11.2023", 'description': "Testlauf3"}, {'name': 'Murat', 'date': "11.11.2023", 'description': "Testlauf"}, {'name': 'Thomas', 'date': "15.11.2023", 'description': "Testlauf1"} ]
    },
        {
        'sensor_id': '099107012',
        'name': 'Sensor I',
        'description': 'Torque sensor',
        'tracking': [ {'name': 'Benedict', 'date': "11.11.2023", 'description': "Testlauf3"}, {'name': 'Murat', 'date': "11.11.2023", 'description': "Testlauf"}, {'name': 'Thomas', 'date': "15.11.2023", 'description': "Testlauf1"} ]
    },
        {
        'sensor_id': '298847391',
        'name': 'Sensor J',
        'description': 'Torque sensor',
        'tracking': [ {'name': 'Benedict', 'date': "11.11.2023", 'description': "Testlauf3"}, {'name': 'Murat', 'date': "11.11.2023", 'description': "Testlauf"}, {'name': 'Thomas', 'date': "15.11.2023", 'description': "Testlauf1"} ]
    },
    {
        'sensor_id': '634087203',
        'name': 'Sensor K',
        'description': 'Acceleration sensor',
        'tracking': [ {'name': 'Benedict', 'date': "11.11.2023", 'description': "Testlauf3"}, {'name': 'Murat', 'date': "11.11.2023", 'description': "Testlauf"}, {'name': 'Thomas', 'date': "15.11.2023", 'description': "Testlauf1"} ]
    },
]