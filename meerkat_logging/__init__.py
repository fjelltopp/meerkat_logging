import requests
import datetime


def send_log(url, event_type, source, source_type, implementation,
             event_data, timestamp=None):
    """
    Sends http post request to url with all the data
    """
    if not timestamp:
        timestamp = datetime.datetime.now().isoformat()
    result = requests.post(url + "/event",
                           data={
                               "timestamp": timestamp,
                               "type": event_type,
                               "source": source,
                               "source_type": source_type,
                               "implementation": implementation,
                               "event_data": event_data
                           })
    if result.status_code == 200:
        return True
    else:
        return False
