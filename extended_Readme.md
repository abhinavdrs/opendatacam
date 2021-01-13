This extended\_readme details how to use the python files in API\_extensions to start opendatacam's inference on recorded videos without spending additional time in drawing counters. The APIs to can also retrieve the tracker data after the recording is done and convert it to the desired .csv format.

Desired use case: The users want to run opendatacam on pre-recorded videos. The user changes file name in config.json to the desired video_file name and then restarts the opendatacam container. After the opendatacam browser loads the video, the user draws counters in the desired areas of the video frame and then presses the record button to start recording which triggers the object counting and detection process. 
Problem: A significant amount of video has passed before the recording can be started because drawing counters takes time.

Solution: Using python scripts in API_extensions, user can start the recording process much earlier. This is done by running the desired recorded video twice with opendatacam. In the first run the counters are drawn on the desired area and later the locations of these counters are stored using the scripts in API\_extensions directory. In the second run of the same video, scripts inside API\_extensions can be used to POST these counters and start recording on the the running video. The second run posts counters and starts recording in first few (2-3) seconds of the video and hence significantly reduces the time from the usual one-run approach.

The steps to be followed along with accompanying scripts are detailed below.

First run: Draw counters and store them in .json path. 
1) Start the desired video by editing "file:" field in config.json.
2) Draw counters in the opendatacam browser tool.
3) Open 'Get-Counters_Area.py':
	3.1 edit counter\_dir and provide directory to store counters.
		counter_dir = '/path/to/your/directory/counter_file_name.json'
	3.2 Run 'Get-Counters_Area.py'
4) Verify that .json file is present in the location you provided in counter\_dir directory.

Second Run: POST counter you stored previously, start collecting tracking data using these counters.

1) Open 'Post\_Counter\_Areas.py'
	1.1 edit counter-dir as follows.
		counter_dir = 'same as in Get-Counters_Area.py'
	1.2 close 'Post\_Counter\_Areas.py'

2) Restart the opendatacam container.

3) Run 'Run\_with\_counters.py' and verify that the console prints 'Recording is started'. This message confirms that the recording is now running with stored counter values.



Data retrieval. 

1) Get the recording\_id of the finished video by running 'Get\_Status.py'.

2) Open 'Get\_Tracker\_Data.py' and provide path to store tracker.py. DO NOT PROVIDE THE FILE NAME.
		  	tracker_dir = '/just/the/path/'
3) Run 'Get\_Tracker\_Data.py' and provide the recording\_id (from step 1) as an argument.

4) Find the tracker data stored in the tracker_dir by the name recording\_id\_tracker\_data.csv.
