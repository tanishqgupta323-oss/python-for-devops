functions in devops

def s3():
    return boto3.client('s3')
def ec2():
    return boto3.client('ec2')
def lambda_client():
    return boto3.client('lambda')
def dynamodb():    
    return boto3.client('dynamodb')
def cloudwatch():
    return boto3.client('cloudwatch')

modules use in 
aws- boto3
github- github
jira- jira
http- reuests
python hub - PYPI (python package index)
you can install using (pip install boto3)
- (pip install virtualenv) (python -m venv project-abc)- to create a virtual environment (ls ltr)....(source project-abc/bin/activate)- to activate the virtual environment (pip install jira) this will install in project-abc virtual environment........(pip list | grep jira)-to see the installed package.......(deactivate)- to deactivate the virtual environment...
pip list - to list all the installed packages