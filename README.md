# similarity-detector-web-app
https://similarity-detector.streamlit.app/ 

This project is an interactive Streamlit web app that detects and visualizes textual similarity between files. It is designed to help you compare programming code files (C, C++, Java, Python, MATLAB) or plain text files and quickly spot matching regions. It works similarly to a MOSS (Measure of similarity software).

# Multi‑Language Similarity Detector

## Project Overview
This web app compares **one main file** against **one or more other files** to find similar text or code.  
It is built with **Streamlit** and implements the **Winnowing algorithm** for fast and robust similarity detection.

### How it Works:
1. **Strips irrelevant parts** (like whitespace and comments) from each file.
2. **Breaks the text into k‑grams** and computes rolling hash values.
3. **Generates a fingerprint** of each file based on minimal hash values in windows.
4. **Compares fingerprints** to find common substrings.

The app then:
- Shows a **similarity score** between files.
- Displays both files side by side with **matched regions highlighted**.
- Uses **independent scrollable panels** for long content.
- Caches fingerprints in memory for faster repeated comparisons.


## Features
- Highlights matched substrings in side‑by‑side panels.
- Scroll through long text/code independently in each panel.
- Supports multiple programming languages:
  - `txt`, `c`, `c++`, `java`, `python`, `matlab`
- Automatically strips language‑specific comments.
- Adjustable matching parameters:
  - `k` (noise threshold)
  - `t` (guarantee threshold)
- Compare one main file against many others at once.
- Cached fingerprints for instant re‑comparisons.


## File Descriptions

| File | Description |
|------|-------------|
| **app.py** | Main Streamlit application. Handles the user interface, file uploads, parameter inputs, runs the similarity comparison, and displays results in scrollable panels with highlighted matches. |
| **StripString.py** | Contains logic to normalize input text by stripping whitespace and irrelevant characters before further processing. |
| **Kgram.py** | Generates k‑grams (substrings of length *k*) from the normalized text. |
| **HashList.py** | Converts each k‑gram into a rolling hash value for efficient comparison. |
| **hash31.py** | Implements the specific hash function (modular arithmetic with base 31) used for k‑gram hashing. |
| **Window.py** | Splits the hash list into overlapping windows based on the guarantee threshold (*t*) and prepares them for winnowing. |
| **RightMin.py** | Utility to select the rightmost minimal hash in a window (core step in winnowing). |
| **Fingerprint.py** | Core winnowing implementation. Uses the windows and `RightMin` to produce a set of fingerprints for a document. |
| **Winnow.py** | Orchestrates the winnowing process, may combine multiple steps (depending on your implementation). |
| **FindMatchPositions.py** | Compares two sets of fingerprints and determines positions in each file where matches occur. |
| **FindMatchIndices.py** | Helper to locate indices of matching fingerprints (low-level matching logic). |
| **SimilarityScore.py** | Calculates similarity percentages based on matched positions and total length. |
| **README.md** | This documentation file that explains the project, its usage, and its components. |



## Running the app Locally
1. Install Python 3.9+.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
3. Run the app:
   ```bash
   streamlit run app.py
4. Open the local URL provided 

---
## Support / Contact
If you have questions or improvements, feel free to open an issue or submit a pull request.
