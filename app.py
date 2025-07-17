import streamlit as st
import re
import io
import hashlib
from StripString import strip_string
from Kgram import Kgram
from HashList import HashList
from Fingerprint import Fingerprint
from FindMatchPositions import FindMatchPositions
from SimilarityScore import SimilarityScore


# COMMENT STRIPPING:
# Removes comments depending on language
def strip_comments(text: str, lang: str) -> str:
    """
    Remove language-specific comments from the given text.

    Parameters
    ----------
    text : str
        The original text content of the file.
    lang : str
        The language of the file (e.g., 'c', 'cpp', 'java', 'python', 'matlab').

    Returns
    -------
    str
        The text with comments removed according to the language rules.
    """
    lang = lang.lower()
    if lang in ["c", "cpp", "java"]:
        # remove /* */ blocks and // comments
        text = re.sub(r"/\*.*?\*/", "", text, flags=re.DOTALL)
        text = re.sub(r"//.*", "", text)
    elif lang == "python":
        text = re.sub(r"#.*", "", text)
    elif lang == "matlab":
        text = re.sub(r"%.*", "", text)
    return text

# PROCESS FILES:
# Process uploaded file bytes: strip comments, generate fingerprints
def process_bytes(file_bytes: bytes, lang: str, k: int, t: int):
    """
    Process a file's raw bytes to produce a cleaned string and a fingerprint.

    Steps performed:
    1. Decode bytes to UTF-8 text.
    2. Remove language-specific comments.
    3. Normalize the string by stripping whitespace and converting to lowercase.
    4. Generate k-grams, hash them, and compute a winnowing fingerprint.

    Parameters
    ----------
    file_bytes : bytes
        The raw bytes of the uploaded file.
    lang : str
        The programming language or 'txt' for plain text.
    k : int
        Noise threshold; size of each k-gram.
    t : int
        Guarantee threshold; determines window size.

    Returns
    -------
    tuple
        (fingerprint, cleaned_text)
        fingerprint : output of Fingerprint function
        cleaned_text : the normalized string with comments/whitespace removed
    """
    raw = file_bytes.decode('utf-8', errors='ignore')
    raw = strip_comments(raw, lang)
    cleaned = strip_string(raw)
    kgrams = Kgram(k, cleaned)
    hashes = HashList(kgrams)
    w = t - k + 1
    if w <= 0:
        # defensive check, should also be prevented by UI
        raise ValueError("Window size (t - k + 1) must be a positive integer.")
    fingerprint = Fingerprint(w, hashes)  # correct call per Fingerprint.py
    return fingerprint, cleaned

# CACHE SETUP:
cache = {}  # in-memory cache to speed up repeated runs

def get_cache_key(file_bytes: bytes, lang: str, k: int, t: int) -> str:
    """
    Generate a unique cache key based on file content and parameters.

    Parameters
    ----------
    file_bytes : bytes
        Raw file content.
    lang : str
        File language.
    k : int
        Noise threshold.
    t : int
        Guarantee threshold.

    Returns
    -------
    str
        SHA-256 hash string representing a unique key for the file and parameters.
    """
    # Use file contents and parameters to generate a unique hash
    h = hashlib.sha256()
    h.update(file_bytes)
    h.update(lang.encode('utf-8'))
    h.update(str(k).encode('utf-8'))
    h.update(str(t).encode('utf-8'))
    return h.hexdigest()

def get_fingerprint(file_obj, lang: str, k: int, t: int):
    """
    Get or compute the fingerprint for a file-like object.

    This function checks the in-memory cache first; if the fingerprint for this
    file with the given parameters exists, it returns that. Otherwise, it processes
    the file and stores the result in the cache.

    Parameters
    ----------
    file_obj : file-like
        File-like object returned by Streamlit's uploader.
    lang : str
        File language.
    k : int
        Noise threshold.
    t : int
        Guarantee threshold.

    Returns
    -------
    tuple
        (fingerprint, cleaned_text)
    """
    
    file_bytes = file_obj.read()
    key = get_cache_key(file_bytes, lang, k, t)
    if key in cache:
        return cache[key]
    else:
        fp, cleaned = process_bytes(file_bytes, lang, k, t)
        cache[key] = (fp, cleaned)
        return fp, cleaned

# HIGHLIGHT MATCHES:
# Highlight matched positions in the text based on fingerprint matches
def highlight_matches(text: str, match_positions, k):
    """
    Highlight matching regions in a text string using HTML <mark> tags.
    Safely escapes special characters (<, >, &) so they don't break HTML rendering.

    Parameters
    ----------
    text : str
        The cleaned text to highlight.
    match_positions : list
        A list of starting indices (1-based) where matches occur.
    k : int
        The length of each match.

    Returns
    -------
    str
        HTML-formatted string with <mark> tags around matched characters.
    """
    matched = set()
    for start in match_positions:
        for i in range(k):
            pos = start - 1 + i
            if pos < len(text):
                matched.add(pos)

    highlighted = ""
    for i, ch in enumerate(text):
        safe_char = html.escape(ch)  # escape special HTML chars
        if i in matched:
            highlighted += f"<mark>{safe_char}</mark>"
        else:
            highlighted += safe_char
    return highlighted
    
# UI SETUP:
# Set a consistent font for clarity
st.markdown(
    """
    <style>
    html, body, [class*="css"] {
        font-family: 'Arial', sans-serif;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("Multi‑Language Similarity Detector")
st.markdown("""
## Project Overview

This app compares **one main file** against **one or more other files** to find similar text/code.

It uses the **Winnowing** algorithm, which works as follows:

1. **Strips irrelevant parts** (like whitespace and comments).
2. **Breaks text into k-grams** and computes rolling hash values.
3. **Creates a fingerprint** of the file based on minimal hash values in windows.
4. **Compares fingerprints** to find common substrings.

The app displays:
- A **similarity score** between the files.
- Highlighted matching regions in **independent scrollable panels** for easy inspection.

## Features
- Highlight matched substrings
- Side‑by‑side comparison
- Compare multiple files at once
- Cached fingerprints for faster repeated comparisons
- Scrollable text panels for long content
""")

#FILE INPUT:
file1 = st.file_uploader("Upload main file", type=None)
lang1 = st.selectbox("Language of main file", ["txt", "c", "cpp", "java", "python", "matlab"])

file_list = st.file_uploader("Upload one or more files to compare against", type=None, accept_multiple_files=True)
langs = st.multiselect("Languages of comparison files (applies in order, defaults to txt)",
                       ["txt", "c", "cpp", "java", "python", "matlab"])

# ADVANCED PARAMETERS:
st.markdown("### Advanced Matching Parameters")
st.markdown("""
**Noise Threshold (k):**  
Controls how tolerant the similarity detector is to small edits or noise.  
- Smaller k = more sensitive to minor changes.  
- Larger k = more forgiving, ignoring small edits.

**Guarantee Threshold (t):**  
Sets the minimum size of a matching region that the algorithm will guarantee to detect.  
- Smaller t = detects shorter matches (may include insignificant ones).  
- Larger t = focuses only on longer, more meaningful matches.

**Important:** t must always be **greater than or equal to** k because the window size is calculated as `(t - k + 1)` and must be positive.
""")

col_k, col_t = st.columns(2)
with col_k:
    k_input = st.text_input("Noise Threshold (k)", value="5",
                            help="Integer. Controls sensitivity to small edits.")
with col_t:
    t_input = st.text_input("Guarantee Threshold (t)", value="8",
                            help="Integer. Must be >= k. Minimum guaranteed match length.")

# Validate k and t
try:
    k = int(k_input)
    t = int(t_input)
    if t < k:
        st.error("Guarantee Threshold (t) must be greater than or equal to Noise Threshold (k).")
        st.stop()
except ValueError:
    st.error("Please enter valid integer values for k and t.")
    st.stop()

# PROCESS AND COMPARE :
if file1 and file_list:
    file1_bytes = file1.read()
    fp1, cleaned1 = get_fingerprint(io.BytesIO(file1_bytes), lang1, k, t)

    for idx, compfile in enumerate(file_list):
        comp_bytes = compfile.read()
        lang = langs[idx] if idx < len(langs) else "txt"
        fp2, cleaned2 = get_fingerprint(io.BytesIO(comp_bytes), lang, k, t)

        m1, m2 = FindMatchPositions(fp1, fp2)
        score1 = SimilarityScore(m1, k, len(cleaned1))
        score2 = SimilarityScore(m2, k, len(cleaned2))
        overall = (score1 + score2) / 2

        st.subheader(f"Results comparing `{file1.name}` with `{compfile.name}`")
        st.metric("Similarity Score", f"{overall*100:.2f}%")

        # SCROLLABLE TEXT BOXES 
        # Create a reusable scrollable style
        scrollable_style = """
        <div style="
            white-space: pre-wrap;
            font-family: monospace;
            background-color: #f9f9f9;
            padding: 10px;
            border: 1px solid #ddd;
            border-radius: 5px;
            height: 400px;
            overflow-y: scroll;
        ">
        {content}
        """

        colA, colB = st.columns(2)
        with colA:
            st.markdown(f"**{file1.name} (main):**", unsafe_allow_html=True)
            st.markdown(
                scrollable_style.format(content=highlight_matches(cleaned1, m1, k)),
                unsafe_allow_html=True
            )
        with colB:
            st.markdown(f"**{compfile.name}:**", unsafe_allow_html=True)
            st.markdown(
                scrollable_style.format(content=highlight_matches(cleaned2, m2, k)),
                unsafe_allow_html=True
            )
        st.markdown("---")
