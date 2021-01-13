"""Retrieves the counters stored using Get_Counter_Areas and POST them on the running video. Invoked by Run_with_Counters.py"""
import requests
import json

#counter_dir should be same as in Get_Counter_Areas.py

counter_dir = 'your_directory_of_choice/counter_file_name.json'
received_counter_area_data = json.loads(open(counter_dir, 'r').read())


#Iterate over counter_area dict
for keys in received_counter_area_data:
    #to delete 'computed' key as it is not expected in the POST  request
    del received_counter_area_data[keys]['computed']


Post_counter_area_data = {"countingAreas": received_counter_area_data}
headers = {'Content-type': 'application/json'}
response_post_counter_areas = requests.post('http://localhost:8080/counter/areas', json = Post_counter_area_data)


if(response_post_counter_areas.status_code == 200):
    print('SUCCESS: Counter areas added from ' + counter_dir)







