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


class BatchCdkStack(Stack):
      def __init__(self, scope: Construct, construct_id: str, **kwargs) -> iam:
            super().__init__(scope, construct_id, **kwargs)

            # Create a aws iam role, for the batch job
            batch_cdk_role = iam.Role(self, "BatchCdkIamRole",
                                      assumed_by = iam.ServicePrincipal(service="ecs-tasks.amazonaws.com"),
                                      role_name = "BATCH_CDK_IAM_ROLE")
                                      
            
            # attach iam policy
            batch_cdk_role.attach_inline_policy(
        policy=iam.Policy(self, "batch-iam-role",
        policy_name="batch-cdk-iam-role-policy",
            document=iam.PolicyDocument.from_json(
                {
                    "Version": "2012-10-17",
                    "Statement": [
                        {
                            "Effect": "Allow",
                            "Action": [
                                "ecr:GetAuthorizationToken",
                                "ecr:BatchCheckLayerAvailability",
                                "ecr:GetDownloadUrlForLayer",
                                "ecr:BatchGetImage",
                                # "logs:CreateLogStream",
                                # "logs:PutLogEvents",
                                # from AWS docs
                                "ec2:DescribeAccountAttributes",
                                "ec2:DescribeInstances",
                                "ec2:DescribeInstanceAttribute",
                                "ec2:DescribeSubnets",
                                "ec2:DescribeSecurityGroups",
                                "ec2:DescribeKeyPairs",
                                "ec2:DescribeImages",
                                "ec2:DescribeImageAttribute",
                                "ec2:DescribeInstanceStatus",
                                "ec2:DescribeSpotInstanceRequests",
                                "ec2:DescribeSpotFleetInstances",
                                "ec2:DescribeSpotFleetRequests",
                                "ec2:DescribeSpotPriceHistory",
                                "ec2:DescribeVpcClassicLink",
                                "ec2:DescribeLaunchTemplateVersions",
                                "ec2:CreateLaunchTemplate",
                                "ec2:DeleteLaunchTemplate",
                                "ec2:RequestSpotFleet",
                                "ec2:CancelSpotFleetRequests",
                                "ec2:ModifySpotFleetRequest",
                                "ec2:TerminateInstances",
                                "ec2:RunInstances",
                                "autoscaling:DescribeAccountLimits",
                                "autoscaling:DescribeAutoScalingGroups",
                                "autoscaling:DescribeLaunchConfigurations",
                                "autoscaling:DescribeAutoScalingInstances",
                                "autoscaling:CreateLaunchConfiguration",
                                "autoscaling:CreateAutoScalingGroup",
                                "autoscaling:UpdateAutoScalingGroup",
                                "autoscaling:SetDesiredCapacity",
                                "autoscaling:DeleteLaunchConfiguration",
                                "autoscaling:DeleteAutoScalingGroup",
                                "autoscaling:CreateOrUpdateTags",
                                "autoscaling:SuspendProcesses",
                                "autoscaling:PutNotificationConfiguration",
                                "autoscaling:TerminateInstanceInAutoScalingGroup",
                                "ecs:DescribeClusters",
                                "ecs:DescribeContainerInstances",
                                "ecs:DescribeTaskDefinition",
                                "ecs:DescribeTasks",
                                "ecs:ListAccountSettings",
                                "ecs:ListClusters",
                                "ecs:ListContainerInstances",
                                "ecs:ListTaskDefinitionFamilies",
                                "ecs:ListTaskDefinitions",
                                "ecs:ListTasks",
                                "ecs:CreateCluster",
                                "ecs:DeleteCluster",
                                "ecs:RegisterTaskDefinition",
                                "ecs:DeregisterTaskDefinition",
                                "ecs:RunTask",
                                "ecs:StartTask",
                                "ecs:StopTask",
                                "ecs:UpdateContainerAgent",
                                "ecs:DeregisterContainerInstance",
                                "logs:CreateLogGroup",
                                "logs:CreateLogStream",
                                "logs:PutLogEvents",
                                "logs:DescribeLogGroups",
                                "iam:GetInstanceProfile",
                                "iam:GetRole",
                            ],
                            "Resource": "*",
                        }
                    ],
                }
            ),
        )
            )