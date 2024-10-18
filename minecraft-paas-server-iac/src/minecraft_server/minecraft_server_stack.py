from aws_cdk import (
    Stack,
    aws_ec2 as ec2,
    aws_iam as iam
)
from constructs import Construct
from pathlib import Path
from string import Template

THIS_DIR = Path(__file__).parent
USER_DATA_SH_TEMPLATE_FPATH = (THIS_DIR / "../../resources/user-data.template.sh").resolve()
from constructs import Construct
from typing import Any

class MinecraftServerStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, minecraft_server_version: str, **kwargs,) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Create a VPC
        _vpc = ec2.Vpc.from_lookup(
            self,
            id="DefaultVPC",
            is_default=True,
        )
        
        # Attach a security group to the VPC
        _sg = ec2.SecurityGroup(
            self,
            id="MinecraftServerSecurityGroup",
            vpc=_vpc,
            allow_all_outbound=True,
        )
        # Allow inbound traffic on port 25565 for Minecraft Server
        _sg.add_ingress_rule(
            peer=ec2.Peer.any_ipv4(),
            connection=ec2.Port.tcp(25565),
            description="Allow inbound traffic on port 25565",
        )
        # Allow inbound traffic on port 22 for SSH
        _sg.add_ingress_rule(
            peer=ec2.Peer.any_ipv4(),
            connection=ec2.Port.tcp(22),
            description="Allow inbound traffic on port 22",
        )
        # Allow all outbound traffic to connect to the internet
        _sg.add_egress_rule(
            peer=ec2.Peer.any_ipv4(),
            connection=ec2.Port.all_traffic(),
            description="Allow all outbound traffic",
        )
        
        # Create a IAM role for the EC2 instance using AmazonSSMManagedInstanceCore 
        # so we can connect to the instance locally without using a key pair
        _iam_role = iam.Role(
            self,
            id="MinecraftServerIAMRole",
            assumed_by=iam.ServicePrincipal("ec2.amazonaws.com"),
            managed_policies=[
                iam.ManagedPolicy.from_aws_managed_policy_name("AmazonSSMManagedInstanceCore"),
            ],
        )
        
        # Define User Data script
        _user_data_script  = ec2.UserData.custom(
            render_user_data_script(
                minecraft_semantic_version=minecraft_server_version,
                aws_account_id=self.account,
                aws_region=self.region,
            )
        )
        
        # Setup an EC2 instance
        ec2.Instance(
            self,
            "MinecraftServer",
            instance_type=ec2.InstanceType("t2.medium"),
            machine_image=ec2.MachineImage.latest_amazon_linux2(),
            vpc=_vpc,
            security_group=_sg,
            role=_iam_role,
            user_data=_user_data_script,
        )
        
        # Build the docker image and run it
        
        # ----------------
        
        # Push the image to ECR
        
        # ---------------
        
        # We could do backups to S3



def render_user_data_script(
    minecraft_semantic_version: str,
    aws_account_id: str,
    aws_region: str,
) -> str:
    """Render the user data script for the EC2 instance.

    :param minecraft_semantic_version: The semantic version of the Minecraft server to install.
    :param backup_service_docker_image_uri: The URI of the Docker image in ECR for the backup service.
    """
    return Template(USER_DATA_SH_TEMPLATE_FPATH.read_text()).substitute(
        {
            "AWS_ACCOUNT_ID": aws_account_id,
            "AWS_REGION": aws_region,
            "MINECRAFT_SERVER_SEMANTIC_VERSION": minecraft_semantic_version,
        }
    )        
        # example resource
        # queue = sqs.Queue(
        #     self, "CdkBoilerplateQueue",
        #     visibility_timeout=Duration.seconds(300),
        # )
        