# Python code to interact with Cloud Storage

_Here we have a python code example to interact with cloud storage, to start you need to install the dependences with:_

```
pip install -r requirements.txt
```

Now to make the app work, you need to set 2 env vars, **GCP_PROJECT** and **GCP_BUCKET_NAME**, you can use the following comands:

```
export GCP_PROJECT=YOUR-GCP-PROJECT
export GCP_BUCKET_NAME=YOUR-GCP-BUCKET-NAME
```

_Now you need a service account, you can create and download it with the following commands:_

```
gcloud iam service-accounts create py-serviceaccount
gcloud projects add-iam-policy-binding YOUR-GCP-PROJECT --member="serviceAccount:py-serviceaccount@YOUR-GCP-PROJECT.iam.gserviceaccount.com" --role="roles/storage.admin"
gcloud iam service-accounts keys create credentials.json --iam-account=py-serviceaccount@YOUR-GCP-PROJECT.iam.gserviceaccount.com
```

_This service account have the storage admin role, so do not share it either use it in production, it is for development purposes only, check the roles in the [gcp page](https://cloud.google.com/iam/docs/understanding-roles#cloud-storage-roles)_

_Finally just run the app:_

```
python app.py
```