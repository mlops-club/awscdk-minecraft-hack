from aws_cdk import (
    # Duration,
    Stack,
    # aws_sqs as sqs,
)
from constructs import Construct
from aws_cdk import aws_ecr as ecr
import aws_cdk as cdk
from pathlib import Path
from aws_cdk import aws_ecs as ecs

from aws_cdk import aws_ecr_assets as ecr_assets
from aws_cdk import aws_batch as batch
from aws_cdk import aws_ec2 as ec2


THIS_DIR = Path(__file__).parent

PROJECT_ROOT_DIR = (THIS_DIR / "../../..").resolve()
MINECRAFT_SERVER_IAC_DIR = PROJECT_ROOT_DIR / "minecraft-paas-server-iac"


class PaasStack(Stack):

        def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
            super().__init__(scope, construct_id, **kwargs)


            # docker build --platform linux/amd64 path/to/minecraft-paas-server-iac
            minecraft_server_deployer_img = ecs.ContainerImage.from_asset(
                directory=str(MINECRAFT_SERVER_IAC_DIR),
                platform=ecr_assets.Platform.LINUX_AMD64,
            )


            default_vpc = ec2.Vpc.from_lookup(self, "DefaultVpc", is_default=True)

            batch_compute_env = batch.FargateComputeEnvironment(
                self,
                "FargateComputeEnvironment",
                vpc=default_vpc,
                spot=True,   
            )

            job_queue = batch.JobQueue(
                self,
                "JobQueue",
                compute_environments=[
                      batch.OrderedComputeEnvironment(
                            order=1,
                            compute_environment=batch_compute_env
                      )
                ],
            )
            

            
            job_definition = batch.EcsJobDefinition(
                self,
                "EcsJobDefinition",
                container=batch.EcsFargateContainerDefinition(
                    self,
                    "EcsFargateContainerDefinition",
                    image=minecraft_server_deployer_img,
                    memory=cdk.Size.mebibytes(1024),
                    cpu=0.5,
                    # https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task_definition_parameters.html
                )
            )
