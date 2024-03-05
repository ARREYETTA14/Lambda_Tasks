### Code Starts all instances at a time 8am
import boto3

import datetime

## Estimated Start time
start_time = datetime.time(8, 0)  # 8AM

##Get all instancids
Ec2_InstanceIds=[]

def get_all_instances():
    client = boto3.client('ec2')
    response = client.describe_instances()
    for i in response["Reservations"]:
        for j in i["Instances"]:
            Ec2_InstanceIds.append(j["InstanceId"])
    return Ec2_InstanceIds

## Time to start instances 
def start_time():
    # Get the current time
    current_time = datetime.datetime.now().time()
    
    # Compare the current time to the stop time
    return current_time >= start_time

## start all ec2 instances
def start_instances(instanceids):
    client = boto3.client('ec2')
    response = client.start_instances(
        InstanceIds=instanceids
    )

def lambda_handler(event, context):
    if start_time():
        client = boto3.client('ec2')
        response = client.describe_instances()
        instanceids = get_all_instances()    
        start_instances(instanceids)

    else:
        print("Not time to start Instances")



