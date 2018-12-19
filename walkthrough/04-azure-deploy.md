## 04 - Manual Deploy

We're going to deploy StoreIt manually.

### Accessing VMs

We access our VMs through the Jumpbox VM:

```
$ ssh -o ProxyCommand="ssh -W %h:%p storeit@JUMPBOX_IP" storeit@app
```

TL;DR starts by creating an SSH connection to the jumpbox and tunnels the SSH connection to the `app`. Notice that Azure provides name resolution for VMs, as we can refer to `app` by name.

### `app`

#### Installing Components `app`

Start by SSH'ing into the `app` VM. Install `python3-pip` for managing Python dependencies, clone StoreIt from Github and install the dependencies:

```
$ ssh -o ProxyCommand="ssh -W %h:%p storeit@JUMPBOX_IP" storeit@app
$ sudo apt install python3-pip
$ git clone https://github.com/serain/storeit.git
$ cd storeit
$ pip3 install -r requirements.txt
```

#### Setting Connection String

The StoreIt app needs the CosmosDB database connection string we got from the previous step. This is set as an environment variable:

```
$ export STOREIT_MONGO_URI="COSMOSDB_CONNECTION_STRING"
```

#### Run the `app`

```
$ nohup ./app.py &
```

`nohup` ("no hangup") will keep the app running even if we kill the terminal. We use as well `&` to background.

Check the app is running properly:

```
$ curl localhost:3000
<html>
...
</html>
```

### `gw`

#### Installing nginx

SSH into the `gw` VM and install `nginx`:

```
$ ssh -o ProxyCommand="ssh -W %h:%p storeit@JUMPBOX_IP" storeit@gw
$ sudo apt install nginx
```

#### Configuring nginx

This configuration will listen for HTTP on 80 and proxy it to the `app` on 3000.

>Note that we're using Azure's name resolution by referring to the app VM as `app`.

```
$ sudo vim /etc/nginx/nginx.conf
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

#### Running nginx

```
$ sudo systemctl start nginx
```

Check you can access the app from your host, over the internet, by hitting the gateway:

```
$ curl 137.135.x.y

<html>
...
</html>
```
