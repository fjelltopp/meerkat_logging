"""
meerkat_logging

Api for gathering event logs

"""
from flask import Flask, abort, request
import datetime
import time
from dateutil.parser import parse
import uuid
from model import Log
from flask_sqlalchemy import SQLAlchemy

# Create the Flask app

app = Flask(__name__)
app.config['DEBUG'] = True
db = SQLAlchemy(app)
app.secret_key = uuid.uuid4()

@app.route("/", methods=['GET'])
def root():
    return "Meerkat Logging"


@app.route("/event", methods=['POST'])
def add_event():
    t = time.time()
    post_data = request.get_json()
    log_entry = input_to_log(post_data)
    print(time.time() - t)
    print(log_entry)
    return "OK"


def input_to_log(data):
    try: 
        log = Log(
            uuid=uuid.uuid4(),
            timestamp=parse(data["timestamp"]),
            source=data["source"],
            type=data["type"],
            source_type=data["source_type"],
            implementation=data["implementation"],
            event_data=data["event_data"]
        )
        return log
    except KeyError:
        print("Wrong format")
        abort(500, "Wrong Format")

if __name__ == "__main__":
    app.run()
