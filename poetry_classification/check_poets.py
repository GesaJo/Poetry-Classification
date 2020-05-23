''' Checking if poems by the author are on the website via a list of the
    names that has been created beforehand.'''

import re
import requests
from bs4 import BeautifulSoup

def poets_list():
    """generating the list of author-names
        (via one poet from each alphabet-section)"""
    poets_list = []
    for name in ['auslaender', 'eich', 'hagelstange', 'lasker', 'platen']:
        get_poets = requests.get(f'https://www.deutschelyrik.de/{name}.html')
        poets_soup = BeautifulSoup(get_poets.text, 'html.parser')

        for poet in poets_soup.find_all(attrs={'class': 'level_2'})[0].find_all('a'):
            poet_name = poet.get('title')
            poets_list.append(poet_name)
        poets_list.append(name)

    # take out Kaléko due to rights-situation
    if 'Kaléko' in poets_list:
        poets_list.remove('Kaléko')

    poets_available = ([x.lower() for x in poets_list])
    poets_available = re.sub('ä', 'ae', str(poets_available))
    poets_available = re.sub('ö', 'oe', poets_available)
    poets_available = re.sub('ü', 'ue', poets_available)
    poets_available = re.sub('ß', 'ss', poets_available)

    # save
    with open("poets_list.txt", "w") as output:
        output.write(str(poets_available))


def check_poets_function(list_of_poets):
    '''
        function to check if the given poet is on the website (= in the list).
        Input: list of poet-names,
        output: exits the program if poet is not in list, otherwise continues.
    '''
    with open("poets_list.txt", "r") as out:
        poets_av = out.read()

        for poet_name_to_check in list_of_poets:
            if poet_name_to_check not in poets_av:
                print(f'Unfortunately, no poems by {poet_name_to_check} exist on the website.')
                print('Please start again.')
                raise SystemExit(0)
