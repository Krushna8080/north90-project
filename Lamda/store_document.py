import boto3
from botocore.exceptions import NoCredentialsError
import io  # To handle byte streams

def lambda_handler(event, context):
    # S3 Configuration
    bucket_name = 'your-bucket-name'
    file_name = 'example.pdf'  # Replace with the actual file name
    file_content = b'Hello, this is the content of the file.'  # Replace with actual content as bytes

    # Initialize S3 Client
    s3 = boto3.client('s3', region_name='your-region')  # Replace 'your-region'

    try:
        # Convert bytes to a file-like object
        file_obj = io.BytesIO(file_content)

        # Upload to S3
        s3.upload_fileobj(file_obj, bucket_name, file_name)

        return {
            'statusCode': 200,
            'body': f'File {file_name} uploaded successfully to bucket {bucket_name}'
        }

    except NoCredentialsError:
        return {
            'statusCode': 500,
            'body': 'AWS credentials not found. Please configure them.'
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': str(e)
        }

# Test locally
if __name__ == "__main__":
    response = lambda_handler(None, None)
    print(response)
