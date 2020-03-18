import requests
from bs4 import BeautifulSoup


def scrape_texts_function(list_of_poets):
    ''' Get the links to all poems and write the texts into a file'''

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

        if len(poems_list) < 5:
            print(f'Sadly, there are not enough poems by {poet.title()} to make a prediction.')
            print('Please start again.')
            raise SystemExit(0)
            
        # get the texts and append them to a list
        poem_text = []
        for poem in poems_list:
            poem = requests.get('http://deutschelyrik.de/'+poem).text
            poem_text_parsed = BeautifulSoup(poem, 'html.parser')

            try:
                for k in range(len(poem_text_parsed.find_all(attrs={'class': 'ce_text last block'})[0].find_all('p'))):
                    poem_text.append(poem_text_parsed.find_all(attrs={'class': 'ce_text last block'})[0].find_all('p')[k])
            except IndexError:
                for k in range(len(poem_text_parsed.find_all(attrs={'class': 'ce_text block'})[0].find_all('p'))):
                    poem_text.append(poem_text_parsed.find_all(attrs={'class': 'ce_text block'})[0].find_all('p')[k])
        print('...still scraping...')

        # save to disk
        with open(f"Poems/{poet}.txt", "w") as output:
            output.write(str(poem_text))
