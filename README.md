# gcp-intro-to-cloudrun
Intro to GCP Cloud run with Python.

## Command to create a docker image in Google Registry
gcloud builds submit --tag gcr.io/{Replace-with-Project-Id}/py-hello-world  

#### Note:

Run command to get the project id :
`gcloud config get-value project`

## Command to Deploying the inmage to Cloud Run
gcloud run deploy --image gcr.io/{Replace-with-Project-Id}/py-hello-world --platform managed

Note: If not already selected the you might get an CLI alert to select an region & others as:
1. Select an region where Cloud Run is currently available
2. Select a random number between a range
3. Whether we want to allow unauthenticated invocations? - enter "y"