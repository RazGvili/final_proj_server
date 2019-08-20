import spacy
import textacy
import textacy.keyterms

# Load spaCy's English NLP model
nlp = spacy.load("en_core_web_sm")

# pre - processing function
def pre(text):
    text = textacy.preprocess.remove_punct(text, marks='…')
    text = textacy.preprocess.remove_punct(text, marks='“”')
    text = textacy.preprocess.remove_punct(text, marks='-')
    text = textacy.preprocess.remove_punct(text, marks='…')
    text = textacy.preprocess.remove_punct(text, marks='’')
    text = textacy.preprocess.remove_punct(text, marks='“')
    text = textacy.preprocess.remove_punct(text, marks='”')
    text = textacy.preprocess.remove_punct(text, marks=' – ')
    text = textacy.preprocess.normalize_whitespace(text)

    # Text after pre - processing
    print("Text after pre-processing --> \n")
    print(text)

    return text


def getKeys(text):

    # pre - processing
    text = pre(text)

    # Parse the text with spaCy
    # Our 'document' variable now contains a parsed version of text.
    document_text = nlp(text)

    print("key_terms_from_semantic_network(divrank):")
    statements_semantic_network = textacy.keyterms.key_terms_from_semantic_network(document_text, ranking_algo='divrank')
    print(statements_semantic_network)
    print()

    print(len(document_text))
    return statements_semantic_network
    # return statements_semantic_network


def getKeysJoin(text):

    # pre - processing
    text = pre(text)

    # Parse the text with spaCy
    # Our 'document' variable now contains a parsed version of text.
    document_text = nlp(text)

    print("key_terms_from_semantic_network(default)(join_key_words=True):")
    statements_semantic_network_join = textacy.keyterms.key_terms_from_semantic_network(document_text, join_key_words=True)
    print(statements_semantic_network_join)
    print()

    print(len(document_text))
    return statements_semantic_network_join


# Local Tests
if __name__ == '__main__':
    text1 = " Then all of a sudden, about 1 hour later there was a 360 degrees change in my wife’s attitude towards me:" \
           " she stopped answering simple questions, walked around looking angry and I could feel fire in her eyes. "

    text2 = "I came back from a 2 week business trip in the USA," \
            "and my wife and kids were all around me at home unpacking my suitcase and looking for their presents," \
            "and my wife helping me with the laundry." \
            "Then all of a sudden, about 1 hour later there was a 360 degrees change" \
            "in my wife s attitude towards me: she stopped" \
            "answering simple questions, walked around looking angry and I could feel fire in her eyes."

    # getKeys(text1)


