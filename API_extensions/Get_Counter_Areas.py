import requests
import json

get_counter_url= 'http://localhost:8080/counter/areas'
response_get_counter_url = requests.get(url=get_counter_url, verify=False)
if (response_get_counter_url.status_code == 200):
    print("SUCCESS: Counter areas added to /home/abhinav/tool3/data/Counter_Areas/counter_area.json")
    counter_data = response_get_counter_url.json()
    #print(counter_data)
    with open('/home/abhinav/tool3/data/Counter_Areas/counter_area.json', 'w') as json_file:
        json.dump(counter_data, json_file)
#print(json.dumps(counter_data, indent=4, sort_keys=True))



