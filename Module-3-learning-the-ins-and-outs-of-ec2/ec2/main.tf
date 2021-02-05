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

resource "aws_network_interface" "nic" {
  subnet_id   = var.subnet_id
  private_ips = var.ip_address

  tags = {
    Name = "webserver_network_interface"
  }
}

resource "aws_instance" "webserver" {
  ami                         = var.ami
  instance_type               = var.instance_type
  key_name                    = var.key_name

  network_interface {
    network_interface_id = aws_network_interface.nic.id
    device_index         = 0
  }

  tags = {
      "Name" = "cloudskillsweb"
  }
}
