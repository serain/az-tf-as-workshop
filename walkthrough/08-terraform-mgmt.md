## 08 - Management Subnet

We'll move on and create the management subnet first, including the management NSG and jumpbox VM.

>Don't create your resources in `uksouth` on a free subscription. Amend where relevant below.


### Call the `sub-mgmt` module

From the `environment/main.tf`, call the `mgmt-sub` module by passing in the `vnet.rg` variable:

```
module "sub-mgmt" {
  source             = "../modules/sub-mgmt"
  rg                 = "${module.vnet.rg}"
}
```

Since we're using the `rg` variable in `sub-mgmt` we need to declare it in `modules/sub-mgmt/variables.tf`:

```
variable rg {}
```

### Create the `mgmt` subnet

We're going to create a subnet resource in the `vnet` previously created.

>Remember the syntax
>resource "RESOURCE_TYPE" "TERRAFORM_INTERNAL_RESOURCE_NAME" {
>  name = "ACTUAL_AZURE_NAME"
>}

```
resource "azurerm_subnet" "sub" {
  name                 = "mgmt"
  resource_group_name  = "${var.rg}"
  virtual_network_name = "vnet"
  address_prefix       = "10.1.10.0/24"
}
```

>We're using a variable for the `resource_group_name` created in the previous step, whereas we're hardcoding our `address_prefix` and `vnet` names. Hardcoding these in various places is obviously bad practice but we're doing this for simplicity. Ideally we'd use variables almost everywhere for easier maintenance.

### Create the `mgmt-nsg` Network Security Group

We're going to create the `mgmt-nsg` again. A template to get you started is below:

```
resource "azurerm_network_security_group" "nsg" {
  name                               = "mgmt-nsg"
  location                           = "uksouth"
  resource_group_name                = "${var.rg}"

  # ssh from internet
  security_rule {
    name                             = "ssh-inbound"
    priority                         = 100
    direction                        = "inbound"
    access                           = "allow"
    protocol                         = "tcp"
    source_port_range                = "*"
    destination_port_range           = "*"
    source_address_prefix            = "*"
    destination_address_prefix       = "*"
  }
} 
```

>You can use tags like `Internet` and `VirtualNetwork` in the `*_address_prefix`.

Refer to the rules in `01-azure-vnet` to populate the management rules.

### Associate the Subnet and the NSG

The following resource associates the subnet and the NSG together, referring to them by ID.

```
resource "azurerm_subnet_network_security_group_association" "nsg_association" {
  subnet_id                 = "${azurerm_subnet.sub.id}"
  network_security_group_id = "${azurerm_network_security_group.nsg.id}"
}
```

### Create Network Interface and Public IP

Our management VM is going to need a network interface, and a public IP.

```
resource "azurerm_public_ip" "pip" {
  name                               = "jb-pip"
  location                           = "uksouth"
  resource_group_name                = "${var.rg}"
  public_ip_address_allocation       = "static"
}

resource "azurerm_network_interface" "nic" {
  name                               = "jb-nic"
  location                           = "uksouth"
  resource_group_name                = "${var.rg}"

  ip_configuration {
    name                             = "jb-ip"
    subnet_id                        = "${azurerm_subnet.sub.id}"
    private_ip_address_allocation    = "dynamic"
    public_ip_address_id             = "${azurerm_public_ip.pip.id}"
  }
}
```

>Note again how we're referring to the subnet and public IP IDs.


### Output the Public IP

In `modules/sub-mgmt/outputs.tf` we want to pass the public IP generated above:

```
output "pip"   {
    value = "${azurerm_public_ip.pip.ip_address}"
}
```

To output it to the user at the end of the build process, we'll add it to the `environment/outputs.tf`:

```
output "jb-ip" {
    value = "${module.sub-mgmt.pip}"
}
```

### Test

It's probably a good time to test everything for any typos. We need to run `terraform init` again because we added a module:

```
$ terraform init environment/
$ terraform plan -var-file=./environment/env.tfvars environment/
```

This should flag up any typos or predictable issues.

### SSH User and Key Variables

For convenience we're going to define our SSH user and public key once in the main environment, and re-use it for each module.

In `environment/variables.tf` add:

```
variable vm_user {}
variable vm_ssh_key {}
```

In `environment/env.tfvars` add your variables:

```
vm_user = "storeit"
vm_ssh_key = "YOUR_PUBLIC_SSH_KEY"
```

In `environment/main.tf` pass the variables to your module:

```
module "sub-mgmt" {
  source             = "../modules/sub-mgmt"
  rg                 = "${module.vnet.rg}"
  vm_user            = "${var.vm_user}"
  vm_ssh_key         = "${var.vm_ssh_key}"
}
```

These still need to be declare in each modules' own `variables.tf`, for example by adding the following to `modules/sub-mgmt/variables.tf`:

```
vm_user = "storeit"
vm_ssh_key = "YOUR_PUBLIC_SSH_KEY"
```

We can now use these variables when creating our VM in the next bit.

### Create `jb` VM

Creating the VM is a big chunk of pretty self-explanatory configuration:

```
resource "azurerm_virtual_machine" "vm" {
  name                               = "jb"
  location                           = "uksouth"
  resource_group_name                = "${var.rg}"
  vm_size                            = "Standard_A1_v2"
  network_interface_ids              = [
    "${azurerm_network_interface.nic.id}"
  ]

  delete_os_disk_on_termination      = true
  delete_data_disks_on_termination   = true

  storage_image_reference {
    publisher                        = "Canonical"
    offer                            = "UbuntuServer"
    sku                              = "18.04-LTS"
    version                          = "latest"
  }

  # default os_disk
  storage_os_disk {
    name                             = "jb-dsk"
    caching                          = "ReadWrite"
    create_option                    = "FromImage"
    managed_disk_type                = "Standard_LRS"
  }

  os_profile {
    computer_name                    = "jb"
    admin_username                   = "${var.vm_user}"
  }

  os_profile_linux_config {
    disable_password_authentication  = true

    ssh_keys {
      path                           = "/home/${var.vm_user}/.ssh/authorized_keys"
      key_data                       = "${var.vm_ssh_key}"
    }
  }
}
```

### Pray and Deploy

```
$ terraform apply -var-file=./environment/env.tfvars -auto-approve environment/
```
