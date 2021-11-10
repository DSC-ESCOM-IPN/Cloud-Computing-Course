#!/bin/bash

echo "Deleting vm-1..."
gcloud compute instances delete vm-1 --zone=us-central1-a

echo "Deleting vm-1..."
gcloud compute instances delete vm-2 --zone=us-central1-c

echo "Deleting vm-1..."
gcloud compute instances delete vm-3 --zone=us-central1-a