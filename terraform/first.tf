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

## Whenever we run terraform init, it will download the required providers and create a lock file
## if we change the version of providers, it will update the lock file but we need to run terraform init again
## terraform init --upgrade will upgrade the providers to the latest version  
## terraform init -reconfigure will reconfigure the providers
## terraform init -force-copy will force copy the providers
