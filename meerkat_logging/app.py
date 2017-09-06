"""
meerkat_logging

Api for gathering event logs

"""
from flask import Flask, abort, request, current_app
import time
from dateutil.parser import parse
import uuid
from meerkat_logging import model
from meerkat_libs.logger_client import FlaskActivityLogger
from meerkat_logging.setup_database import setup_database
from flask_sqlalchemy import SQLAlchemy
from meerkat_libs.auth_client import auth
# Create the Flask app

app = Flask(__name__)

app.config.from_object('config.Development')

# Set up DB
setup_database(url=app.config["SQLALCHEMY_DATABASE_URI"], base=model.Base)
db = SQLAlchemy(app)

app.secret_key = uuid.uuid4()
print(app.config)
FlaskActivityLogger(app, ["/event"])

@app.route("/", methods=['GET'])
def root():
    return "Meerkat Logging"


@app.route("/event", methods=['POST'])
@auth.authorise(["logging"], ["meerkat"])
def add_event():
    t = time.time()
    post_data = request.get_json()
    print(post_data)
    if post_data:
        log_entry = input_to_log(post_data)
        db.session.add(log_entry)
        db.session.commit()
    print(time.time() - t)
    return "OK"


def input_to_log(data):
    try:
        log = model.Log(
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
