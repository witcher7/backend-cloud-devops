terraform {
  required_version = "~> 1.12.1"
  required_providers { # required providers are the providers that are used in the terraform configuration 
    aws = { # aws is the provider name
      source = "hashicorp/aws" # source is the provider source
      version = "~> 5.0" # version is the provider version, This really affects the terraform plan and apply
    }
    random = { # random is the provider name
      source = "hashicorp/random" # source is the provider source
      version = "~> 3.0" # version is the provider version, This really affects the terraform plan and apply
    }
  }
}

## provider block 
provider "aws" {
  region = "us-east-1"
  access_key = "AKIAIOSFODNN7EXAMPLE"
  secret_key = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"
  shared_credentials_files = ["~/.aws/credentials"]
  profile = "default"
}

## Whenever we run terraform init, it will download the required providers and create a lock file
## if we change the version of providers, it will update the lock file but we need to run terraform init again
## terraform init --upgrade will upgrade the providers to the latest version  
## terraform init -reconfigure will reconfigure the providers
## terraform init -force-copy will force copy the providers


## We can have multiple providers 
provider "aws" {
  region = "us-west-1"
  profile = "default"
  alias = "us-west-1" # we are giving alias to provider to differentiate between providers
}

resource "aws_vpc" "west-vpc" {
  cidr_block = "10.0.0.0/16"
  provider = aws.us-west-1
  tags = {
     "Name" = "us-west-1"
  }
}