from StripString import strip_string
from Kgram import Kgram
from HashList import HashList
from Window import Window
from Fingerprint import Fingerprint

def winnow(filename: str, k: int, t: int):
    """
    Generate a fingerprint of a text file using the Winnowing algorithm.

    Args:
        filename (str): Path to the text file to process.
        k (int): Noise threshold (length of k-grams). Must be a positive integer.
        t (int): Guarantee threshold. Must be >= k.

    Returns:
        tuple: (fp, filelength)
            fp (list): Fingerprint values and their positions.
            filelength (int): Length of the processed string (after stripping whitespace and lowercasing).

    Raises:
        ValueError: If k or t are invalid.
        FileNotFoundError: If filename cannot be opened.
    """
    # Validate inputs
    if not isinstance(k, int) or k <= 0:
        raise ValueError("k must be a positive integer.")
    if not isinstance(t, int) or t < k:
        raise ValueError("t must be an integer greater than or equal to k.")

    # Calculate window size
    w = t - k + 1

    # Read file
    with open(filename, 'r', encoding='utf-8') as f:
        s = f.read()

    # Preprocess the string
    s = strip_string(s)
    filelength = len(s)

    # Create k-grams
    kgrams = Kgram(k, s)

    # Hash k-grams
    hashes = HashList(kgrams)

    # ✅ Pass the raw hashes into Fingerprint, not pre-windowed
    fp = Fingerprint(w, hashes)

    return fp, filelength
