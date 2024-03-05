### Code terminates all instances at a time 6pm
import boto3

import datetime

## Stoppaged time
stop_time = datetime.time(18, 0)  # 6:00 PM

##Get all instancids
Ec2_InstanceIds=[]

def get_all_instances():
    client = boto3.client('ec2')
    response = client.describe_instances()
    for i in response["Reservations"]:
        for j in i["Instances"]:
            Ec2_InstanceIds.append(j["InstanceId"])
    return Ec2_InstanceIds

## Time to stop instances 
def stoppage_time():
    # Get the current time
    current_time = datetime.datetime.now().time()
    
    # Compare the current time to the stop time
    return current_time >= stop_time

## stop all ec2 instances
def terminate_instances(instanceids):
    client = boto3.client('ec2')
    response = client.terminate_instances(
        InstanceIds=instanceids
    )

def lambda_handler(event, context):
    if stoppage_time():
        client = boto3.client('ec2')
        response = client.describe_instances()
        instanceids = get_all_instances()    
        terminate_instances(instanceids)