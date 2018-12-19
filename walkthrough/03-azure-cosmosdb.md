## 03 - Create CosmosDB

We're going to create a CosmosDB account for our app.

### Create

Add a resource and search for CosmosDB.

Select the `storeit-rg` Resource Group.

Set `storeit` as the Account Name.

For API, set `Azure Cosmos DB for MongoDB API`.

Under Network, set the `vnet` and `back` subnet.


### Get Connection URI

It will taker several minutes to create the CosmoDB account. Once it's done we can get our authentication URI with:

```
$ az cosmosdb list-connection-strings -g storeit-rg -n storeit
```

Take a note of the `connectionString`.
