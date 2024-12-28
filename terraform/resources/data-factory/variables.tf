/*
These variables are used to define the values that will be used in the resources. 
They are passed using the -var option in the terraform plan and terraform apply commands. 
The values are defined in the terraform.tfvars file.
Example usage:
terraform plan \
  -var="data_factory_name=ecommercedatafactory" \
  -var="resource_group_name=ecommerce-datalakehouse-rg" \
  -var="location=East US"

terraform apply \
  -var="data_factory_name=ecommercedatafactory" \
  -var="resource_group_name=ecommerce-datalakehouse-rg" \
  -var="location=East US"

*/
#Location for the resources
variable "location" {
  description = "The Azure region where the resources will be created."
}

# Resource Group name
variable "resource_group_name" {
  description = "The name of the resource group."
}

# Azure subscription ID
variable "subscription_id" {
  description = "The Azure subscription ID."
}

# Storage Account name
variable "storage_account_name" {
  description = "The Azure region where the resources will be created."
}

# Data Factory name
variable "data-factory-name" {
  description = "The name of the Data Factory."
}