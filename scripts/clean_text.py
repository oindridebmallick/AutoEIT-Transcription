import re

def clean_transcript(text):

    text = text.lower()

    fillers = ["uh", "um", "eh"]

    for f in fillers:
        text = re.sub(r"\b"+f+r"\b", "", text)

    text = re.sub(r"\s+", " ", text)

    return text.strip()