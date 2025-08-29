"""Functions for creating, transforming, and adding prefixes to strings."""


def add_prefix_un(word):
    """Take the given word and add the 'un' prefix.

    :param word: str - containing the root word.
    :return: str - of root word prepended with 'un'.
    """

    return ("un" + word)


def make_word_groups(vocab_words):
    """Transform a list containing a prefix and words into a string with the prefix followed by the words with prefix prepended.

    :param vocab_words: list - of vocabulary words with prefix in first index.
    :return: str - of prefix followed by vocabulary words with
            prefix applied.

    This function takes a `vocab_words` list and returns a string
    with the prefix and the words with prefix applied, separated
     by ' :: '.

    For example: list('en', 'close', 'joy', 'lighten'),
    produces the following string: 'en :: enclose :: enjoy :: enlighten'.
    """

    prefix_string = vocab_words[0]
    prefix = prefix_string
    
    num = len(vocab_words)
    
    for i in range(1, num):
        new = " " + prefix + vocab_words[i]
        #print(f"new={new}")
        prefix_string += new
        
    prefix_string = prefix_string.split()
    prefix_string = " :: ".join(prefix_string)
    
    return prefix_string


def remove_suffix_ness(word):
    """Remove the suffix from the word while keeping spelling in mind.

    :param word: str - of word to remove suffix from.
    :return: str - of word with suffix removed & spelling adjusted.

    For example: "heaviness" becomes "heavy", but "sadness" becomes "sad".
    """

    ness_removed = word[:-4:]
    print(f"ness_removed = {ness_removed}")

    if ness_removed[-1::] == "i":
        i_removed = ness_removed[:-1:]
        y_added = i_removed + "y"
        ness_removed = y_added

    return ness_removed
        


def adjective_to_verb(sentence, index):
    """Change the adjective within the sentence to a verb.

    :param sentence: str - that uses the word in sentence.
    :param index: int - index of the word to remove and transform.
    :return: str - word that changes the extracted adjective to a verb.

    For example, ("It got dark as the sun set.", 2) becomes "darken".
    """

    adjective = sentence.split()[index]
    
    if adjective[-1::] in [".", ",", "!"]:
        adjective = adjective[:-1:]
    
    return adjective + "en"
     
