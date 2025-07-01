import boto3

session = boto3.session.Session(profile_name='default', region_name='us-east-1')
def handler(event, context):
  ec2 = session.client('ec2')
  volumes = ec2.describe_volumes()
  total_size = sum(volume['Size'] for volume in volumes['Volumes'])
  return {'TotalSizeGB': total_size}

total_size = handler(None, None)
print(f"Total size of all volumes: {total_size['TotalSizeGB']} GB")