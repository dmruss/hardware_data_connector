# Hardware Data Connector

## Description
This is a tool to record hardware measurements.  The data is collected using the psutil module and then can be recorded to AWS via S3 or Kinesis data streams.  This tool was created as a useful as a way to generate data for a batch or streaming data pipeline work.  
The fields currently recorded are:
```
{
    user time: time spent by normal processes executing in user mode,
    system time:  time spent by processes executing in kernel mode,
    idle time: time spent doing nothing,
    available memory: the memory that can be given instantly to processes without the system going into swap,
    used memory:  memory used,
    process count: number of currently running processes 
}
```

## Setup

