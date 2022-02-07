from aws_cdk import (
    aws_eks as _eks,
    aws_ec2 as _ec2,
    aws_iam as _iam
)
from constructs import Construct

class DeployEksCluster(Construct):

    def __init__(self, scope: Construct, id: str, ecr_repo_name: str, image_tag: str, container_port: int, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)
        
        #Create EKS Cluster
        cluster_name='%s-Cluster' % id
        eks_cluster=_eks.FargateCluster(
            self, cluster_name,
            cluster_name=cluster_name,
            version=_eks.KubernetesVersion.V1_21
        )

        #eks_cluster.add_nodegroup_capacity(
        #    'node_group',
        #    min_size=1,
        #    max_size=2,
        #    instance_types=[_ec2.InstanceType('t2.micro')]
        #)

        #Deploy the App
        #eks_cluster.add_manifest("mypod", {
        #    "apiVersion": "v1",
        #    "kind": "Pod",
        #    "metadata": {"name": "mypod"},
        #    "spec": {
        #        "containers": [{
        #            "name": "hello",
        #            "image": "%s:%s" % (ecr_repo_name, image_tag),
        #            "ports": [{"containerPort": container_port}]
        #        }
        #        ]
        #    }
        #})


