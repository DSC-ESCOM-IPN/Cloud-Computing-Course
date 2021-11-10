# Mount a basic lamp stack on a Debian VM 

## Pre-work 📋
* [Debian 10 VM running on GCP](https://console.cloud.google.com/compute/instances)

## Starting 🚀
_To install the lamp stack we prepared a simple shell script, so you just have to copy the file to the VM or clone the repository with the following command:_

```
$ git clone https://github.com/DSC-ESCOM-IPN/Cloud-Computing-Course.git
```

_After this, we need to add execution permission to the shell script by running:_

```
$ chmod +x lamp-debian.sh
```

**Remember to be located in the file path**

_Now you just have to run the script:_

```
$ ./lamp-debian.sh
```

_When this script finishes you'll have the apache server, php language and mariaDB installed_

## Configuration and tests 🔧

_A recommended configuration is the data base security, so you have to run the next command to configure root access, password, default dbs, users, etc._

```
$ sudo mysql_secure_installation
```

_After this you should be able to access to the db server:_

```
$ sudo mysql
```

_Something we recommend is mount a phpinfo page to be sure the php language is interpreted correctly, you can do that by running:_

```
$ sudo sh -c 'echo "<?php phpinfo(); ?>" > /var/www/html/phpinfo.php'
```

_To view this page you have to access to your server by opening in your browser the following address:_

```
http://[YOUR_EXTERNAL_IP_ADDRESS]/phpinfo.php
```

## Extra 📦

**Remember you can use systemctl to manage the services.**

_Apache service_

```

$ sudo systemctl [action] apache2
```

_MariaDB service_

```
$ sudo systemctl [action] mariadb
```

_Common actions: status, restart, start, stop, enable, disable_