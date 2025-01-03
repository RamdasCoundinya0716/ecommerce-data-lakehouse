/*
These variables are used to define the values that will be used in the resources. 
They are passed using the -var option in the terraform plan and terraform apply commands. 
The values are defined in the terraform.tfvars file.
*/

#Location for the resources
variable "location" {
  default = "your-location"
  description = "The Azure region where the resources will be created."
}

# Resource Group name
variable "resource_group_name" {
  default = "your-resource-group-name"
  description = "The name of the resource group."
}
# Azure subscription ID
variable "subscription_id" {
  default = "your-subscription-id"
  description = "The Azure subscription ID."
}