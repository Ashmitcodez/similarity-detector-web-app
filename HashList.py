from hash31 import hash31

def HashList(input_array):
    """
    Convert a list of strings into their hash values using hash31.

    Args:
        input_array (list): A list of strings.

    Returns:
        list: A list of integer hash values corresponding to each string.

    Example:
        >>> HashList(["abc", "def"])
        [<hash1>, <hash2>]
    """
    output_array = []
    for item in input_array:
        ascii_values = [ord(c) for c in item]
        h = hash31(ascii_values)
        output_array.append(h)
    return output_array
