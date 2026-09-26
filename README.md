# AWS 3-Tier Cloud Migration Demo

Interview-ready demonstration of a web application architecture using **EC2, RDS, S3, VPC and IAM**. The repository contains a small Flask application and a CloudFormation stack.

## Architecture
Client -> EC2 web tier -> RDS database tier; EC2 also accesses S3 for object storage. VPC, subnet, routes and IAM role provide infrastructure and access control.

## Run locally
```bash
cd app
python -m venv .venv
# Windows: .venv\Scripts\activate
# Linux/macOS: source .venv/bin/activate
pip install -r requirements.txt
python app.py
```
Open `http://localhost:5000`.

## AWS deployment
1. Create an EC2 key pair.
2. Review `cloudformation/stack.yaml` and replace the AMI ID with a current Amazon Linux AMI for your AWS Region.
3. Deploy with CloudFormation and pass the key name and a database password.
4. SSH to the instance and run the application from the cloned repository.
5. Configure tighter security-group rules before any public demonstration.

> AWS resources can incur charges. Delete the CloudFormation stack after the interview demo.
