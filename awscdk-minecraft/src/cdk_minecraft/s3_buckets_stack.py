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
from aws_cdk import aws_iam as iam
from lib.s3_secure import S3SecureBucket

class S3BucketStack(Stack):
      def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
            super().__init__(scope, construct_id, **kwargs)

            # Bucket for the backup of the world, nether, end, player inventories, etc
            game_data = S3SecureBucket(self, 
                                       "GameDataBucket",
                                       bucket_name = "game-data-s3-bucket"
                                       )

            front_end_asset = S3SecureBucket(self,
                                             "FrontEndAssetBucket",
                                             bucket_name = "react-frontend-asset")
            
            