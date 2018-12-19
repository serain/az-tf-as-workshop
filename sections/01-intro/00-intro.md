name: inverse
layout: true
class: center, middle, inverse
---
# Intro

---

.left-column[
    ## Intro
### - Our App
]
.right-column[
We're going to deploy StoreIt.

.center[https://github.com/serain/storeit]
]
???

---

.left-column[
    ## Intro
### - Our App
### - Our Env
]
.right-column[

]
???

---

.left-column[
    ## Intro
### - Our App
### - Our Env
### - IaaS, PaaS, SaaS
]
.right-column[
<img src="https://miro.medium.com/max/1000/1*0z9Pqwn7ujypQ396wleJ1Q.png" width="640px">
]
???

---

.left-column[
    ## Intro
### - Our App
### - Our Env
### - IaaS, PaaS, SaaS
### - Azure Panel
]
.right-column[
**Azure**

* Has some IaaS, PaaS, SaaS offerings
* Can spin up VMs, databases...
* Quick intro to the panel
* Clouds are complex, just abstract what you're not interested in or you get lost
]
???

---

.left-column[
    ## Intro
### - Our App
### - Our Env
### - IaaS, PaaS, SaaS
### - Azure Panel
### - Terraform
]
.right-column[
**Terraform**

* Define infrastructure as code
* Repeatable deployments
* Automated deployments
* CI/CD

Terraform interacts with the Azure REST API.

]
???

---

.left-column[
    ## Intro
### - Our App
### - Our Env
### - IaaS, PaaS, SaaS
### - Azure Panel
### - Terraform
### - Ansible
]
.right-column[
**Ansible**

* Automate interaction with VMs
* Create users
* Update machines
* Install dependencies
* ...

Ansible interacts with the VMs' SSH service (uses Python on both ends)
]
???
