import boto3


def replicate_object(source_bucket, object_key, username, destination_bucket):
    """
    Replicate an object from a source Amazon S3 bucket to a destination Amazon S3 bucket,
    placing it in a subdirectory named after the specified username.

    Args:
        source_bucket (str): The name of the source S3 bucket.
        object_key (str): The key (path) of the object to be replicated within the source bucket.
        username (str): The username used to create a subdirectory within the destination bucket.
        destination_bucket (str): The name of the destination S3 bucket.

    Returns:
        None

    Raises:
        botocore.exceptions.ParamValidationError: If any of the provided parameters are invalid.
        botocore.exceptions.EndpointConnectionError: If there is an issue connecting to the AWS endpoint.
        botocore.exceptions.ClientError: If any other S3-specific errors occur during replication.

    Example:
        >>> replicate_object('my-source-bucket', 'path/to/source/object.pdf', 'john_doe', 'my-destination-bucket')

    This function replicates the object located at 'path/to/source/object.pdf' within the 'my-source-bucket' to the
    'john_doe' subdirectory of 'my-destination-bucket'.

    Note:
        - The function uses the Boto3 library to interact with Amazon S3.
        - The 'source_bucket' and 'destination_bucket' parameters should be the names of the S3 buckets.
        - The 'object_key' should be the path to the object within the source bucket.
        - The 'username' parameter is used to create a subdirectory within the destination bucket, making it easier
          to organize replicated objects by user.
    """

    s3 = boto3.client('s3')
    s3.copy_object(
        CopySource={'Bucket': source_bucket, 'Key': object_key},
        Bucket=destination_bucket,
        Key=username + '/' + object_key
    )