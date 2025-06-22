import boto3
import pprint

session = boto3.session.Session(profile_name="default", region_name="us-east-1")

def delete_unused_elastic_ips():
    ec2 = session.client('ec2')
    #pprint.pprint(ec2.describe_addresses()["Addresses"])

    for ip in ec2.describe_addresses()["Addresses"]:
        if "AssociationId" not in ip:
            print(f"IP {ip["PublicIp"]} is unused. It will be deleted.")
            ec2.release_address(AllocationId=ip["AllocationId"])
        else:
            print(f"IP {ip["PublicIp"]} is being used.")

delete_unused_elastic_ips()