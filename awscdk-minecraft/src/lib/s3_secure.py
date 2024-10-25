from aws_cdk import (
    aws_s3 as s3,
    RemovalPolicy,
)
from constructs import Construct


class S3SecureBucket(s3.Bucket):
    def __init__(self, scope: Construct, id: str, **kwargs):
        # Apply defaults and allow overrides using **kwargs
        super().__init__(
            scope, 
            id, 
            versioned=True,                      # Enable versioning by default
            public_read_access=False,            # Disable public read access
            block_public_access=s3.BlockPublicAccess.BLOCK_ALL,  # Block all public access
            removal_policy=RemovalPolicy.DESTROY,  # Set removal policy
            **kwargs                             # Allow users to override properties if needed
        )
