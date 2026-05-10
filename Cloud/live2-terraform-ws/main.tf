terraform {
    required_providers { // tells terraform to work with AWS
        aws = {
            source = "hashicorp/aws"
            version = "~> 4.0"
        }
    }

    required_version = ">= 1.2.0"
}

# Configure the AWS Provider to default to a given region 
provider "aws" {
    region = "us-east-1"
}

# Create a VPC 
resource "aws_s3_bucket" "s3_bucket" {
    bucket = "tcb-app-qa-jr-hisuby"
}

# Make bucket not public anymore 
resource "aws_s3_bucket_public_access_block" "s3_block" {
    bucket = aws_s3_bucket.s3_bucket.id

    block_public_acls = true
    block_public_policy = true
    ignore_public_acls = true
    
}