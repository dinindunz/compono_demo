from os import environ
import aws_cdk as cdk
from constructs import Construct
from cdk_stacks import(
    compono_eks_app_demo as ComponoEksAppDemo
)
from common.get_environment import GetEnvironment

class DeployStacks(cdk.Stage):

    def __init__(self, scope: Construct, id: str, aws_account, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)
        
        env=GetEnvironment.aws_enviromnet(aws_account)

        ComponoEksAppDemo.Deploy(self, 'Compono-EKS-App-Demo', env=env[0])