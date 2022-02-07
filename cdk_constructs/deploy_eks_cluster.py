from aws_cdk import (
    aws_eks as _eks,
    aws_ec2 as _ec2,
    aws_iam as _iam
)
from constructs import Construct

class DeployEksCluster(Construct):

    def __init__(self, scope: Construct, id: str, ecr_repo_name: str, image_tag: str, container_port: int, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)
        
        #Get the VPC
        #vpc=_ec2.Vpc.from_lookup(
        #  self, 'vpc',
        #  is_default=True
        #)
        
        #Create EKS Cluster Role
        cluster_name='%s-Cluster' % id
        #cluster_role=_iam.Role(
        #  self, '%s-Role' % cluster_name,
        #  assumed_by=_iam.AccountRootPrincipal()
        #)
        
        #Deploy Cluster
        eks_cluster=_eks.Cluster(
          self, cluster_name,
          cluster_name=cluster_name,
          version=_eks.KubernetesVersion.V1_21,
          default_capacity_instance=_ec2.InstanceType.of(
            _ec2.InstanceClass.BURSTABLE2,
            _ec2.InstanceSize.MICRO
          ),
          default_capacity=1
        )

        #eks_cluster.add_nodegroup_capacity(
        #  'node_group',
        #  instance_types=_ec2.InstanceType.of(
        #    _ec2.InstanceClass.BURSTABLE2,
        #    _ec2.InstanceSize.MICRO
        #  ),
        #  min_size=1,
        #  max_size=2
        #)

        #Deploy the App
        eks_cluster.add_manifest("mypod", {
            "apiVersion": "v1",
            "kind": "Pod",
            "metadata": {"name": "mypod"},
            "spec": {
                "containers": [{
                    "name": "hello",
                    "image": "%s:%s" % (ecr_repo_name, image_tag),
                    "ports": [{"containerPort": container_port}]
                }
                ]
            }
        })


