import re
import string
import fitz  # PyMuPDF library
import nltk
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
from fuzzywuzzy import fuzz
import pycorrector  # Spell checking library

def clean_pdf_text(pdf_path):
    """Cleans and preprocesses text extracted from a PDF."""

    with fitz.open(pdf_path) as doc:
        text = ""
        for page in doc:
            text += page.get_text()

    # Spell checking
    text = pycorrector.correct(text)

    # Normalization
    text = text.lower()  # Convert to lowercase
    text = re.sub(r"[^a-z0-9\s]", "", text)  # Remove punctuation and special characters

    # Tokenization
    tokens = nltk.word_tokenize(text)

    # Stemming
    stemmer = PorterStemmer()
    stemmed_tokens = [stemmer.stem(token) for token in tokens]

    # Stop word removal
    stop_words = set(stopwords.words("english"))
    filtered_tokens = [token for token in stemmed_tokens if token not in stop_words]

    # Deduplication
    deduplicated_tokens = []
    seen_tokens = set()
    for token in filtered_tokens:
        if fuzz.ratio(token, seen_tokens) < 90:  # Adjust threshold as needed
            deduplicated_tokens.append(token)
            seen_tokens.add(token)

    # Join the cleaned tokens back into a string
    cleaned_text = " ".join(deduplicated_tokens)

    return cleaned_text

# Example usage:
cleaned_text = clean_pdf_text("path/to/your/pdf.pdf")
print(cleaned_text)
