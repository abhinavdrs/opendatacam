"""Stops recording on the current video"""

import requests

stop_recording_url= 'http://localhost:8080/recording/stop'
response_stop_recording_url = requests.get(url=stop_recording_url, verify=False)
if (response_stop_recording_url == 'OK'):
    print("Recording is Started")
