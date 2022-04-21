import re

def clean_set(list):
    result_list = []
    for word in list:
        if len(word)>1:
            result_list.append(word)
    return set(result_list)

def prepare_text(text):

    return re.findall(r"[\w']+", text.lower()) # change text to lower and remove punctuation marks.  