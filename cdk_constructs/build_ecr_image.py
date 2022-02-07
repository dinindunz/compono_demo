from aws_cdk import (
    aws_ecr as _ecr,
    aws_ecr_assets as _ecr_assets
)
from constructs import Construct
import cdk_ecr_deployment as _ecr_deployment

class BuildEcrImage(Construct):

    def __init__(self, scope: Construct, id: str, ecr_repo_name: str, image_tag: str, directory: str, account: str, region: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        #Create ECR Repo
        ecr_repo=_ecr.Repository(
          self, id,
          repository_name=ecr_repo_name
        )

        #Build Docker Image
        docker_image=_ecr_assets.DockerImageAsset(
          self, ecr_repo_name,
          directory=directory
        )

        #Push Image to ECR  
        ecr_deployment=_ecr_deployment.ECRDeployment(
          self, 'ecr_deployment',
          src=_ecr_deployment.DockerImageName(docker_image.image_uri),
          dest=_ecr_deployment.DockerImageName('%s.dkr.ecr.%s.amazonaws.com/%s:%s' %(account, region, ecr_repo_name, image_tag))
        )
