import json
import csv
import pandas as pd
from pandas.io.json import json_normalize

dirty_data = json.loads(open('/home/abhinav/tracker','r').read())

clean_data = json_normalize(data = dirty_data, record_path= 'objects', meta = ['_id' , 'recordingId' , 'timestamp'])
clean_data.to_csv('/home/abhinav/clean_data.csv')
