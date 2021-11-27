# Python with cloudsql sample for Google App Engine Standard Environment

This sample demonstrates how to deploy an app on [Google App Engine Standard Environment](https://cloud.google.com/appengine) that is connected to a Cloud SQL instance.

## Preparing

As this example use a Cloud SQL instance it is recommended to follow the [SQL Lab](../../../SQL/README.md) first, and create the mysql instance.

You should open the [app.yaml](./app.yaml) file and enter the db credentials in the env vars:

```
  CLOUD_SQL_USERNAME: YOUR-USERNAME
  CLOUD_SQL_PASSWORD: YOUR-PASSWORD
  CLOUD_SQL_DATABASE_NAME: YOUR-DATABASE
  CLOUD_SQL_CONNECTION_NAME: YOUR-CONNECTION-NAME
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

Once you have the app running in app engine, try to change something in the app, for example, add a new endpoint to get the profile table info in [main.py](./main.py)

you can use this:
```
@app.route('/profiles')
def profiles():
    with cnx.cursor() as cursor:
        rows = []
        cursor.execute('SELECT * from profile;')
        data_rows = cursor.fetchall()
        print(data_rows)
        for data_row in data_rows:
            rows.append({
                'boleta': data_row[0],
                'LastName': data_row[1],
                'FirstName': data_row[2],
            })
    cnx.close()

    return json.dumps(rows)
```

don't forget to add:
```
import json
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