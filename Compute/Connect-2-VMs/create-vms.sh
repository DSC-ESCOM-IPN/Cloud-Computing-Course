#!/bin/bash

echo "Creating vm-1..."
gcloud compute instances create "vm-1" \
--zone "us-central1-a" \
--machine-type "e2-micro" \
--image-project "debian-cloud" \
--image "debian-10-buster-v20211105" \
--boot-disk-type "pd-standard" \
--tags "http-server" \
--subnet "default" \

echo "Creating vm-2..."
gcloud compute instances create vm-2 \
--zone=us-central1-c \
--machine-type=n1-standard-1 \
--image-project=centos-cloud \
--boot-disk-type=pd-standard \
--image=centos-8-v20211105 \
--subnet=default \

echo "Creating vm-3..."
gcloud compute instances create "vm-3" \
--zone "us-central1-a" \
--machine-type "e2-micro" \
--image-project "ubuntu-os-cloud" \
--image "ubuntu-minimal-2110-impish-v20211014" \
--boot-disk-type "pd-standard" \
--subnet "default" \