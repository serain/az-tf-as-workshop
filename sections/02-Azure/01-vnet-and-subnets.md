.left-column[
    ## Azure
### - Resource Groups
### - VNET & Subnets
]
.right-column[
* VNET defines the total address space for resources
* VNET can be split into subnets
]
???

---

.left-column[
    ## Azure
### - Resource Groups
### - VNET & Subnets
### - NSG
]
.right-column[
**Network Security Groups**

* NSGs are soft-of like firewalls.

* Define network rules applied to individual network interfaces or to a subnet.

]
???

---

.left-column[
    ## Azure
### - Resource Groups
### - VNET & Subnets
### - NSG
]
.right-column[
When applied to a subnet, **NSG rules apply to each resource in that subnet**:

* Define an NSG with that allows 80 inbound only

* Attach it to a subnet with 3 VMs

* *Each VM will allow inbound 80 only*! Even when talking to other VMs in the same subnet.

]
???

---