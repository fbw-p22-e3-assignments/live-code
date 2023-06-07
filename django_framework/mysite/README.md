# Deploying to Google Cloud using APP Engine, Cloud SQL and Cloud Storage

## Download Cloud SQL AUth proxy to connect to Cloud SQL from the local machine

1. Authenticate and acquire credentials for the API:

    ```
    gcloud auth application-default login
    ```

2. Download and install the Cloud SQL Auth proxy to our local machine:

    ```
    # Linux
    curl -o cloud-sql-proxy https://storage.googleapis.com/cloud-sql-connectors/cloud-sql-proxy/v2.3.0/cloud-sql-proxy.linux.amd64

    #Windows
    Right-click https://storage.googleapis.com/cloud-sql-connectors/cloud-sql-proxy/v2.3.0/cloud-sql-proxy.x64.exe and select Save Link As to download the Cloud SQL Auth proxy. Rename the file to cloud-sql-proxy.exe.
    ```

    ```
    #Linux
    chmod +x cloud-sql-proxy
    ```

## Create backing services

## Set up a Cloud SQL for PostgreSQL instance

**Using gcloud**

1. Create a PostgreSQL instance

    ```
    gcloud sql instances create pb-blog-db-1 --project python-bugs-1 --database-version POSTGRES_13 --tier db-f1-micro --region europe-west1
    ```

2. Create a database within the SQL instance:

    ```
    gcloud sql databases create pb_gcp_blog --instance pb-blog-db-1
    ```

3. Create database user:

    ```
    gcloud sql users create blog_admin --instance pb-blog-db-1 --password blog1234
    ```


## Set up a Cloud Storage Bucket

1. Create a Cloud Storage Bucket

    ```
    gsutil mb -l europe-west1 gs://python-bugs-1_blog_files
    ```

## Store Secret Values in Secret Manager

Create a .env file :
    1. Database url
    2. Storage bucket name
    3. Secret key for Django

DATABASE_URL=postgres://DATABASE_USERNAME:DATABASE_PASSWORD@//cloudsql/PROJECT_ID:REGION:INSTANCE_NAME/DATABASE_NAME

GS_BUCKET_NAME=PROJECT-ID_BUCKET-NAME

SECRET_KEY = DJANGO_SECRET_KEY

## Configure environment variables in settings.py

1. in settings.py, import `environ` and `secretmanager`

    pip install environ

    ```
    import environ
    from google.cloud import secretmanager
    ```

    TODO: Update configuration process and code

## Configure .yaml file

Contains configuration info for deployment to the app engine environment

```
runtime: python
env: flex
entrypoint: gunicorn -b :$PORT mysite.wsgi

beta_settings:
    cloud_sql_instances: python-bugs-1:europe-west1:pb-blog-db-1

runtime_config:
    python_version: 3.10

```

## Store secret in Secret Manager

1. Create a new secret `django_settings`, with the values of the .env file:

    ```
    # Create a new secret
    gcloud secrets create django_settings --data-file .env

    # Update secret
    gcloud secrets versions add django_settings --data-file=.env --project=python-bugs-1
    ```

    

2. Confirm the craetion of the secret:

    ```
    gcloud secrets describe django_settings
    gcloud secrets versions access latest --secret django_settings
    ```

3. Delete the local .env file


## Configure access to the secret:

```
gcloud secrets add-iam-policy-binding django_settings --member serviceAccount:python-bugs-1@appspot.gserviceaccount.com --role roles/secretmanager.secretAccessor
```

## Run the app on our local machine

1. Start the Cloud SQL Auth proxy:

    ```
    #Linux
    ./cloud-sql-proxy python-bugs-1:europe-west1:pb-blog-db-1

    #Windows
    cloud-sql-proxy.exe python-bugs-1:europe-west1:pb-blog-db-1
    ```

2. Set the project ID locally:

    ```
    #Linux 
    export GOOGLE_CLOUD_PROJECT=python-bugs-1

    #Windows
    set GOOGLE_CLOUD_PROJECT=python-bugs-1

3. Set an environment variable to indicate we are using Cloud SQL Auth proxy:

    ```
    # Linux
    export USE_CLOUD_SQL_AUTH_PROXY=true

    # Windows
    set USE_CLOUD_SQL_AUTH_PROXY=true

4. Run django migrations and collect static files

    ```
    python manage.py makemigrations
    python manage.py migrate
    python manage.py collectstatic
    ```

5. Run server locally:

    ```
    python manage.py runserver
    ```

## Deploy to App Engine flexible environment

1. Upload to app engine:

    ```
    gcloud app deploy
    ```