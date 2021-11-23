# This folder contains the tutorials to connect to Cloud SQL instances

_To run the commands as written, you should create the following var envs:_

```
$ export SERVICE_ACCOUNT=<YOUR SERVICE ACCOUNT NAME>
$ export GCP_PROJECT=<YOUR GCP PROJECT ID>
$ export MYSQL_INSTANCE=<YOUR MYSQL INSTANCE NAME>
$ export POSTGRESQL_INSTANCE=<YOUR POSTGRESQL INSTANCE NAME>
$ export SQL_INSTANCE=<YOUR SQL INSTANCE NAME>
$ export REGION=<YOUR DESIRED REGION>
```

_For each one, you need a service account, you can create and download it with the following commands:_

```
$ gcloud iam service-accounts create $SERVICE_ACCOUNT
$ gcloud projects add-iam-policy-binding $GCP_PROJECT --member="serviceAccount:$SERVICE_ACCOUNT@$GCP_PROJECT.iam.gserviceaccount.com" --role="roles/cloudsql.client"
$ gcloud iam service-accounts keys create credentials.json --iam-account=$SERVICE_ACCOUNT@$GCP_PROJECT.iam.gserviceaccount.com
```

## [MySQL Tutorial](https://github.com/DSC-ESCOM-IPN/Cloud-Computing-Course/blob/main/SQL/files/MySQL_README.md)

## [PostgreSQL Tutorial](https://github.com/DSC-ESCOM-IPN/Cloud-Computing-Course/blob/main/SQL/files/PostgreSQL_README.md)

## [SQL Server Tutorial](https://github.com/DSC-ESCOM-IPN/Cloud-Computing-Course/blob/main/SQL/files/SQL_Server_README.md)