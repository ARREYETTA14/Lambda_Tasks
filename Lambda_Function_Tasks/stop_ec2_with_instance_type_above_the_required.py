### Code terminates all instances with instance type > t3.medium
import boto3

## Minimum instance type
mini_instancetype = "t3.medium"

## To see list of Instance Ids
Ec2_InstanceIds=[]

## Get all Instance
def get_all_instances():
    client = boto3.client('ec2')
    response = client.describe_instances()
    for i in response["Reservations"]:
        for j in i["Instances"]:
            InstanceIds = j["InstanceId"]
            Instance_type = j["InstanceType"]
            if Instance_type > mini_instancetype:
                Ec2_InstanceIds.append(j["InstanceId"])

    return Ec2_InstanceIds

## stop the instances
def terminate_instances(instanceids):
    client = boto3.client('ec2')
    response = client.terminate_instances(
        InstanceIds=instanceids
    )
## The Lambda handler
def lambda_handler(event, context):
        client = boto3.client('ec2')
        response = client.describe_instances()
        instanceids = get_all_instances()    
        terminate_instances(instanceids)


