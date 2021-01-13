"""Retrieves the tracker data generated from currently recorded video in .json format and converts it to the desired .csv format."""
#takes recording_ID as input.

import sys
import requests
import json
from pandas.io.json import json_normalize
from pathlib import Path

#tracker_dir is the directory where the tracking areas would  will be stored
tracker_dir = 'your_directory_of_choice/'

#print number of arguments and their list representation
print('Number of arguments:', len(sys.argv), 'arguments.')
print ('Argument List:', str(sys.argv))

if(len(sys.argv)>1):
    recording_id = str(sys.argv[1])
    print(recording_id)

else:
    print("Please provide recording ID as 'Only' argument to Get_Tracker_Data.py")


arg_url = "http://localhost:8080/recording/rec_id/tracker"

url= arg_url.replace("rec_id",recording_id)

print(url)
response = requests.get(url=url, verify=False)
print(response)

dirty_data = response.json()
#print(dirty_data)

#transform data in the desired format
clean_data = json_normalize(data = dirty_data, record_path= 'objects', meta = ['_id' , 'recordingId' , 'timestamp'])
tracker_file_name = 'rec_id_tracker_data.csv'
tracker_file_name = tracker_file_name.replace("rec_id",recording_id)

csv_path = os.path.join(tracker_dir,tracker_file_name)
clean_data.to_csv(csv_path)



