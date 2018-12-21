## 12 - Ansible Nginx

We'll setup the gateway first. 

### Install nginx

Modify the `nginx/tasks/main.yml` main task to install `nginx`:

```
- name: Install nginx
  apt:
    name: nginx
    update_cache: yes
```

As you can see, Ansible has a built in function to handle an `apt` install. We can just specify the args for `apt` instead of specifying a full shell command.


### Configuration File

Under the `roles/nginx/files` create `nginx.conf`:

```
events {}

http {
    server {
        listen 80;

        location / {
            proxy_pass http://app:3000;
        }
    }
}
```

We can then upload this file to the `gw` by adding the following to the `nginx/tasks/main.yml`

```
- name: Upload nginx.conf
  copy:
    src: nginx.conf
    dest: /etc/nginx/nginx.conf
```

The `copy` keyword is used to copy _local_ file to a remote destination. By default Ansible will look for the file in the role's `files/` directory.

### Enable nginx

We'll use the `systemd` keyword to enable nginx with the new configuration. We add a parameter to force the service to bounce and reload the configuration.

```
- name: Enable and restart nginx
  systemd:
    name: nginx
    enabled: yes
    state: restarted
```

>The above is bad Ansible practice. Good Ansible should be _idempotent_, however the above command will bounce the service each time the Ansible playbook is run. Not a big deal but purists will not like it.
