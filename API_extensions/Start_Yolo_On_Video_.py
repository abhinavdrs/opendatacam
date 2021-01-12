import requests

start_yolo_url= 'http://localhost:8080/start'
response_yolo_url = requests.get(url=start_yolo_url, verify=False)
if (response_yolo_url == 'OK'):
    print("Yolo is hooked on the video")
