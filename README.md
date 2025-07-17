# similarity-detector-web-app
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


## 📂 File Structure
`app.py` # Main Streamlit app
`StripString.py` # Helper for text normalization
`Kgram.py` # Helper for k‑gram generation
`HashList.py` # Helper for hashing k‑grams
`Fingerprint.py` # Helper for winnowing fingerprint
`FindMatchPositions.py` # Helper to find match positions
`SimilarityScore.py` # Helper to compute similarity score
`requirements.txt` # Dependencies for deployment
`README.md` # This file


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
