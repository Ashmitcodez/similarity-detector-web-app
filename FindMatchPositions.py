def FindMatchPositions(f1, f2):
    """
    Compare two fingerprints and find matching positions.

    Args:
        f1 (tuple): A 2-element structure [hash_list1, pos_list1].
        f2 (tuple): A 2-element structure [hash_list2, pos_list2].

    Returns:
        tuple: (p1, p2)
            p1 (list): Positions in f1 where a hash matches any in f2.
            p2 (list): Positions in f2 where a hash matches any in f1.

    Example:
        >>> f1 = [[11, 22, 33], [0, 1, 2]]
        >>> f2 = [[33, 44], [5, 6]]
        >>> FindMatchPositions(f1, f2)
        ([2], [0])
    """
    if not (isinstance(f1, (list, tuple)) and isinstance(f2, (list, tuple))):
        raise TypeError("f1 and f2 must be tuples or lists of [hashes, positions].")
    if len(f1) < 2 or len(f2) < 2:
        raise ValueError("Each fingerprint must have two components: [hashes, positions].")

    hash1, pos1 = f1
    hash2, pos2 = f2

    p1 = []
    p2 = []

    # Matching positions from f1 to f2
    for i in range(len(hash1)):
        for j in range(len(hash2)):
            if hash1[i] == hash2[j] and pos1[i] not in p1:
                p1.append(pos1[i])

    # Matching positions from f2 to f1
    for j in range(len(hash2)):
        for i in range(len(hash1)):
            if hash2[j] == hash1[i] and pos2[j] not in p2:
                p2.append(pos2[j])

    return p1, p2


# Example usage
if __name__ == "__main__":
    f1 = [[11, 22, 33], [0, 1, 2]]
    f2 = [[33, 44], [5, 6]]
    print(FindMatchPositions(f1, f2))
