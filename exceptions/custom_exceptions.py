class NotAFileError(Exception):
    """
    Custom exception class to represent the error when an expected file is not a file but a directory.

    Args:
        path (str): The path that is a directory instead of a file.

    Attributes:
        message (str): A user-friendly error message indicating that the given path is a directory, not a file.

    Example:
        >>> try:
        ...     raise NotAFileError('/path/to/directory')
        ... except NotAFileError as e:
        ...     print(e)
        "'/path/to/directory' is a directory, not a file."
    """

    def __init__(self, path):
        super().__init__(f"'{path}' is a directory, not a file.")


class BadFormatError(Exception):
    """
    Custom exception class to represent the error when a file does not have the expected .pdf format.

    Args:
        file_key (str): The filename or key of the file that does not match the .pdf format.

    Attributes:
        message (str): A user-friendly error message indicating that the given file does not have a .pdf format.

    Example:
        >>> try:
        ...     raise BadFormatError('document.txt')
        ... except BadFormatError as e:
        ...     print(e)
        "'document.txt' is not a .pdf file."
    """

    def __init__(self, file_key):
        super().__init__(f"'{file_key}' is not a .pdf file.")


class FileNameError(Exception):
    """
    Custom exception class to represent the error when a file name does not adhere to a specific naming rule.

    Args:
        file_key (str): The filename or key of the file that violates the naming rule.

    Attributes:
        message (str): A user-friendly error message indicating that the given file name does not follow the naming rule.

    Example:
        >>> try:
        ...     raise FileNameError('illegal_file_name')
        ... except FileNameError as e:
        ...     print(e)
        "'illegal_file_name' does not abide the naming rule."
    """

    def __init__(self, file_key):
        super().__init__(f"'{file_key}' does not abide the naming rule.")
