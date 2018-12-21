## 01 - Create VNET and Subnets

Get our StoreIt network diagram up on your screen so you know what we're doing.

>Make sure you always create all resources with the "Resource Manager" deployment model, and _not_ "Classic"

### Create the VNET and `mgmt` subnet

Under the `storeit-rg` click Add and type `Virtual Network`.

We'll call our VNET `vnet`, and make sure it's created under the `storeit-rg` Resource Group.

We'll leave the default address space of `10.1.0.0/16`. As a first subnet we'll create the `mgmt` subnet in the address range `10.1.10.0/24`.

### Create `front` and `back` subnets

Navigate to the `storeit-rg` Resource Group, click on the `vnet` and go to the `Subnets` on the left pane.

Create the `front` subnet in the address range `10.1.1.0/24` and the `back` subnet in the address range `10.1.2.0/24`.

We'll leave the Network Security Groups blank here.

### Create Network Security Groups

Network Security Groups (NSGs) are sort-of firewall rules. We're going to use them to limit the traffic that can hit our VMs.

>NSGs "cascade" to each VM if you apply to them a subnet. This means that the NSG is _not_ the rules that apply at a gateway (like a traditional firewall). Instead these rules are applied to each VM in the subnet individually.

Go to the `storeit-rg` RG, and click add. Search for "Network security group". Create three NSGs:

* `front-nsg`
* `back-nsg`
* `mgmt-nsg`

Make sure you create these resources in `storeit-rg`.

Go back to the `storeit-rg` and navigate to the `vnet` resource. Under "Subnets" attach each NSG to its respective subnet.

### Configure `mgmt-nsg`

We want to allow SSH into the management box from the internet. We also want SSH from the management box to other boxes.

Navigate to the `mgmt-nsg` NSG, then to "Inbound security rules". Create:

* Allow `Internet` from any TCP source port to `mgmt` subnet (`10.1.10.0/24`) on destination port 22 TCP. Call it `inbound-ssh` and set priority to `100`.
* Deny `VirtualNetwork` from `any` to `any` over `any` protocol. Call it `deny-vnet-inbound` and set priority to `110`.

>We overwrite Azure's default "any to any" on the internal vnet; if our gateway gets popped we don't want people being able to hit our mgmt box (which in turn would allow them to hit anything if popped).

>In a real scenario you may want to whitelist inbound SSH to your orgs IP range.

Under "Outbound security rules" create:

* Allow `mgmt` subnet to outbound port 22 TCP to `VirtualNetwork`. Call it `outbound-ssh` and set priority to `100`.
* Deny all other `VirtualNetwork` outbound (priority `110`)

These rules will ensure that the boxes in the `mgmt` subnet can SSH to any box in the VNET, but not vice-versa. It'll also restrict inbound to SSH service only, and only from the Internet.

### Configure `front-nsg`

Similarly, apply the following inbound rules to the `front-nsg`:

* Allow 80 TCP inbound from Internet to `front` subnet (`10.1.1.0/24`), prio: 100
* Allow 22 TCP inbound from `mgmt` (`10.1.10.0/24`), prio: 110
* Deny all `VirtualNetwork` inbound, prio: 120

Apply the following outbound rules to the `front-nsg`:

* Allow 3000 TCP outbound from `front` (`10.1.1.0/24`) to `back` subnet (`10.1.2.0/24`), prio: 100
* Deny all other `VirtualNetwork` outbound, prio: 110

### Configure `back-nsg`

Similarly, apply the following inbound rules to the `back-nsg`:

* Allow 3000 TCP inbound from `front` (`10.1.1.0/24`), prio 110
* Allow 22 TCP inbound from `mgmt` (`10.1.10.0/24`), prio: 110
* Deny all other `VirtualNetwork` inbound, prio: 120

Apply the following outbound rules to the `back-nsg`:

* Deny all `VirtualNetwork` outbound, prio: 110
