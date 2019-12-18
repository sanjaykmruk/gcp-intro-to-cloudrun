# gcp-intro-to-cloudrun
Intro to GCP Cloud run with Python.

# 1. Manual Creating a image and deploying it to Cloud Run
## Command to create a docker image in Google Registry
`gcloud builds submit --tag gcr.io/{Replace-with-Project-Id}/py-hello-world`

#### Note:

Run command to get the project id :
`gcloud config get-value project`

## Command for Deploying the image to Cloud Run
`gcloud run deploy --image gcr.io/{Replace-with-Project-Id}/py-hello-world --platform managed`

Note: If not already selected the you might get an CLI alert to select an region & others as:
1. Select an region where Cloud Run is currently available
2. Select a random number between a range
3. Whether we want to allow unauthenticated invocations? - enter "y"

# 2. Deploy through Cloud Build pipeline
Run command: `gcloud builds submit`

Should Trigger the cloud build & we can retrieve the endpoint exposed by the Cloud Run deployment.

Note: In order to access (For test purpose only) the API from browser you can grant access in google console by:
      Cloud Run > py-hello-world > PERMISSIONS > +ADD > allUsers (Select Member) > Cloud Run - Cloud Run Invoker
