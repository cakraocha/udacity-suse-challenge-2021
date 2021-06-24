from flask import Flask
from flask import json
import logging

app = Flask(__name__)

# Create a routing for the healthcheck in /status
@app.route("/status")
def healthcheck():
    response = app.response_class(
            response=json.dumps({"result":"OK - healthy"}),
            status=200,
            mimetype='application/json'
    )
    # Add log details
    app.logger.info('Status request success')

    return response

# Create a routing for metrics in /metrics
@app.route("/metrics")
def metrics():
    response = app.response_class(
            response=json.dumps({"status":"success",
                                "code":0,
                                "data":{"UserCount":140,
                                        "UserCountActive":23
                                        }
                                }
                                ),
            status=200,
            mimetype='application/json'
    )
    # Add log details
    app.logger.info('Metrics request success')

    return response

@app.route("/")
def hello():
    # Add log details
    app.logger.info('Main request success')
    return "Hello World!"

if __name__ == "__main__":
    # Stream logs into file
    logging.basicConfig(filename='app.log', level=logging.DEBUG)
    app.run(host='0.0.0.0')
