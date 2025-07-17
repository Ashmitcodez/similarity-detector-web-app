def RightMin(values):
    """
    Find the minimum value in a list and its rightmost index.

    Args:
        values (list): A list of comparable elements.

    Returns:
        tuple: (min_value, rightmost_index)
    """
    if not values:
        raise ValueError("Input list is empty.")

    min_value = min(values)
    rightmost_index = -1

    for i in range(len(values)):
        if values[i] == min_value:
            rightmost_index = i

    return (min_value, rightmost_index)
