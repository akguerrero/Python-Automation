import boto3

session = boto3.session.Session(profile_name="default", region_name="us-east-1")
ec2 = session.client("ec2")
firewall = session.client("network-firewall")

def identify_firewall_rules(rule_group_name):
    variables = firewall.describe_rule_group(RuleGroupName=rule_group_name, Type='STATEFUL')["RuleGroup"]["RuleVariables"]
    variable_list = []
    for variable, definition in variables.items():
        variable_list.append(variable)

    print(variable_list)

identify_firewall_rules("rule-group-example")