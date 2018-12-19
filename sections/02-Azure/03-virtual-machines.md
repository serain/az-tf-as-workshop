.left-column[
    ## Azure
### - Resource Groups
### - VNET & Subnets
### - NSG
### - CosmosDB
### - Virtual Machines
]
.right-column[
**VMs**
* VMs are an IaaS primitive in Azure

* Selection of base images on offer

* Create VMs using the GUI
]
???

---

.left-column[
    ## Azure
### - Resource Groups
### - VNET & Subnets
### - NSG
### - CosmosDB
### - Virtual Machines
]
.right-column[
**VMs**
* Let's create a VM and browse the output

* We're using Azure GUI with minimal changes

* Some things create for us:
   * network interface
   * disks
   * public IPs
]
???

---

.left-column[
    ## Azure
### - Resource Groups
### - VNET & Subnets
### - NSG
### - CosmosDB
### - Virtual Machines
]
.right-column[
* Demo creation of VM

* Demo fetching public IP
```
az network public-ip list -g storeit-rg
```

* Walkthrough 03
]
???

---