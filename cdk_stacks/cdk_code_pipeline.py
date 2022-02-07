from tkinter.messagebox import NO
from aws_cdk import (
    Stack,
    pipelines as _pipelines,
    aws_codepipeline as _codepipeline,
    aws_codepipeline_actions as _codepipeline_actions,
    aws_codestarconnections as _codestar_con
)
from constructs import Construct
from common.get_environment import GetEnvironment
from common.deploy_stacks import DeployStacks

class CdkCodePipelineStack(Stack):

    def __init__(self, scope: Construct, id: str, owner: str, repo: str, codestar_con: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        dev_env=GetEnvironment.aws_enviromnet('dev')
        prod_env=GetEnvironment.aws_enviromnet('prod')
        
        #Deploy CDK Code Pipeline
        code_pipeline=_pipelines.CodePipeline(
            self, self.stack_name, 
            pipeline_name=self.stack_name,
            synth=_pipelines.ShellStep(
                'Synth', 
                input=_pipelines.CodePipelineSource.connection(
                    repo_string='%s/%s' % (owner, repo),
                    connection_arn='arn:aws:codestar-connections:%s:%s:connection/%s' % (self.region, self.account, codestar_con),
                    branch='master',
                    trigger_on_push=True
                ),
                commands=[
                    'npm install -g aws-cdk', 
                    'python3 -m pip install -r requirements.txt', 
                    'cdk synth',
                    'ls -al'
                ]
            ),
            #Deply only the pipeline first with SelfMutation=False, then redeploy by setting it to True
            #Give Admin access to codepipeline role and buildproject role
            self_mutation=True
        )

        #if source_action.variables.branch_name=='dev':
        code_pipeline.add_stage(
            DeployStacks(self, 'Deploy-Dev', 'dev', env=dev_env[0])
        )

        #deploy_pipeline.add_application_stage(
        #    DeployModules(self, 'Deploy-Prod', 'prod', env=prod_env[0])
        #)