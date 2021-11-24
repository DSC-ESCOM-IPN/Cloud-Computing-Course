# Simple API to connect with Cloud Storage

## Pre-work 📋
* [Cloud Storage instances](https://github.com/DSC-ESCOM-IPN/Cloud-Computing-Course/tree/main/SQL)

_First of all, you should edit the [init.sh](https://github.com/DSC-ESCOM-IPN/Cloud-Computing-Course/blob/main/SQL/api/init.sh) file with your project values for each env var, once you did that, you should set it in your local machine by running:_

```
$ source init.sh
```

_Now to start the api, it's recommended to activate a python virtual env, for this you can run:_
```
$ virtualenv venv
$ source ./venv/bin/activate
```

_Install the dependencies_

```
$ pip install -r requirements.txt
```

_Start the api_

```
$ python app.py
```