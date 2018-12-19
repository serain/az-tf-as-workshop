## 05 - Terraform Setup

### Installation

Download Terraform from: https://www.terraform.io/downloads.html

```
$ unzip terraform_0.11.11_linux_amd64.zip
$ sudo mv terraform /usr/local/bin/
$ terraform --version
Terraform v0.11.11
```

### Create Directory Structure

Use the `tf-boilerplate` directory as a template for your Terraform project.

### Service Account for Azure

First take note of your `subscription_id` from:

```
$ az account list
```

Then create a Service Principal (tl;dr service account):

```
$ az ad sp create-for-rbac --role="Contributor" --scopes="/subscriptions/SUBSCRIPTION_ID"
```

This will output several values:

* `appId` is our Terraform `client_id`
* `password` is our Terraform `client_secret`
* `tenant` is our Terraform `tenant_id`

Use these values to populate your `env.tfvars`.
