1. Install the CodeDeploy agent in the `code-deploy-agent-docs.sh` file
2. Ensure to have an `appspec.yml` file in the root directory for the application
3. Ensure that the IAM role attached to the EC2 instance has the following permissions:
    `AmazonEC2RoleforAWSCodeDeploy`
    `AWSCodeDeployRole`