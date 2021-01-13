"""Returns recording id assigned to the current video. It is invoked by Run_with_Counters.py."""

import requests
import json
get_status_url= 'http://localhost:8080/status'
response_get_status_url = requests.get(url=get_status_url, verify=False)

print("Recording ID : ", json.dumps(response_get_status_url.json()["appState"]["recordingStatus"]["recordingId"] , indent=4, sort_keys=True))

