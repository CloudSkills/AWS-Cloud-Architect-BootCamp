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

resource "aws_s3_bucket" "cloudskillsbucket" {
    bucket = var.bucket_name
    acl = var.acl

    tags = {
        Name = var.bucket_name
        Environment = "website"
    }
}