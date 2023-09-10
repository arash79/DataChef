import json
from utils import extract_meta_data, is_key_valid
from tools import replicate_object
from config import *


def lambda_handler(event, context):
    """
    AWS Lambda function handler that replicates an object from a source Amazon S3 bucket to a destination Amazon S3 bucket
    with proper metadata extraction, validation, and replication steps.

    Args:
        event (dict): The event object that triggered the Lambda function, typically containing metadata.
        context (object): The Lambda function runtime context.

    Returns:
        dict: A dictionary containing the HTTP response status code and a message indicating the execution status.

    Example:
        >>> event = {
        ...     # An example event object representing an S3 bucket event or file transfer event.
        ... }
        >>> lambda_handler(event, None)
        {
            'statusCode': 200,
            'body': 'Execution Finished!'
        }

    This Lambda function serves as an event-driven object replication mechanism. It extracts essential metadata from
    the provided 'event' object, validates the file key format, and replicates the object from a source S3 bucket
    to a destination S3 bucket using the 'replicate_object' function if the required conditions are met.

    Note:
        - The 'extract_meta_data' function is used to extract 'username', 'source_bucket', and 'file_key' from the event.
        - The 'is_key_valid' function is used to validate the naming convention and the format of the 'file_key'.
        - The 'replicate_object' function is responsible for copying the object with proper naming conventions.

    """

    username, source_bucket, file_key = extract_meta_data(event)
    destination_bucket = DESTINATION_BUCKET_NAME

    is_key_valid(file_key)  # checks the naming criteria
    replicate_object(source_bucket=source_bucket,
                     object_key=file_key,
                     username=username,
                     destination_bucket=destination_bucket)  # copies object from source to destination

    return {
        'statusCode': 200,
        'body': json.dumps('Execution Finished!')
    }
