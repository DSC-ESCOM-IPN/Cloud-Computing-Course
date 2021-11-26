# Lab to connect 2 VM in different zones on GCP

## Pre-work 📋
* [Google cloud SDK](https://cloud.google.com/sdk/docs/install)

## Starting 🚀
_In this lab we'll use the gcloud cli tool to create the resources we need to connect 2 VMs in different zones on GCP,_


_First we need to select a zone where we want to connect our VMS, you can list all the avilable zones by running:_

```
gcloud compute zones list
```

_You can set you default zone with the following command:_

```
gcloud config set compute/zone [SELECTED_ZONE] 
```

_Now create at least 2 VMs, you can run this minimal command:_

```
gcloud compute instances create VM-NAME \
  --machine-type VM-MACHINE-TYPE \
  --image-project VM-IMAGE-PROJECT-NAME \
  --image VM-IMAGE-NAME \
  --subnet SUBNET-NAME
```

_If you didn't set a default zone you must add the zone flag:_

```
  --zone ZONE-NAME
```

### ping among the VMs

_You should ssh into your vm and be able to ping them with the command:_

```
ping VM-NAME
```

_If the vm is in another zone you should use the [dns instance name](https://cloud.google.com/compute/docs/internal-dns#view_instance_dns_name), you can get this name by running:_
```
curl "http://metadata.google.internal/computeMetadata/v1/instance/hostname" \
  -H "Metadata-Flavor: Google"
```

_Use that to ping the vm:_

```
ping VM_NAME.ZONE.c.PROJECT_ID.internal
```

## Conifgure ssh connection 🔧

_To connect to your VMs from third party ssh you have to generate a ssh ey on your HOST (the computer outside GCP), you can do it as follow:_

```
ssh-keygen -t rsa -f ~/.ssh/KEY-NAME -C USER
```

_This will generate 2 keys, the private (KEY-NAME) and the public(KEY-NAME).pub, you must upload the public key to the cloud and add it to your VM with the following command:_

```
gcloud compute instances add-metadata VM-NAME --metadata-from-file ssh-keys=PATH/TO/YOUR/PUB
```

_Now you can ssh from the HOST to the VM:_

```
ssh -i PATH/TO/YOUR/KEY USER@VM-EXTERNAL-IP
```

**The key you use here is the private one**

## Extra 📦

_To ensure you are connected to your vm instance, you can install a web server, for example._

```
sudo apt install nginx
```

_And change the main page with something you want:_

```
sudo nano /var/www/html/index.nginx-debian.html
```

**This commands are for a debian based distro**

## Troubleshooting 📦


_If you get a "remote host identification has changed" error when sshing, you have to delete the host auto generated key by running:_

```
ssh-keygen -R VM-EXTERNAL-IP
```

_If you get a "permission denied (publickey)" error, probably you have the OS login enabled, you must disable it:_

```
gcloud compute project-info add-metadata --metadata enable-oslogin=FALSE
```

_If his doesn't work, read the [documentation page](https://cloud.google.com/compute/docs/troubleshooting/troubleshooting-ssh)_