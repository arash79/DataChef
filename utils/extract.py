def extract_meta_data(event):
    """
    Extracts metadata from an event,
    specifically an AWS Lambda event triggered by an S3 bucket event or a file transfer event.

    Args:
        event (dict): A dictionary representing the event object containing metadata.

    Returns:
        tuple: A tuple containing extracted metadata in the following order: (username, source_bucket, file_key).

    Raises:
        KeyError: If the expected keys are not found in the event dictionary.

    Example:
        >>> event = {
        ...     'Records': [
        ...         {
        ...             'userIdentity': {'principalId': 'arn:aws:iam::123456789012:role/service-role/lambda-role'},
        ...             's3': {
        ...                 'bucket': {'name': 'my-source-bucket'},
        ...                 'object': {'key': 'path/to/myfile.pdf'}
        ...             }
        ...         }
        ...     ]
        ... }
        >>> extract_meta_data(event)
        ('lambda-role', 'my-source-bucket', 'path/to/myfile.pdf')

    This function extracts metadata from an event object. It attempts to extract the 'username', 'source_bucket', and
    'file_key' from the event, assuming the event structure is compatible with AWS Lambda S3 and file transfer events.
    If the expected keys are not found, it falls back to an alternate structure that might contain the same information.
    """

    try:
        username = event['Records'][0]['userIdentity']['principalId']
        username = username.split(':')[2].split('.')[0]
        source_bucket = event['Records'][0]['s3']['bucket']['name']
        file_key = event['Records'][0]['s3']['object']['key']
    except KeyError:
        username = event['serviceMetadata']['transferDetails']['userName']
        source_bucket = event['fileLocation']['bucket']
        file_key = event['fileLocation']['key']

    return username, source_bucket, file_key