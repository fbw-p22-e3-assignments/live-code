from google.cloud import storage 

client = storage.Client()

# Create a new storage bucket
new_bucket = client.create_bucket('python-bugs-storage-1') # Bucket name should be GLOBALLY UNIQUE

# Get an existing bucket
#existing_bucket = client.get_bucket('python-bugs-storage-1')

#Create a blob(file) to be uploaded
new_blob = new_bucket.blob('test-folder/manage.py')

# Upload the file
new_blob.upload_from_filename(filename='manage.py')


