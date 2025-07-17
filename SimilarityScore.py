def SimilarityScore(matched_positions, k, total_length):
    """
    Compute similarity score based on matched positions.

    Args:
        matched_positions (list): List of starting indices (1-based) of matched substrings.
        k (int): Length of each match.
        total_length (int): Total length of original string.

    Returns:
        float: Similarity score between 0 and 1.

    Example:
        >>> SimilarityScore([1, 5], 3, 10)
        0.6
    """
    matched_chars = [0] * total_length
    for pos in matched_positions:
        for i in range(pos - 1, pos - 1 + k):
            if 0 <= i < total_length:
                matched_chars[i] = 1

    matched_sum = sum(matched_chars)
    return matched_sum / total_length if total_length > 0 else 0.0
