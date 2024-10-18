## Create a new AWS profile

```bash
aws configure sso --profile minecraft 
```

## Install `uv`

```bash
brew install uv
```

## Install AWS CDK

Install `nvm` (like `pyenv` for `node`) and use it to install node version 22.

```bash
brew install nvm
nvm install 22

# globally set node to v22 (like `pyenv global 3.11`)
nvm alias default 22
# default -> 22 (-> v22.10.0)

node --version      
# v22.10.0

which node     
# /Users/eric/.nvm/versions/node/v22.10.0/bin/node
```

## Bootstrap the AWS account

```bash
AWS_ACCOUNT_ID=$(aws sts get-caller-identity --profile minecraft --query "Account" --output text)
AWS_REGION=us-west-2

uv run -- cdk bootstrap aws://$AWS_ACCOUNT_ID/$AWS_REGION --profile minecraft
```