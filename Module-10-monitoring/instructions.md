1. Prerequisites
WSL installed (Ubuntu) if on Windows. If on MacOS, use the standard terminal.
Install `eksctl`: https://docs.aws.amazon.com/eks/latest/userguide/eksctl.html
Install `kubectl`: https://kubernetes.io/docs/tasks/tools/install-kubectl-linux/
Install AWS CLI: https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2-linux.html

2. Create a new EKS cluster
`eksctl create cluster --name mjlmonitoring --region us-east-1`

3. Get access to EKS
`aws eks --region region update-kubeconfig --name cluster_name`

4. IAM Policy needed:
`CloudWatchAgentServerPolicy`

4. Run the code in `containerinsights.sh`

5. Clean environment
`eksctl delete cluster --name mjlmonitoring --region us-east-1`