# Python websockets sample for Google App Engine Flexible Environment

This sample demonstrates how to use websockets on [Google App Engine Flexible Environment](https://cloud.google.com/appengine).

## Running locally

To run locally, you need to use gunicorn with the ``flask_socket`` worker:

```
gunicorn -b 127.0.0.1:8080 -k flask_sockets.worker main:app
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

Once you have the app running in app engine, try to change something in the app, for example, add a header in [index.html](./templates/index.html)

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