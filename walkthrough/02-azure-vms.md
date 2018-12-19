## 02 - Create VMs

We're going to create VMs for our `gw` (gateway), `app` and `jb` (jumpbox).

### For each VM

Add a resource, search for "Ubuntu 18.04".

#### Basics Tab

Make sure the resource is getting created in the `storeit-rg` Resource Group.

Name the VM (`gw`, `app` and `jb`).

Under the size, search for `A1_v2` (clear filters first).

For the admin account, call your user `storeit` and put your public SSH key.

#### Networking Tab

Set the VNET to the `storeit` `vnet`. Select the appropriate subnet:

* `gw` -> `front`
* `app` -> `back`
* `jb` -> `mgmt`

Don't create another NSG here.

**IMPORTANT** For the `gw` and `jb` box we will leave the `Public IP` field to the default, which will assign a public IP. You want to set `Public IP` to `None` for the `app` so it doesn't get exposed to the internet.

#### Create

You can leave the rest as default, just click `Review + create` and `Create`.

### Get Public IPs

The Azure CLI is often handier than the GUI when you're looking for specific things. It's worth getting familiar with it.

We're going to use the CLI to get the Public IPs for our `gw` and `jb`.

Install the Azure CLI on your host Ubuntu by following [these instructions](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli-apt?view=azure-cli-latest).

Then:

```
$ az login
$ az network public-ip list -g storeit-rg
```

Take note of the Jumpbox IP and Gateway IP
