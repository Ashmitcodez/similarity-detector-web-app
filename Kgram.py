def Kgram(k, string):
    """
    Generate k-grams (substrings of length k) from a string.

    Args:
        k (int): Length of each k-gram.
        string (str): The input string.

    Returns:
        list: A list of k-length substrings.

    Example:
        >>> Kgram(3, "abcdef")
        ['abc', 'bcd', 'cde', 'def']
    """
    output_array = []
    if k > len(string):
        return [string]

    for i in range(len(string) - k + 1):
        output_array.append(string[i:i + k])
    return output_array
