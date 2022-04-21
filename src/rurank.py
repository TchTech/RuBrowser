# from customscore import search_and_count <-- IMPORT YOUR FUNCTION
from bertscore import bert_score

# import asyncio <-- USE FOR PARALLEL FUNCTIONS

def ru_rank(query, text, header):

    text_to_search = header

    if(text.find(query)>-1):
        idx = text.find(query)
        text_to_search = text[max(idx-20, 0), min(len(text)-1, idx+20)]

    return bert_score(query, text_to_search) # ADD CUSTOM FUNCTIONS AS YOU WANT.