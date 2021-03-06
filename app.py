#!/usr/bin/env python3
import os
from typing_extensions import Self
import aws_cdk as cdk

from cdk_stacks.cdk_code_pipeline import CdkCodePipelineStack
from common.get_environment import GetEnvironment
from cdk_stacks.compono_eks_app_demo import Deploy

app=cdk.App()

env=GetEnvironment.aws_enviromnet('tooling')
CdkCodePipelineStack(
    app, 'Compono-CDK-Pipeline-Deploy-EKS-Clusters',
    owner='dinindunz',
    repo='compono_demo',
    codestar_con='dfc7050c-f2f2-49a9-9083-ffa4776a3649',
    env=env[0],
)

app.synth()
