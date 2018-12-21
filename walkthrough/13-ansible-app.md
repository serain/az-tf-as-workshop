## 13 - Ansible App

### Install Python

We'll be using the `apt` keyword to install Python3-PIP:

```
- name: Install python3-pip
  apt:
    name: python3-pip
    update_cache: yes
```

### Clone StoreIt

There's a `git` keyword to conveniently clone from GitHub:

```
- name: Git clone StoreIt
  git:
    repo: 'https://github.com/serain/storeit.git'
    dest: /opt/storeit
```

### Python Dependencies

There's actually a `pip` keyword but I couldn't get it working last night and was too dead to debug. Instead, we'll introduce the `shell` keyword.

```
- name: Install Python dependencies
  shell: pip3 install -r /opt/storeit/requirements.txt
```

>`shell` is bad Ansible because it's not idempotent. The shell command will run everytime even if there are no changes needed.

### Run the App

We're going to use the `shell` keyword again to spin up our janky app. The redirection shenanigans are copy-pasted from Stack Overflow to use `nohup` 

```
- name: start simple http server in background
  shell: nohup /opt/storeit/app.py </dev/null >/dev/null 2>&1 &
  environment: "{{app_env}}"
```
