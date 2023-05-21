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
A setup prereq is to have either an s3 bucket created or a kinesis data stream created in AWS.  This must also include an IAM role with the ability to write to either resource you have chosen to use.  The terminal you are using to run this script must be authenticated using that IAM role.
Update the config file to include the bucket name or data stream name, and your tenant name.

## Run
In the authenticated terminal run the main script with the kinesis or s3 parameter.