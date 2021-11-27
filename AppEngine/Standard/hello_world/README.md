# Python hello_world sample for Google App Engine Standard Environment

This sample demonstrates how to deploy a hello world app on [Google App Engine Standard Environment](https://cloud.google.com/appengine).

## Running locally

To run locally, it's recommended to activate a python virtual env, for this you can run:

```
virtualenv venv
source ./venv/bin/activate
```

Install the dependencies

```
pip install -r requirements.txt
```

Start the app

```
python app.py
```

## Deploying

1. Use the [Google Developers Console](https://console.developer.google.com)  to create a project/app id. (App id and project id are identical)

2. Setup the gcloud tool, if you haven't already.

   ```
   gcloud init
   ```

3. Use gcloud to deploy your app.

   ```
   gcloud app deploy
   ```

4. Congratulations!  Your application is now live at `your-app-id.appspot.com`

## Next steps

Once you have the app running in app engine, try to change something in the app, for example, add a new endpoint in [main.py](./main.py)

if you are not familiarized with flask you can use:

```
@app.route('/gdsc')
def hello2():
    return 'Hello World from the GDSC ESCOM IPN'
```

Use gcloud to update your app.

```
gcloud app deploy
```

Split the traffic to simulate how a new feature is tested in production

```
gcloud app services set-traffic [MY_SERVICE] \
  --splits [MY_VERSION1]=[VERSION1_WEIGHT],[MY_VERSION2]=[VERSION2_WEIGHT] \
  --split-by [IP_COOKIE_OR_RANDOM]
```