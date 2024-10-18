#!/usr/bin/env python3
import os
import boto3

import aws_cdk as cdk

from src.minecraft_server.minecraft_server_stack import MinecraftServerStack

AWS_ACCOUNT_ID = boto3.client('sts').get_caller_identity().get('Account')
AWS_REGION = os.getenv("AWS_REGION", "us-west-2")
MINECRAFT_SERVER_VERSION = os.environ.get("MINECRAFT_SERVER_VERSION", "1.19.3")

app = cdk.App()
MinecraftServerStack(app, "MinecraftServerStack",
    # If you don't specify 'env', this stack will be environment-agnostic.
    # Account/Region-dependent features and context lookups will not work,
    # but a single synthesized template can be deployed anywhere.

    # Uncomment the next line to specialize this stack for the AWS Account
    # and Region that are implied by the current CLI configuration.

    #env=cdk.Environment(account=os.getenv('CDK_DEFAULT_ACCOUNT'), region=os.getenv('CDK_DEFAULT_REGION')),

    # Uncomment the next line if you know exactly what Account and Region you
    # want to deploy the stack to. */

    env=cdk.Environment(account=AWS_ACCOUNT_ID, region=AWS_REGION),
    minecraft_server_version=MINECRAFT_SERVER_VERSION,

    # For more information, see https://docs.aws.amazon.com/cdk/latest/guide/environments.html
    )


app.synth()
