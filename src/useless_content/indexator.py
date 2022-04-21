import re

def prepare_for_indexing(text):
    paragraphs = text.split('\n')
    result = []
    for p in paragraphs:
        result.append(re.findall(r"[\w']+", p.lower()))
    return result# change text to lower and remove punctuation marks.  