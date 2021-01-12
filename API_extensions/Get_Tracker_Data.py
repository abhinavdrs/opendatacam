import sys
import requests
import json
from pandas.io.json import json_normalize
from pathlib import Path
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

clean_data = json_normalize(data = dirty_data, record_path= 'objects', meta = ['_id' , 'recordingId' , 'timestamp'])

arg_csv_path = '/home/abhinav/tool3/data/Tracker_Data/rec_id_tracker_data.csv'
csv_path = arg_csv_path.replace("rec_id",recording_id)
clean_data.to_csv(csv_path)



