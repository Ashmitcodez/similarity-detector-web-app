def strip_string(input_string: str) -> str:
    """
    Preprocess a string by:
    - Converting to lowercase
    - Removing all spaces

    Args:
        input_string (str): The original string.

    Returns:
        str: Processed string.

    Example:
        >>> strip_string(" Hello World ")
        "helloworld"
    """
    if not isinstance(input_string, str):
        raise TypeError("input_string must be a string.")
    return input_string.lower().replace(" ", "")
