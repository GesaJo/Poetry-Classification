import re
import spacy


def clean_text_function(list_of_poets):
    ''' cleaning the texts, replacing Umlaute,
        tokenizing with spacy
        and saving cleaned texts.'''
        
    for poet in list_of_poets:
        f = open(f'Poems/{poet}.txt', 'r')
        poetx = f.read()
        f.close()

        # clean up text
        text_clean = re.sub('<.+?>', ' ', poetx)
        text_clean1 = re.sub('Aufnahme \d{4}', '!--!', text_clean)
        text_clean2 = re.sub('\\\xa0', '', str(text_clean1))
        text_clean3 = re.sub('ä', 'ae', text_clean2)
        text_clean4 = re.sub('ö', 'oe', text_clean3)
        text_clean5 = re.sub('ü', 'ue', text_clean4)
        text_clean6 = re.sub('ß', 'ss', text_clean5)

        clean_text = text_clean6.split(sep='!--!')

        # tokenize
        model = spacy.load('de_core_news_sm')

        clean_all = []
        for poem in clean_text:
            clean_poem = []
            tokenized_poem = model(poem)
            for token in tokenized_poem:
                if not token.is_stop:
                    if token.is_alpha:
                        clean_poem.append(token.lemma_)
            clean_all.append(clean_poem)
        clean_all.pop(0)

        # save
        with open(f"Poems/{poet}_cleaned.txt", "w") as output:
            output.write(str(clean_all))

        print(f'{poet.title()} has been added to the corpus.')
