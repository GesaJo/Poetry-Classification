import spacy

def tokenize_function(dict_poets):
    '''Tokenizing with spacy and saving cleaned texts.'''

    dict_tokenized = {}
    for poet in dict_poets:
        model = spacy.load('de_core_news_sm')
        tokenized = []
        for paragraph in dict_poets[poet]:
            for poem in paragraph:
                clean_poem = []
                tokenized_poem = model(poem)
                for token in tokenized_poem:
                    if not token.is_stop:
                        if token.is_alpha:
                            clean_poem.append(token.lemma_)
                tokenized.append(clean_poem)
        tokenized.pop(0)
        dict_tokenized[poet] = tokenized
        print(f'{poet.title()} has been added to the corpus.')
    return dict_tokenized
