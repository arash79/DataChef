from exceptions import *
import re


def name_validity(file_name):
    """
    Validate the format of a file name.

    Args:
        file_name (str): The file name to be validated.

    Returns:
        bool: True if the file name matches the expected format (six digits), False otherwise.

    Example:
        >>> name_validity('202310')
        True

        >>> name_validity('abc123')
        False
    """

    return bool(re.match(r'^\d{6}$', file_name))


def is_key_valid(path_to_file):
    """
    Validate the format and name of a file.

    Args:
        path_to_file (str): The path to the file within an object storage system.

    Returns:
        bool: True if the file key is valid, False otherwise.

    Raises:
        NotAFileError: If the provided path_to_file does not represent a file (lacks a file format at the end).
        BadFormatError: If the file format is not 'pdf'.
        FileNameError: If the file name does not adhere to the expected format.

    Example:
        >>> is_key_valid('path/to/valid_file.pdf')
        False

        >>> is_key_valid('path/to/invalid_format.txt')
        False

        >>> is_key_valid('path/to/invalid_name/123456.pdf')
        True

    This function is used to validate file keys, used in Amazon S3 object storage systems.
    It checks whether the file key has the expected format, file format, and file name format. If any of these
    checks fail, an appropriate exception is raised.
    """

    match = re.search(r'[^/\\]+$', path_to_file)

    if match:

        file_key = match.group()
        file_name, file_format = file_key.split('.')

        if file_format == 'pdf':

            if name_validity(file_name):
                return True

            raise FileNameError(file_key)

        raise BadFormatError(file_key)

    raise NotAFileError(path_to_file)
