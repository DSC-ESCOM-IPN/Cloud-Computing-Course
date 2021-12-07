#!/bin/bash

CLUSTER_NAME="gke-cluster"
GCP_ZONE="us-central1-a"
GCP_REGION="us-central1"
GCP_PROJECT=""

for arg in "$@"; do
    case $arg in
    -c | --cluster)
        CLUSTER_NAME="$2"
        shift
        shift
        ;;
    -z | --zone)
        GCP_ZONE="$2"
        shift
        shift
        ;;
    -r | --region)
        GCP_REGION="$2"
        shift
        shift
        ;;
    -p | --project)
        GCP_PROJECT="$2"
        shift
        shift
        ;;
    esac
done

echo "Getting GKE credentials for ${GCP_PROJECT}/${GCP_ZONE}/${CLUSTER_NAME}..."
gcloud container clusters get-credentials ${CLUSTER_NAME} --zone ${GCP_ZONE} --project ${GCP_PROJECT}

API_IMG_ID=$(gcloud container images list-tags us.gcr.io/${GCP_PROJECT}/api | grep latest | awk '{print $1}')
INSTANCE_CREDENTIALS_SECRET=$(kubectl get secrets | grep cloudsql-instance-credentials | awk '{print $1}')
DB_CREDENTIALS_SECRET=$(kubectl get secrets | grep cloudsql-db-credentials | awk '{print $1}')
GCR_SECRET=$(kubectl get secrets | grep gcr-secret | awk '{print $1}')
NAMESPACE=$(kubectl get namespace | grep dev-namespace)
IMG_PREFIX="us.gcr.io/${GCP_PROJECT}/"

set -e

if [[ -z $API_IMG_ID ]]; then
    echo "API image not found, building image..."
    docker build . -t ${IMG_PREFIX}api:v1.0 -t ${IMG_PREFIX}api:latest
    echo "Pulling API image..."
    docker push ${IMG_PREFIX}api --all-tags
fi

if [[ -z $NAMESPACE ]]; then
    echo "Creating dev-namespace namespace..."
    kubectl create namespace dev-namespace
fi

echo "Setting dev-namespace as current namespace..."
kubectl config set-context --current --namespace=dev-namespace

echo "Importing env variables from file..."
export $(cat .secrets/service-accounts.env)
export $(cat .secrets/credentials.env)
connection=$GCP_PROJECT:$GCP_REGION:$POSTGRESQL_INSTANCE

if [[ -z $INSTANCE_CREDENTIALS_SECRET ]]; then
    echo "Creating cloudsql-instance-credentials secret..."
    kubectl create secret generic cloudsql-instance-credentials \
        --from-file=credentials.json=.secrets/${SA_SQL_FILE}
fi

if [[ -z $DB_CREDENTIALS_SECRET ]]; then
    echo "Creating cloudsql-db-credentials secret..."
    kubectl create secret generic cloudsql-db-credentials \
        --from-literal=username=${username} --from-literal=password=${password} \
        --from-literal=connection=${connection} --from-literal=db=${db}
fi

if [[ -z $GCR_SECRET ]]; then
    echo "Creating gcr secret..."
    kubectl create secret docker-registry gcr-secret \
        --docker-server=us.gcr.io \
        --docker-username=_json_key \
        --docker-password="$(cat .secrets/${SA_GCR_FILE})" \
        --docker-email=${SA_GCR_EMAIL}
fi

echo "Setting up API Deployment and Service..."
kubectl create -f ./api.deployment.yml --save-config
kubectl create -f ./api.service.yml --save-config

sleep 5
echo "Getting all the resources..."
kubectl get all
