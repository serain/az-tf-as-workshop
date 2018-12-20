## 06 - Terraform VNET

### Terraform TL;DR

When declaring a new resource, we specify the RESOURCE_TYPE and the RESOURCE_NAME and then pass the relevant properties:

```
resource RESOURCE_GROUP RESOURCE_NAME {
    PROPERTY = "VALUE"
}
```

### Define RG and VNET configuration

In `modules/vnet/main.tf`, define the StoreIt Resource Group and VNET:

```
resource "azurerm_resource_group" "rg" {
  name                = "storeit-rg"
  location            = "uksouth"
}

resource "azurerm_virtual_network" "vnet" {
  name                = "vnet"
  location            = "uksouth"
  address_space       = ["10.1.0.0/16"]
  resource_group_name = "${azurerm_resource_group.rg.name}"
}
```

Note that we're using Terraform's variable notation to fetch the name of the Resource Group in the second block, good practice.

The format for using a variable from another resource is:

```
${RESOURCE_TYPE.RESOURCE_NAME.PROPERTY}
```

We could also have user defined values from a `variables.tf` and `*.tfvars` files. We'll see that later.

### Call the VNET module

We've defined stuff in the `vnet` module but this modeule still needs to be called from the entrypoint `main.tf`.

In `environment/main.tf` add:

```
module "vnet" {
  source             = "../modules/vnet"
}
```

### Build

From the root of your Terraform project run:

```
$ terraform init -var-file=environment/env.tfvars environment/
```

`init` will download the Azure Resource Manager plugin (we've defined this in `environment/variables.tf`) and parse the modules. Then:

```
$ terraform plan -var-file=environment/env.tfvars environment/
````

`plan` will show you the actions Terraform would perform to make your remote resources match your local definitions.

Terraform is idempotent: if you run it multiple times with the same configuration, it will not perform changes to your remote resources. Terraform `plan` will therefor show you any discrepencies between what's defined in your files and what's on Azure.

If you're happy with what `plan` shows you, you can apply the changes:

```
$ terraform apply -var-file=environment/env.tfvars -auto-approve environment/
```

Use the Azure panel to confirm that your resources have been created as you would expect.

