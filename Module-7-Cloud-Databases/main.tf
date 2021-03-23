# Run with the Terraform secrets:
# terraform plan --var-file=secrets.tfvars

terraform {
  required_providers {
    aws = {
      source = "hashicorp/aws"
    }
  }
}

provider "aws" {
  region = "us-east-1"
}

resource "aws_db_instance" "cloudskillsdb" {
  allocated_storage    = 20
  engine               = "mysql"
  engine_version       = "5.7"
  instance_class       = "db.t2.micro"
  name                 = var.db_name
  username             = "admin"
  password             = var.db_password
  parameter_group_name = "default.mysql5.7"
}