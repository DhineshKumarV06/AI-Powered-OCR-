import re
from textblob import TextBlob


# -------------------------------------------------
# Clean extracted text
# -------------------------------------------------

def clean_text(text):

    text = re.sub(r'\s+', ' ', text)

    text = re.sub(r'[^A-Za-z0-9.,;:!?()\-\s]', '', text)

    return text.strip()


# -------------------------------------------------
# Basic spelling correction
# -------------------------------------------------

def correct_spelling(text):

    blob = TextBlob(text)

    corrected = blob.correct()

    return str(corrected)