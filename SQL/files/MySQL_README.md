# Working with MySQL instances in GCP

## Create instance

_To start with this, you have to make a cloud SQL instance in GCP, you can use the [console](https://console.cloud.google.com/sql/instances/create;engine=MySQL), if you get an error with this link just select your project and it should work_

_If you want to create it by cli, you should run:_

```
gcloud sql instances create $MYSQL_INSTANCE --database-version=MYSQL_5_7 --region=REGION
```

_Now you should set the instance password with the following command:_

```
gcloud sql users set-password root --host=% --instance $MYSQL_INSTANCE --password <YOUR PASSWORD>
```

## Connect to instance

_To connect to the instance you should use the proxy located in the [proxies folder](https://github.com/DSC-ESCOM-IPN/Cloud-Computing-Course/blob/main/SQL/proxies/), according to your OS_

_In that way you can bind your gcp instance as if you were running it locally, this by running:_

```
./cloud_sql_proxy_<YOUR OS> -instances=$GCP_PROJECT:$REGION:$MYSQL_INSTANCE=tcp:3306 -credential_file=../files/credentials.json
```

_Remember you need a service account, you can see the creation of it in the [main readme](https://github.com/DSC-ESCOM-IPN/Cloud-Computing-Course/blob/main/SQL/README.md)_

_Now you should be able to connect to your instance by anny client, we'll use the CLI as example:_

```
mysql -u root -p --host 127.0.0.1
```

_When asked enter your password and now, you are in_


## Test a script

_Here you have a [scrpit](https://github.com/DSC-ESCOM-IPN/Cloud-Computing-Course/blob/main/SQL/files/instance_test.sql) to test everything is running well, to use it you can run:_

```
mysql -u root -p --host 127.0.0.1 < instance_test.sql
```