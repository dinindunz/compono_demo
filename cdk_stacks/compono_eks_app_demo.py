from aws_cdk import (
    Stack
)
from cdk_constructs import (
    build_ecr_image as ecr,
    deploy_eks_cluster as eks,
    deploy_eks_fargate_cluster as eks_fargate
)
from constructs import Construct

class Deploy(Stack):

    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        ecr_repo_name='compono/eks_app_demo'
        image_tag='1.0.0'

        ecr.BuildEcrImage(
            self, 'Build_ECR_Image',
            ecr_repo_name=ecr_repo_name,
            image_tag=image_tag,
            directory='./src/compono_eks_app_demo',
            account=self.account,
            region=self.region
        )

        eks_fargate.DeployEksCluster(
            self, 'Deploy_Compono_EKS_App_Demo',
            ecr_repo_name=ecr_repo_name,
            image_tag=image_tag,
            container_port=8080
        )

        