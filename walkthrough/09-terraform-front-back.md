## 09 - Terraform `gw` and `app`

All the primitives we need for the `front` and `back` subnets, as well as the `gw` and `app` VMs were already introduced.

Starting with the `mgmt` Terraform configuration as base, the following elements need to be changed for the `front` and `back`:

* the subnet name and subnet range
* the nsg name
* the nsg rules
* the public ip name (**no public IP for the app box**)
* change the nic and ip_configuration name
* change the vm name, storage_os_disk name and os_profile name
* add the module to the main and change the output name in the main outputs

Make sure you can SSH to both `gw` and `app` through `jb` as before.
