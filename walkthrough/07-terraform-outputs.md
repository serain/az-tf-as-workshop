## 07 - Terraform Outputs

We'll learn how to work with Terraform outputs.

You have to see the chain of input/output a bit like this:

```
environment/main.tf
--- sends inputs to --->
modules/vnet/main.tf
--- sends outputs to --->
environment/outputs.tf
```

Outputs are used both to:

* output to the user at the end of the build process (for example a dynamically generated public IP)
* pass variables between modules

We're going to pass the Resource Group name from the `vnet` module up to the main entrypoint and output it to the user in the terminal.

Add the following to the `modules/vnet/outputs.tf`

```
output "rg" {
    value = "${azurerm_resource_group.rg.name}"
}
```

This will output a variable called `rg` from the `vnet` module to the main entrypoint.

In the main `environment/outputs.tf`, we will output another variable called `rg`, using the `rg` value passed up from the `vnet` module:

```
output "rg" {
    value = "${module.vnet.rg}"
}
```

Note that only outputs from the main `outputs.tf` are shown in the terminal at the end of the build.

If we run the build again we'll get an output in the terminal:

```
$ terraform apply -var-file=./environment/secrets.tfvars -auto-approve environment/
...
Outputs:

rg = storeit-rg-tf
```
