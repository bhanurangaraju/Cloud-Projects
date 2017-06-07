After cloning the project from git 
	
		
		--> copy mapper.py and reducer.py to your home directory.



**Command to run mappper and reducer on Hadoop File System:**

	>> hadoop jar /opt/hadoop-2.7.1/share/hadoop/tools/lib/hadoop-streaming-2.7.1.jar \
	  -file /home/$USER/mapper.py    -mapper /home/$USER/mapper.py \
	  -file /home/$USER/reducer.py   -reducer /home/$USER/reducer.py \
	   -input /data/nyc/nyc-traffic.csv  -output /user/$USER/OUTPUT



**Summary Statistics:**
	
	>>  hadoop fs -cat /user/$USER/OUTPUT/*

		AMBULANCE			3713
		BICYCLE 			24153
		BUS					25871
		FIRE TRUCK			1333
		LARGE COM VEH(6 OR MORE TIRES)	27981
		LIVERY VEHICLE			17775
		MOTORCYCLE				10029
		OTHER					51360
		PASSENGER VEHICLE		1005161
		PEDICAB					123
		PICK-UP TRUCK			26281
		SCOOTER					534
		SMALL COM VEH(4 TIRES)	30048
		SPORT UTILITY / STATION WAGON 	363210
		TAXI    			63892
		UNKNOWN				105481
		VAN					51666
		

**Command to print log on HDFS:**
	
	>> yarn logs -applicationId  <APPLICATION_ID>


**Log File:**


	17/04/03 22:06:28 WARN streaming.StreamJob: -file option is deprecated, please use generic option -files instead.
	packageJobJar: [/home/rangarba/mapper.py, /home/rangarba/reducer.py, /tmp/hadoop-unjar3571121104722136990/] [] /tmp/streamjob7279801730933191670.jar tmpDir=null
	17/04/03 22:06:30 INFO impl.TimelineClientImpl: Timeline service address: http://hadoop2-0-0.cscloud.ceas.uc.edu:8188/ws/v1/timeline/
	17/04/03 22:06:30 INFO client.RMProxy: Connecting to ResourceManager at hadoop2-0-0.cscloud.ceas.uc.edu/192.168.2.20:8050
	17/04/03 22:06:31 INFO impl.TimelineClientImpl: Timeline service address: http://hadoop2-0-0.cscloud.ceas.uc.edu:8188/ws/v1/timeline/
	17/04/03 22:06:31 INFO client.RMProxy: Connecting to ResourceManager at hadoop2-0-0.cscloud.ceas.uc.edu/192.168.2.20:8050
	17/04/03 22:06:31 INFO mapred.FileInputFormat: Total input paths to process : 1
	17/04/03 22:06:31 INFO net.NetworkTopology: Adding a new node: /admin-16-core/192.168.2.21:50010
	17/04/03 22:06:31 INFO net.NetworkTopology: Adding a new node: /admin-16-core/192.168.2.20:50010
	17/04/03 22:06:31 INFO net.NetworkTopology: Adding a new node: /24-core/192.168.2.25:50010
	17/04/03 22:06:31 INFO net.NetworkTopology: Adding a new node: /24-core/192.168.2.24:50010
	17/04/03 22:06:31 INFO net.NetworkTopology: Adding a new node: /16-core/192.168.2.22:50010
	17/04/03 22:06:31 INFO net.NetworkTopology: Adding a new node: /16-core/192.168.2.23:50010
	17/04/03 22:06:32 INFO mapreduce.JobSubmitter: number of splits:2
	17/04/03 22:06:32 INFO mapreduce.JobSubmitter: Submitting tokens for job: job_1487033268220_0810
	17/04/03 22:06:32 INFO impl.YarnClientImpl: Submitted application application_1487033268220_0810
	17/04/03 22:06:32 INFO mapreduce.Job: The url to track the job: http://hadoop2-0-0.cscloud.ceas.uc.edu:8088/proxy/application_1487033268220_0810/
	17/04/03 22:06:32 INFO mapreduce.Job: Running job: job_1487033268220_0810
	17/04/03 22:06:38 INFO mapreduce.Job: Job job_1487033268220_0810 running in uber mode : false
	17/04/03 22:06:38 INFO mapreduce.Job:  map 0% reduce 0%
	17/04/03 22:06:49 INFO mapreduce.Job:  map 43% reduce 0%
	17/04/03 22:06:52 INFO mapreduce.Job:  map 83% reduce 0%
	17/04/03 22:06:53 INFO mapreduce.Job:  map 100% reduce 0%
	17/04/03 22:07:05 INFO mapreduce.Job:  map 100% reduce 88%
	17/04/03 22:07:06 INFO mapreduce.Job:  map 100% reduce 100%
	17/04/03 22:07:06 INFO mapreduce.Job: Job job_1487033268220_0810 completed successfully
	17/04/03 22:07:06 INFO mapreduce.Job: Counters: 50
	        File System Counters
	                FILE: Number of bytes read=40558930
	                FILE: Number of bytes written=81516988
	                FILE: Number of read operations=0
	                FILE: Number of large read operations=0
	                FILE: Number of write operations=0
	                HDFS: Number of bytes read=176307514
	                HDFS: Number of bytes written=314
	                HDFS: Number of read operations=9
	                HDFS: Number of large read operations=0
	                HDFS: Number of write operations=2
	        Job Counters
	                Launched map tasks=2
	                Launched reduce tasks=1
	                Other local map tasks=1
	                Data-local map tasks=1
	                Total time spent by all maps in occupied slots (ms)=49162
	                Total time spent by all reduces in occupied slots (ms)=19060
	                Total time spent by all map tasks (ms)=24581
	                Total time spent by all reduce tasks (ms)=9530
	                Total vcore-seconds taken by all map tasks=24581
	                Total vcore-seconds taken by all reduce tasks=9530
	                Total megabyte-seconds taken by all map tasks=37756416
	                Total megabyte-seconds taken by all reduce tasks=19517440
	        Map-Reduce Framework
	                Map input records=924098
	                Map output records=1808611
	                Map output bytes=36941702
	                Map output materialized bytes=40558936
	                Input split bytes=240
	                Combine input records=0
	                Combine output records=0
	                Reduce input groups=17
	                Reduce shuffle bytes=40558936
	                Reduce input records=1808611
	                Reduce output records=17
	                Spilled Records=3617222
	                Shuffled Maps =2
	                Failed Shuffles=0
	                Merged Map outputs=2
	                GC time elapsed (ms)=328
	                CPU time spent (ms)=30700
	                Physical memory (bytes) snapshot=1794785280
	                Virtual memory (bytes) snapshot=10284003328
	                Total committed heap usage (bytes)=1587019776
	        Shuffle Errors
	                BAD_ID=0
	                CONNECTION=0
	                IO_ERROR=0
	                WRONG_LENGTH=0
	                WRONG_MAP=0
	                WRONG_REDUCE=0
	        File Input Format Counters
	                Bytes Read=176307274
	        File Output Format Counters
	                Bytes Written=314
			17/04/03 22:07:06 INFO streaming.StreamJob: Output directory: /tmp/finalout1.txt
	
