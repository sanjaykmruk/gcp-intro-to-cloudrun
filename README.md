# GCP Cloud Run Service

This Python project is used for creating and deploying a Cloud Run Service using Cloud Build and Container Registry.

### Note:
* Before we begin ensure that you Google SDK Installed and configured, Cloud Build, Container Registry and Cloud Run services are enabled and you have the right privileges.
* The square brackets should be replaced with appropriate values.
* Run below command to get the project Id:

``` bash
gcloud config get-value project
```

## 1. Cloud Build through CLI

Execute the below command to trigger a cloud build step for creating and pushing the image to container registry.
``` bash
gcloud builds submit --tag eu.gcr.io/[PROJECT_ID]/cloudrun-hello
```

"eu.gcr.io": Its hostname and could be one of four options: gcr.io, us.gcr.io, eu.gcr.io, or asia.gcr.io. The docker image will be pushed to the specified host region.

Execute the below command to trigger a cloud build step deploy the image to Cloud Run.

``` bash
gcloud run deploy --image eu.gcr.io/[PROJECT_ID]/cloudrun-hello --platform managed
```

Note: If not already selected you might be prompted to select a region & others as:
* Select a region where Cloud Run is currently available
* provide a service name
* Select a random number between a range
* Whether we want to allow unauthenticated invocations? - enter "y"

## 2. Deploy through Cloud Build pipeline

We will use the "cloudbuild.yaml" to trigger a cloud build pipeline. Each step in the pipeline will trigger another step upon successful execution.

Execute command and observe the logs:

 ```bash
 gcloud builds submit
 ```

Should Trigger the cloud build pipeline and on successful deployment, we should be able to see the endpoints in the logs.

### Note:
The pipeline is creating a cloud run service deployment to allow public access. If in the case while accessing the URL you are getting forbidden or any access-related issue. Follow the path in Console and grant alluser/public access (for test purpose only).

Cloud Run > cloudrun-hello > PERMISSIONS > +ADD > allUsers (Select Member) > Cloud Run - Cloud Run Invoker
