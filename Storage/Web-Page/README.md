# Web page example to deploy it in Google Cloud Storage

_To apply this example you need a domain, you can buy one in google domains or another provider, after buy it you should follow the [Domain ownership verification](https://cloud.google.com/storage/docs/domain-name-verification?authuser=1#verification) steps_

_Here we have a web page example taken from internet, so what we need to do is to copy the files to cloud storage, you can use the console or this command if you have the sdk:_

```
gsutil cp * gs://YOUR-BUCKET-NAME.YOUR-DOMAIN/
```

_If you don't have a bucket you can create it by running:_

```
gsutil mb gs://YOUR-BUCKET-NAME.YOUR-DOMAIN/
```

_Now you have to go to your domain provider panle and add a CNAME registry pointing to c.storage.googleapis.com_

```
YOUR-BUCKET-NAME.YOUR-DOMAIN        CNAME       c.storage.googleapis.com
```

_Finally in the cloud you should set the **Storage Object Viewer** bucket permission to **AllUsers** and editing the websiteconfiguration, setting your entrypoint and not found page (404)_

## Copyright and License

Copyright 2013-2021 Start Bootstrap LLC. Code released under the [MIT](https://github.com/StartBootstrap/startbootstrap-resume/blob/master/LICENSE) license.
