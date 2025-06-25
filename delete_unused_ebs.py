import boto3

session = boto3.session.Session(profile_name='default', region_name='us-east-1')
ec2 = session.resource('ec2')

def delete_unused_ebs():
    for volume in ec2.volumes.all():

        print(volume)

        if volume.state == 'available' and volume.attachments == []:
            print(f"Volume {volume.id} is not being used. It will be deleted!")
            volume.delete()
        else:
            print(f"Volume {volume.id} is being used.")

delete_unused_ebs()
