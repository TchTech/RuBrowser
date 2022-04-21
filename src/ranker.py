from rurank import ru_rank
from bs4 import BeautifulSoup
import requests

with open('query.txt', 'r') as f: #USE IT FOR ENCODING ERRORS!
    query = f.read()

with open("urls.txt", 'r') as links:

    splt_links = links.read().split("\n")

    for link in splt_links:

        if link.startswith('http'):

            page = requests.get(link)

            soup = BeautifulSoup(page.text, "html.parser")

            soup.prettify("utf-16")

            text = soup.get_text()

            if soup.find("title") != None:
                header = soup.find('title').string
            else:
                header = text[0:30]

            with open('text.txt', 'w', encoding='utf-16') as f:
                f.write(text)

            with open('text.txt', 'r', encoding='utf-16') as f:
                text = f.read()

            with open('ranks.txt', 'a') as rankf:
                indices = [index for index in range(len(text)) if text.startswith(query, index)]
                rankf.write(link)
                rankf.write('\n')
                rankf.write(str(ru_rank(query, text, header)+len(indices)))
                rankf.write('\n')
            print('ready')

with open("urls.txt", 'w') as file:
    file.write('')