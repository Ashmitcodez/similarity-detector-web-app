def hash31(values, hashsize=2**20):
    """
    Polynomial rolling hash function (base 31).

    Args:
        values (list): A list of integer values (e.g., ASCII codes).
        hashsize (int): Modulo to limit the hash size. Default = 2**20.

    Returns:
        int: The computed hash value.

    Example:
        >>> hash31([97, 98, 99])
        (some integer)
    """
    h = 0
    for v in values:
        h = (v + 31 * h) % hashsize
    return h

