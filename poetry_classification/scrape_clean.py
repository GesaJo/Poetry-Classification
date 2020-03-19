import requests
import re
from bs4 import BeautifulSoup


def clean_text_function(text):
    ''' function to clean text:
        replace Umlaute and delete noise'''

    Patterns = [('ä', 'ae'), ('ö', 'oe'), ('ü', 'ue'), ('ß', 'ss'),
                ('<.+?>', ' '), ('Aufnahme \d{4}', '!--!'), ('\\\xa0', '')]
    for to_replace, insert in Patterns:
        text = re.sub(to_replace, insert, text)

    return text


def scrape_texts_function(list_of_poets):
    ''' Get the links to all poems from the website and
        write the texts into a file.
        Input: list of poet-names,
        output: saves poems on disk.'''

    dict_poets = {}

    # make a list of all links to the poems of the poet
    for poet in list_of_poets:
        get_poems = requests.get(f'https://www.deutschelyrik.de/{poet}.html')
        link_list = BeautifulSoup(get_poems.text, 'html.parser')

        poems_list = []
        for link in link_list.find_all(attrs={'class': 'mod_navigation block',
                                              'id': 'snav2'})[0].find_all('a'):
            link_adress = link.get('href')

            if str(link_adress).endswith('.html'):
                poems_list.append(link_adress)

        # exception for poets with less than 5 poems on the website
        if len(poems_list) < 5:
            print(f'Sadly, there are not enough poems by {poet.title()} to make a prediction.')
            print('Please start again.')
            raise SystemExit(0)

        # get the texts and append them to a list
        one_poet_text = []
        for poem in poems_list:
            one_poem_text = []
            poem = requests.get('http://deutschelyrik.de/'+poem).text
            poem_text_parsed = BeautifulSoup(poem, 'html.parser')

            try:
                for k in range(len(poem_text_parsed.find_all(attrs={'class': 'ce_text last block'})[0].find_all('p'))):
                    one_p = (poem_text_parsed.find_all(attrs={'class': 'ce_text last block'})[0].find_all('p')[k])
                    text_cleaned = clean_text_function(str(one_p))
                    if len(text_cleaned) > 0:
                        one_poem_text.append(text_cleaned)
            except IndexError:
                for j in range(len(poem_text_parsed.find_all(attrs={'class': 'ce_text block'})[0].find_all('p'))):
                    one_p1 = poem_text_parsed.find_all(attrs={'class': 'ce_text block'})[0].find_all('p')[j]
                    text_cleaned1 = clean_text_function(str(one_p1))
                    if len(text_cleaned1) > 0:
                        one_poem_text.append(text_cleaned1)

            one_poet_text.append(one_poem_text)

        dict_poets[poet] = one_poet_text

    return dict_poets
