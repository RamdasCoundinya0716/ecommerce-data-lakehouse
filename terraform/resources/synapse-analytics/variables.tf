/*
These variables are used to define the values that will be used in the resources. 
They are passed using the -var option in the terraform plan and terraform apply commands. 
The values are defined in the terraform.tfvars file.
Example usage:
terraform plan \
  -var="synapse_workspace_name=ecommercesynapseworkspace0716" \
  -var="sql_admin_password=IamBATMAN0716#" \
  -var="resource_group_name=ecommerce-datalakehouse-rg" \
  -var="location=East US" \
  -var="storage_account_name=synapsestorageacc0716"


terraform apply \
  -var="synapse_workspace_name=ecommercesynapseworkspace0716" \
  -var="sql_admin_password=IamBATMAN0716#" \
  -var="resource_group_name=ecommerce-datalakehouse-rg" \
  -var="location=East US" \
  -var="storage_account_name=synapsestorageacc0716"
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

# Synapse Analytics workspace name
variable "synapse_workspace_name" {
  description = "The name of the Synapse Analytics workspace."
  default = "synapseworkspace"
}

# SQL administrator username
variable "sql_admin_username" {
  description = "The SQL administrator username."
  default = "sqladmin"
}

# SQL administrator password
variable "sql_admin_password" {
  description = "The SQL administrator password."
}