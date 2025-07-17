def FindMatchIndices(Array1, Array2):
    """
    Find indices in Array1 where elements match any element in Array2.

    Args:
        Array1 (list): The first list of elements.
        Array2 (list): The second list of elements.

    Returns:
        list: A list of indices (from Array1) where Array1[i] == Array2[j] for some j.

    Notes:
        - This does not guarantee uniqueness of indices if duplicates appear in Array2.
        - Complexity is O(n*m) for n=len(Array1), m=len(Array2).

    Example:
        >>> FindMatchIndices([1,2,3,4], [2,4,6])
        [1, 3]
    """
    if not isinstance(Array1, list) or not isinstance(Array2, list):
        raise TypeError("Both inputs must be lists.")

    output = []
    for i in range(len(Array1)):
        for j in range(len(Array2)):
            if Array1[i] == Array2[j]:
                output.append(i)
    return output


# Example usage
if __name__ == "__main__":
    print(FindMatchIndices([1, 2, 3, 4], [2, 4, 6]))  # Output: [1, 3]
