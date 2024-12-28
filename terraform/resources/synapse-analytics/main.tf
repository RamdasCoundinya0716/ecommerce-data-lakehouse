# Storage Account for Data Lake Gen2
provider "azurerm" {
  features {}
  subscription_id = var.subscription_id
}

#creating a storage account for the Synapse workspace
resource "azurerm_storage_account" "datalake" {
  name                     = var.storage_account_name
  resource_group_name      = var.resource_group_name
  location                 = var.location
  account_tier             = "Standard"
  account_replication_type = "LRS"
  account_kind = "StorageV2"

  # Enable hierarchical namespace for Data Lake Gen2
  is_hns_enabled = true
}
resource "azurerm_storage_data_lake_gen2_filesystem" "default" {
  name               = "default"
  storage_account_id = azurerm_storage_account.datalake.id
}

resource "azurerm_synapse_workspace" "synapse" {
   name                = var.synapse_workspace_name
  resource_group_name = var.resource_group_name
  location            = var.location
  storage_data_lake_gen2_filesystem_id = azurerm_storage_data_lake_gen2_filesystem.default.id
  sql_administrator_login          = var.sql_admin_username
  sql_administrator_login_password = var.sql_admin_password
  identity {
    type = "SystemAssigned"
  }
}


resource "azurerm_synapse_sql_pool" "sql_pool" {
  name                = "sqlpool"
  synapse_workspace_id = azurerm_synapse_workspace.synapse.id
  sku_name            = "DW100c"
  storage_account_type = "GRS"
  create_mode          = "Default"
}

resource "azurerm_synapse_spark_pool" "spark_pool" {
name                 = "sparkpool"
  synapse_workspace_id = azurerm_synapse_workspace.synapse.id
  spark_version = 3.4
  node_size_family     = "MemoryOptimized"
  node_size            = "Small"
  auto_pause {
    delay_in_minutes = 10
  }
  auto_scale {
    max_node_count = 5
    min_node_count = 3
  }
}