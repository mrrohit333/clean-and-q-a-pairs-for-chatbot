# PDF to Q&A Generator 📘➡️❓

This project contains two Python scripts that:
1. **Extract and clean text from a PDF file.**
2. **Automatically generate question-answer (Q&A) pairs from the cleaned text.**

---

## 🔧 Files

### `clean.py`
- **Purpose:** Extracts raw text from a PDF and cleans it.
- **Cleaning Includes:**
  - Removing extra whitespace and blank lines.
  - Removing standalone page numbers.
  - Removing repeated headers like "INCOME TAX LAW".
- **Output:** A cleaned text file (`cleaned_income_tax_law.txt`).

### `questions.py`
- **Purpose:** Parses the cleaned text and auto-generates Q&A pairs.
- **Q&A Heuristics:**
  - Treats lines in **ALL CAPS** or lines ending in `:` as questions.
  - All following lines until the next question are grouped as the answer.
- **Output:** A text file (`qa_pairs.txt`) with formatted Q&A sections.

---

## 📦 Requirements

Install the required libraries using pip:

```bash
pip install pymupdf
