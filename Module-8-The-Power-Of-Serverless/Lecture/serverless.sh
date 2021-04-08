Install the Serverless framework
`npm install -g serverless`

Create a Serverless Lambda Function
`serverless create --template aws-python3 --name test --path test`

Add Python Serverless requirements
`npm install --save serverless-python-requirements`

Deploy Serverless
`serverless deploy`

Clean up environment
`serverless remove`