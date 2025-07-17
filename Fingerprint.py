from Window import Window
from RightMin import RightMin

def Fingerprint(w, array):
    """
    Compute the fingerprint of the input sequence using the winnowing algorithm.

    Args:
        w (int): Window size.
        array (list): Sequence (e.g., list of hash values).

    Returns:
        list: [fingerprint_values, fingerprint_positions]
    """
    windows = Window(w, array)
    fingerprint_values = []
    fingerprint_positions = []

    for i, win in enumerate(windows):
        min_val, rel_pos = RightMin(win)
        abs_pos = i + rel_pos
        if abs_pos not in fingerprint_positions:
            fingerprint_values.append(min_val)
            fingerprint_positions.append(abs_pos)

    return [fingerprint_values, fingerprint_positions]


# Example usage
if __name__ == "__main__":
    print(Fingerprint(3, [5, 2, 4, 1, 3]))
