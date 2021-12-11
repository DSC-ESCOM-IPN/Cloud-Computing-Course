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

INSTANCE_CREDENTIALS_SECRET=$(kubectl get secrets | grep cloudsql-instance-credentials | awk '{print $1}')
DB_CREDENTIALS_SECRET=$(kubectl get secrets | grep cloudsql-db-credentials | awk '{print $1}')
GCR_SECRET=$(kubectl get secrets | grep gcr-secret | awk '{print $1}')
NAMESPACE=$(kubectl get namespace | grep sam-prod-namespace)

set -e

echo "Getting GKE credentials for ${GCP_PROJECT}/${GCP_ZONE}/${CLUSTER_NAME}..."
gcloud container clusters get-credentials ${CLUSTER_NAME} --zone ${GCP_ZONE} --project ${GCP_PROJECT}

echo "Setting dev-namespace as current namespace..."
kubectl config set-context --current --namespace=dev-namespace

echo "Deleting all the resources..."
kubectl delete -f ./k8s/

if [[ -n $INSTANCE_CREDENTIALS_SECRET ]]; then
    echo "Deleting cloudsql-instance-credentials secret..."
    kubectl delete secret cloudsql-instance-credentials
fi

if [[ -n $DB_CREDENTIALS_SECRET ]]; then
    echo "Deleting cloudsql-db-credentials secret..."
    kubectl delete secret cloudsql-db-credentials
fi

if [[ -n $GCR_SECRET ]]; then
    echo "Deleting gcr secret..."
    kubectl delete secret gcr-secret
fi

if [[ -n $NAMESPACE ]]; then
    echo "Deleting dev-namespace namespace..."
    kubectl delete namespace dev-namespace
fi
