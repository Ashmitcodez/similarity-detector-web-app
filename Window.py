def Window(w: int, array: list):
    """
    Generate a list of sliding windows from a given array.

    Args:
        w (int): The size of each window. Must be a positive integer.
        array (list): The list/array to slice into windows.

    Returns:
        list: A list of sublists (windows). Each window is a contiguous slice of `array`.
              If w > len(array), a single window containing the entire array is returned.

    Example:
        >>> Window(3, [1, 2, 3, 4, 5])
        [[1, 2, 3], [2, 3, 4], [3, 4, 5]]
    """
    if not isinstance(w, int) or w <= 0:
        raise ValueError("Window size w must be a positive integer.")
    if not isinstance(array, (list, tuple)):
        raise TypeError("Array must be a list or tuple.")

    # If window size is greater than array length, return the array itself as one window
    if w > len(array):
        return [array]

    output = []
    for i in range(len(array) - w + 1):
        data = array[i:i + w]
        output.append(data)
    return output


# Example usage:
if __name__ == "__main__":
    print(Window(3, [3, 1, 4, 1, 5, 9, 2, 6, 5]))
