# Variables
variable "aws_access_key" {
  description = "AWS Access Key ID"
  type        = string
}
variable "aws_secret_key" {
  description = "AWS Secret Access Key"
  type        = string
}

# Configure the AWS provider
provider "aws" {
  region     = "ap-northeast-1"
  access_key = var.aws_access_key
  secret_key = var.aws_secret_key
}

# Main configuration
module "vpc" {
  source = "./modules/vpc"
  // Pass necessary variables here
}

module "compute" {
  source = "./modules/compute"
  vpc_id = module.vpc.vpc_id
}

module "security" {
  source = "./modules/security"
  // Define and pass required security configurations
}

module "s3" {
  source = "./modules/storage"
}

module "postgres" {
  source = "./modules/database"
  vpc_id = module.vpc.vpc_id
}

module "dynamo_db" {
  source = "./modules/database"
}

# Configuration for Terraform to use a remote backend for state storage
terraform {
  backend "s3" {
    bucket         = "media-storage-for-anki-like-app"
    key            = "state/terraform.tfstate"
    region         = "ap-northeast-1"
    dynamodb_table = "UserSessions"
    encrypt        = true
  }
}
