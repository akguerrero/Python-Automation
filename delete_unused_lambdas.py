import boto3
from datetime import datetime, timedelta
from pprint import pprint

session = boto3.session.Session(profile_name='default', region_name='us-east-1')
lambda_client = session.client('lambda')
logs_client = session.client('logs')

def delete_unused_lambdas():
    #pprint(lambda_client.list_functions()["Functions"])
    for lambda_function in lambda_client.list_functions()["Functions"]:
        lambda_name = lambda_function["FunctionName"]
        log_group_name = lambda_client.get_function(FunctionName=lambda_name)["Configuration"]["LoggingConfig"]["LogGroup"]

        try:
            last_event = logs_client.describe_log_streams(logGroupName=log_group_name)["logStreams"][0]["lastEventTimestamp"]
            last_event_date = datetime.fromtimestamp(last_event / 1000)
        except:
            last_event_date = None

        max_unused_duration = timedelta(days=60)
        cutoff_date = datetime.now() - max_unused_duration
        if last_event_date is None:
            print(f"Lambda {lambda_name} has no logs. Skipping it.")
        elif last_event_date < cutoff_date:
            print(f"Lambda {lambda_name} is unused. Deleting it.")
        else:
            print(f"Lambda {lambda_name} is used. Skipping it.")

    

delete_unused_lambdas()