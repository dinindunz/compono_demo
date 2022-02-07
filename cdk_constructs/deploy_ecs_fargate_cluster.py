from aws_cdk import (
    aws_ecs as _ecs,
    aws_ecs_patterns as _ecs_patterns,
    aws_ec2 as _ec2
)
from constructs import Construct

class DeployEcsCluster(Construct):

    def __init__(self, scope: Construct, id: str, ecr_repo_name: str, image_tag: str, container_port: int, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)
        
        #Create EKS Cluster
        vpc=_ec2.Vpc(
          self, 'vpc',
          max_azs=3
        )
        cluster=_ecs.Cluster(
          self, 'cluster',
          vpc=vpc
        )
        task_definition=_ecs.FargateTaskDefinition(
          self, 'UnicornServiceTask',
          family='UnicornServiceTask'
        )
        container=task_definition.add_container(
          'app',
          image=_ecs.ContainerImage.from_ecr_repository(ecr_repo_name, image_tag)
        )
        container.add_port_mappings(_ecs.PortMapping(container_port=8080))
        
        fargate_service=_ecs_patterns.ApplicationLoadBalancedFargateService(
          self, 'fargate_service',
          cluster=cluster,
          cpu=256,
          desired_count=1,
          task_definition=task_definition,
          memory_limit_mib=512,
          public_load_balancer=True
        )


