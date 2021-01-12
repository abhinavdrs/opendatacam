#figure out a way to read counter.json andpost it to opendata cam. remember request library for doing all this
import requests
import json

received_counter_area_data = json.loads(open('/home/abhinav/tool3/data/Counter_Areas/counter_area.json', 'r').read())


#Iterate over counter_area dic
for keys in received_counter_area_data:
    #to delete 'computed' key as it is not expected in the POST  request
    del received_counter_area_data[keys]['computed']


Post_counter_area_data = {"countingAreas": received_counter_area_data}
#print("Making counter area ready to send")
#print(json.dumps(Post_counter_area_data , indent=4, sort_keys=True))

#print(counter_data['5287124a-4598-44e7-abaf-394018a7278b']['color'])
#print(counter_data.pop('color'))

headers = {'Content-type': 'application/json'}
response_post_counter_areas = requests.post('http://localhost:8080/counter/areas', json = Post_counter_area_data)
#print(response_post_counter_areas.status_code)
if(response_post_counter_areas.status_code == 200):
    print('SUCCESS: Counter areas added from /home/abhinav/tool3/data/Counter_Areas/counter_area.json ')




