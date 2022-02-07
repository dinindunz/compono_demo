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
    codestar_con='1a99dd90-d0a9-4d4a-a4f7-cb3b28d6a4ea',
    env=env[0],
)

app.synth()
