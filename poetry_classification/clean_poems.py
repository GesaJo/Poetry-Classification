import re
import spacy


def clean_text_function(text):
    ''' function to clean text:
        replace Umlaute and delete noise'''

    Patterns = [('ä', 'ae'), ('ö', 'oe'), ('ü', 'ue'), ('ß', 'ss'),
                ('<.+?>', ' '), ('Aufnahme \d{4}', '!--!'), ('\\\xa0', '')]
    for to_replace, insert in Patterns:
        text = re.sub(to_replace, insert, text)

    return text


def tokenize_function(list_of_poets):
    ''' tokenizing with spacy
        and saving cleaned texts.'''

    for poet in list_of_poets:
        f = open(f'Poems/{poet}.txt', 'r')
        poetx = f.read()
        f.close()

        # clean up text
        clean_text = clean_text_function(poetx)
        clean_text = clean_text.split(sep='!--!')

        # tokenize
        model = spacy.load('de_core_news_sm')

        tokenized = []
        for poem in clean_text:
            clean_poem = []
            tokenized_poem = model(poem)
            for token in tokenized_poem:
                if not token.is_stop:
                    if token.is_alpha:
                        clean_poem.append(token.lemma_)
            tokenized.append(clean_poem)
        tokenized.pop(0)
        return_poet = poet
    return return_poet, tokenized


def save_cleaned_text(poet_name, tokenized_text):

    with open(f"Poems/{poet_name}_cleaned.txt", "w") as output:
        output.write(str(tokenized_text))

    print(f'{poet_name.title()} has been added to the corpus.')
