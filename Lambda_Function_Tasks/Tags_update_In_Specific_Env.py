##Update of all ec2 resources in sandbox to have default tags

#- get all instances in all regions

import boto3


InstanceIds=[]

# function to list all instances in all regions
def get_instances():
    client = boto3.client('ec2')
    response = client.describe_instances()
    for i in response["Reservations"]:
        for j in i["Instances"]:
            InstanceIds.append(j["InstanceId"])
    return InstanceIds

      
# function to get all ebs volumes
def get_ebsvolumes(instanceids):
    client = boto3.client('ec2')
    response = client.describe_volumes(
        Filters=[
            {
                'Name': 'attachment.instance-id',
                'Values': instanceids
            },
        ],
)
    
# function to update tags/create tags
def create_tags(instanceids):
    client = boto3.client('ec2')
    response = client.create_tags(
        Resources=instanceids,  # Pass the list of instance IDs here
        Tags=[
            {
                'Key': 'Name',
                'Value': 'Test'
            },
            {
                'Key': 'Company',
                'Value': 'JJtech Inc'
            },
            {
                'Key': 'Createdby',
                'Value': 'Augustine'
            }
        ]
    )
    
def lambda_handler(event, context):
    client = boto3.client('ec2')
    response = client.describe_instances()
    instanceids = get_instances()    
    create_tags(instanceids)
    get_ebsvolumes(instanceids)

################################################################################
import boto3

InstanceIds = []

# Function to list all instances in all regions
def get_instances():
    client = boto3.client('ec2')
    response = client.describe_instances()
    for i in response["Reservations"]:
        for j in i["Instances"]:
            InstanceIds.append(j["InstanceId"])
    return InstanceIds

# Function to get all EBS volumes associated with specific instances
def get_ebsvolumes(instanceids):
    client = boto3.client('ec2')
    response = client.describe_volumes(
        Filters=[
            {
                'Name': 'attachment.instance-id',
                'Values': instanceids,
            },
        ],
    )
    # Process the response to work with EBS volumes as needed

# Function to update tags/create tags for EC2 instances
def create_tags(instanceids):
    client = boto3.client('ec2')
    response = client.create_tags(
        Resources=instanceids,  # Pass the list of instance IDs here
        Tags=[
            {
                'Key': 'Name',
                'Value': 'Test'
            },
            {
                'Key': 'Company',
                'Value': 'JJtech Inc'
            },
            {
                'Key': 'Createdby',
                'Value': 'Augustine'
            }
        ]
    )

def lambda_handler(event, context):
    client = boto3.client('ec2')
    response = client.describe_instances()
    instanceids = get_instances()
    create_tags(instanceids)
    # Optionally, you can call get_ebsvolumes(instanceids) here if needed

# Remove the get_ebsvolumes(instanceids) call if not needed for your specific use case
