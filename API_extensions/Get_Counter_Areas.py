"""Get_Counter_Areas.py stores the locations of drawn counters on the currently processing video. """
import requests
import json

#counter_dir is the directory where the counter_areas will be stored
counter_dir = 'your_directory_of_choice'
get_counter_url= 'http://localhost:8080/counter/areas'
response_get_counter_url = requests.get(url=get_counter_url, verify=False)
if (response_get_counter_url.status_code == 200):
    print("SUCCESS: Counter areas added" + counter_dir)
    counter_data = response_get_counter_url.json()
    #print(counter_data)
    with open(counter_dir, 'w') as json_file:
        json.dump(counter_data, json_file)
#print(json.dumps(counter_data, indent=4, sort_keys=True))

