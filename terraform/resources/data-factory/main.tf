# Storage Account for Data Lake Gen2
provider "azurerm" {
  features {}
  subscription_id = var.subscription_id
}


resource "azurerm_data_factory" "main" {
  name = var.data-factory-name
  location = var.location
  resource_group_name = var.resource_group_name
}