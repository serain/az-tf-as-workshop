## 10 - Terraform CosmosDB

You guessed it, more configuration.

### CosmosDB

We're going to add a CosmosDB account that can be accessed from the `back` subnet.

You'll need to adapt the name and locations in the below.

The following goes into the `back` module:

```
resource "azurerm_cosmosdb_account" "db" {
    name = "storeit-cosmosdb"
    location = "uksouth"
    resource_group_name = "${var.rg}"
    offer_type = "Standard"
    kind = "GlobalDocumentDB"

    enable_automatic_failover = true
    #is_virtual_network_filter_enabled = true

    consistency_policy {
        consistency_level = "BoundedStaleness"
        max_interval_in_seconds = 10
        max_staleness_prefix = 200
    }

    geo_location {
        location = "uksouth"
        failover_priority = 0
    }

    #virtual_network_rule {
    #    id = "${azurerm_subnet.sub.id}"
    #}
}
```

### Build

Rebuild the environment.

### Get your keys

Because I did this all last minute like a champ, this isn't the same CosmosDB we deployed yesterday (not default to MongoDB). No worries we just have to build our URI ourselves. Navigate to the CosmosDB account in the panel, go to the Keys tab and locate your PRIMARY_KEY. Then construct your URI and keep it somewhere:

```
$ mongo "mongodb://ACCOUNT_NAME:PRIMARY_KEY@ACCOUNT_NAME.documents.azure.com:10255/?ssl=true"
```
