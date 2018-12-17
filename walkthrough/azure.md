# Azure Walthrough

## Create a Resource Group

Azure resources are grouped into "Resource Groups". Generally you'll see one resource group per project, or per environment (dev, uat, prd etc.).

We're going to create a Resource Group for our StoreIt project.

* Go into the Resource Groups panel, click Add
* Call your new Resource Group `storeit-rg`

It always takes a few minutes to create resources, just wait and refresh.

## Create VMs

We're going to create VMs for our gateway, app and jumpbox.

In Resource Group click Add and create Ubuntu 18.04 LTS VMs.

Name them as follows:

* gw
* app
* jb

## 