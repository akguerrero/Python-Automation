import boto3
from pprint import pprint
from datetime import datetime, timedelta, timezone

session = boto3.session.Session(profile_name="default", region_name="us-east-1")

def delete_old_snapshots():
    ec2 = session.client("ec2")
    today = datetime.now(timezone.utc)
    retention_period = timedelta(days=180) # 6 months
    cutoff_date = today - retention_period
    print(f"Today's date: {today}, six months ago was date: {cutoff_date}")

    for snapshot in ec2.describe_snapshots(OwnerIds=['self'])['Snapshots']:
        if snapshot["StartTime"] < cutoff_date:
            print(f"snapshot {snapshot["SnapshotId"]} is too old. Deleting it.")
            #ec2.delete_snapshot(SnapshotId=snapshot["SnapshotId"])
        else:
            print(f"Skipping snapshot {snapshot['SnapshotId']} because it's too new")

delete_old_snapshots()