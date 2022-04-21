from textcleaner import prepare_text#, clean_set
# from indexator import prepare_for_indexing

def search_and_count(query, text):
    
    # splitted_text = prepare_text(text)
    # splitted_query = prepare_text(query)
    counter = 0

    pos = text.find(query)

    with open('text.txt','w', encoding="utf-16") as f:
        f.write(text)
    
    with open('text.txt', 'r', encoding="utf-16") as f:
        text = f.read()
    
    with open('query.txt', 'r') as f:
        query = f.read()

    while pos > -1:
        counter+=1
        text = text[pos+len(query):-1]
        pos = text.find(query)

    return counter