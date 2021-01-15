This repository is forked from https://github.com/opendatacam/opendatacam and was adapted (by abhinavdrs) to suit a specific use case explained below.
For installing and running the tool, please refer to the original_README.md in this repository. 

This README details how to use the python files in API\_extensions to start opendatacam's inference on recorded videos without spending additional time in drawing counters. The APIs to can also retrieve the tracker data after the recording is done and convert it to the desired .csv format. The API\_extensions are not present in the original repository and are developed only for a special use case.

**Desired use case**: The user wants to run opendatacam on pre-recorded videos. The user changes file name in config.json to the desired video_file name and then restarts the opendatacam container. After the opendatacam loads the video in browser, the user draws counters in the desired areas of the video frame and then presses the record button to start recording which triggers the object counting and detection process. <br/>
**Problem**: A significant amount of video-length remains unrecorded before the recording can be started because drawing counters takes time.

**Solution**: Using python scripts in API_extensions, user can start the recording process much earlier. This is done by running the desired recorded video twice with opendatacam. In the first run the counters are drawn on the desired area and later the locations of these counters are stored using the scripts in API\_extensions directory. In the second run of the same video, scripts inside API\_extensions can be used to POST these counters and start recording on the the running video. The second run posts counters and starts recording in first few (2-3) seconds of the video and hence significantly reduces the time from the usual one-run approach.

The steps to be followed along with the usage of accompanying scripts are detailed below.

**First run:** Draw counters and store them in .json file. 
1) Start the desired video by editing "file:" field in config.json. (Explained in original_README.md)
2) Draw counters in the opendatacam browser tool.
3) Open 'Get-Counters_Area.py':<br/>
	3.1 edit counter\_dir and provide directory to store counters.<br/>
	       &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;counter_dir = '/path/to/your/directory/counter_file_name.json'<br/>
	3.2 Run 'Get-Counters_Area.py'<br/>
4) Verify that .json file is present in the location you provided in counter\_dir directory.

**Second Run:** POST counter you stored previously, start collecting tracking data using these counters.

1) Open 'Post\_Counter\_Areas.py' <br/>
	1.1 edit counter-dir as follows.<br/>
		&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;counter_dir = 'same as in Get-Counters_Area.py'<br/>
	1.2 close 'Post\_Counter\_Areas.py'

2) Restart the opendatacam container.

3) Run 'Run\_with\_counters.py' and verify that the console prints 'Recording is started'. This message confirms that the recording is now running with stored counter values.



**Data retrieval:**. 

1) Get the recording\_id of the finished video by running 'Get\_Status.py'.

2) Open 'Get\_Tracker\_Data.py' and provide path to store tracker.py. **DO NOT PROVIDE THE FILE NAME**.<br/>
		  	tracker_dir = '/just/the/path/'
3) Run 'Get\_Tracker\_Data.py' and provide the recording\_id (from step 1) as an argument.

4) Find the tracker data stored in the tracker_dir by the name recording\_id\_tracker\_data.csv.
