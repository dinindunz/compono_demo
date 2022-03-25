
import boto3



s3 = boto3.resource('s3')
BUCKET = "din-test-123"

s3.Bucket(BUCKET).upload_file("diagrams/all_stacks.png", "all_stacks.png")