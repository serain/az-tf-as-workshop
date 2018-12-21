## 11 - Ansible Overview

Copy the `as-boilerplate` to your working directory.

Similarly to Terraform, Ansible expects certain files and folder structure.

### Ansible Config

The `ansible.cfg` is a simple config file. We're using it to tell Ansible which file will contain the lists of hosts we want to operate on as well as some SSH parameters we want Ansible to use (remember, Ansible is just SSH). In our case `ansible.cfg` looks like this:

```
[defaults]
inventory = ./hosts

[ssh_connection]
ssh_args = '-F ssh_config'
```

Note that we tell Ansible to use a custom `ssh_config` defined below.

### SSH Configuration

We're using a custom SSH config, `ssh_config` for this project. Without diving into the details, the important bit of the configuration is that it specifies how to connect to our Jumpbox `jb` by name, and for every box that is not `jb` (`app` and `gw` in our case) how to connect to them (by proxying through `jb`).

Edit the SSH configuration to put your `jb` IP address under `HostName`

Remember you can get your jumpbox IP from `terraform output`.

Once this is configured, you can SSH into any box in your environment by specififying the configuration file:

```
$ ssh -F ssh_config app
$ ssh -F ssh_config gw
$ ssh -F ssh_config jb
```

Ansible will use it similarly.

### Hosts

Take a quick look at the `hosts` file. This is a list of the machines we want to perform actions on, broken down by group (just `front` and `back` for us, although you can get more exotic with advanced configs).

When we later tell Ansible we want to do stuff on the `front` group, it'll pull the list of hosts from this file. In our case there'll be the single host `gw` there.

### Main YAML

Similar to Terraform, there's a main "entrypoint" which we'll use to call Ansible "roles" (modules).

The `main.yml` says we'll want to apply the `nginx` role to the machines in the `front` group, and the `app` role to the machines in the `back` group.

>Note that for our simple case we could skip the use of a `hosts` file and just specify the machine names directly in the `main.yml`. We're just using groups of machines to demo the concept.

We're also defining a variable `app_env`, that is a dictionary of environment variables that our app requires to run. Set your Mongo connection URI here.

>Ansible has encrypted "vault" files for variables which would be a better way to do this.

The `become: true` tells ansible to become `root` when running those roles.

### Roles

Roles are broken down into a few folders. The `tasks` folder contains a `main.yml` that is the entrypoint. Note that we could call other tasks in a role's `main.yml` if we needed to further break down the structure (ie: for a larger project).

Note that the `nginx` role has a `files` folder. If we want to upload something in a task, such as a configuration file, this is the default folder name Ansible will look into.

### Test

Make sure you can connect to the boxes by running the playbook. Even with no tasks Ansible will gather information from the boxes it needs to connect to:

```
$ ansible-playbook main.yml
```
