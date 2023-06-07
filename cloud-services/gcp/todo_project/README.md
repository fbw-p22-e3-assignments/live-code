# Deploying to Google Cloud App Engine

## Setup APIs for backing services
App Engine - Main service that runs our application
Secret Manager - to stores secret keys, API Keys, passwords and any other sensitive values
Cloud SQL - Run a PostgreSQL server for all our databases.
Cloud Storage - To store static files (css, js, images)
Cloud Build - compiles our application into App Engine


## initialize App Engine

    ```
    gcloud app create
    ```

## Download SQL Auth Proxy to connect to Cloud SQL from our local machine

1. Authenticate and acquire credentials for the API:

    ```
    gcloud auth application-default login
    ```

2. Download and install the Cloud SQL Auth proxy to our local machine:

    ```
    #Linux 
    curl -o cloud-sql-proxy https://storage.googleapis.com/cloud-sql-connectors/cloud-sql-proxy/v2.3.0/cloud-sql-proxy.linux.amd64
    chmod +x cloud-sql-proxy

    #Windows
    follow this link https://storage.googleapis.com/cloud-sql-connectors/cloud-sql-proxy/v2.3.0/cloud-sql-proxy.x64.exe .Rename the file downloaded file to cloud-sql-proxy.exe.
    ```

## Create/ Instantiate the backing services

