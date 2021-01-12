import requests
import json
get_status_url= 'http://localhost:8080/status'
response_get_status_url = requests.get(url=get_status_url, verify=False)

print("Recording ID : ", json.dumps(response_get_status_url.json()["appState"]["recordingStatus"]["recordingId"] , indent=4, sort_keys=True))

#recording_id = json.dumps(response_get_status_url.json())
#print(recording_id["recordingId"])
#print(recording_id)
