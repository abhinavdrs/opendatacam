""" Starts recording on the current video """
import requests
import datetime
start_recording_url= 'http://localhost:8080/recording/start'
response_start_recording_url = requests.get(url=start_recording_url, verify=False)

if (response_start_recording_url.status_code == 200):
    with open('/home/abhinav/tool3/data/Counter_Areas/timestamp.txt', 'w') as text:
        text.write(datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S"))
        print("SUCCESS: Recording is Started, timestamp created in /home/abhinav/tool3/data/Counter_Areas/timestamp.txt ")
        print("Success Code", response_start_recording_url.status_code)

