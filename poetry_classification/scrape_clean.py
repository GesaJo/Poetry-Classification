import re
import requests
from bs4 import BeautifulSoup


def clean_text_function(text):
    ''' function to clean text:
        replace Umlaute and delete noise'''

    Patterns = [('ä', 'ae'), ('ö', 'oe'), ('ü', 'ue'), ('ß', 'ss'),
                ('<.+?>', ' '), ('\s*Aufnahme \d{4}', '!--!'), ('\\\xa0', '')]
    for to_replace, insert in Patterns:
        text = re.sub(to_replace, insert, text)
    return text


def scrape_texts_function(list_of_poets):
    ''' Get the links to all poems from the website and
        returns the poets and the texts as dictionary'''

    dict_poets = {}

    for poet in list_of_poets:
        get_poems = requests.get(f'https://www.deutschelyrik.de/{poet}.html')
        soup = BeautifulSoup(get_poems.text, 'html.parser')
        poet = soup.find("h1").text
        poems_list = get_link_list(soup)

        # exception for poets with less than 5 poems on the website
        if len(poems_list) < 5:
            print(f'Sadly, there are not enough poems by {poet.title()} to make a prediction.')
            print('Please start again.')
            raise SystemExit(0)

        # get the texts and append them to a list
        one_poet_text = []
        for poem in poems_list:
            one_poem_text = get_text_list(poem)
            one_poet_text.append(one_poem_text)
        dict_poets[poet] = one_poet_text
    return dict_poets


def get_link_list(links_noisy):
    """get links to poems from BeautifulSoup-object"""

    poems_list = []
    for link in links_noisy.find_all(attrs={'class': 'mod_navigation block',
                                            'id': 'snav2'})[0].find_all('a'):
        link_adress = link.get('href')
        if str(link_adress).endswith('.html'):
            poems_list.append(link_adress)
    return poems_list


def get_text_list(poem):
    """get whole text of single poem"""

    one_poem_text = []
    poem = requests.get('http://deutschelyrik.de/'+poem).text
    poem_text_parsed = BeautifulSoup(poem, 'html.parser')

    try:
        for k in range(len(poem_text_parsed.find_all(attrs={'class': 'ce_text last block'})[0].find_all('p'))):
            one_p = (poem_text_parsed.find_all(attrs={'class': 'ce_text last block'})[0].find_all('p')[k])
            for line in one_p:
                if "Notwendige Anmerkung" in line:
                    break
                text_cleaned = clean_text_function(str(line))
                if text_cleaned.isspace():
                    pass
                elif len(text_cleaned) > 0:
                    one_poem_text.append(text_cleaned)

    except IndexError:
        for j in range(len(poem_text_parsed.find_all(attrs={'class': 'ce_text block'})[0].find_all('p'))):
            one_p1 = poem_text_parsed.find_all(attrs={'class': 'ce_text block'})[0].find_all('p')[j]
            for line1 in one_p1:
                if "Notwendige Anmerkung" in line1:
                    break
                text_cleaned1 = clean_text_function(str(line1))
                if text_cleaned1.isspace():
                    pass
                elif len(text_cleaned1) > 0:
                    one_poem_text.append(text_cleaned1)
    return one_poem_text
