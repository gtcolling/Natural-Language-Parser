grammar = {"sub": ['I', 'We'],
           "adv": ['never', 'always', 'often', 'quickly', 'slowly', 'frequently', 'silently', 'occasionally', 'now',
                   'daily'],
           "verb": ['am', 'are', 'run', 'swim', 'fight', 'go', 'eat', 'understand', 'enjoy', 'use'],
           "prep": ['at', 'in', 'with', 'to', 'below', 'along', 'above', 'on', 'over', 'off'],
           "adj": ['cold', 'sunny', 'mean', 'cool', 'rough', 'damp', 'smooth', 'warm', 'rainy', 'hot'],
           "art": ['the', 'a', 'an'],
           "noun": ['office', 'banana', 'dog', 'cat', 'umbrella', 'hat', 'stone', 'park', 'car', 'breakfast']
           }


def find_in_dict(tokens, dictionary):
    i = 0
    for string in tokens:
        valid = False
        for key, value in grammar.items():
            if string in value:
                if key in dictionary.keys():
                    dictionary[key].append((string, i))
                    valid = True
                else:
                    dictionary[key] = []
                    dictionary[key].append((string, i))
                    valid = True
        if not valid:
            dictionary["not_found"] = string
        i += 1

    return dictionary


def check_grammar(dictionary):
    subject_bool = False
    verb_bool = False
    noun_bool = True
    prep_bool = True
    art_bool = True
    sub = list()
    advp = list()
    verb = list()
    prep = list()
    np = list()
    adjp = list()
    art = list()

    for key, value in dictionary.items():

        # If "I" or "We" is the beginning of the sentence, and there is only one subject, set subject_bool to true.
        rng = range(len(dictionary[key]))
        if key == "sub":
            if dictionary[key][0][1] == 0 and len(dictionary[key]) == 1:
                sub.append(dictionary[key][0][0])
                subject_bool = True
            else:
                print("Subject must come first in your sentence.")

        # Create an adverb phrase (broken by verbs, nouns, articles, adjectives).
        elif key == "adv":
            for i in rng:
                advp.append(dictionary[key][i][0])
                if (i + 1 >= len(dictionary[key])) or ((dictionary[key][i][1]) != int((dictionary[key][i + 1][1]) - 1)):
                    break

        # If verb comes after the subject, set verb_bool to true.
        elif key == "verb":
            if dictionary[key][0][1] > 0 and len(dictionary[key]) == 1:
                verb.append(dictionary[key][0][0])
                verb_bool = True
            else:
                print("Verb must come after the subject of your sentence, and only one verb is allowed.")

        # Load the prep list with the preposition
        elif key == "prep":
            if len(dictionary[key]) == 1:
                prep.append(dictionary[key][0][0])
            else:
                prep_bool = False
                print("Only one preposition is allowed in your sentence.")

        # Load the art list with an article
        elif key == "art":
            if len(dictionary[key]) == 1:
                art.append(dictionary[key][0][0])
            else:
                art_bool = False
                print("Only one article is allowed in your sentence.")

        # Create an adjective phrase (as many adjectives in a row as provided by the user).
        elif key == "adj":
            for j in rng:
                adjp.append(dictionary[key][j][0])
                if (j + 1 >= len(dictionary[key])) or ((dictionary[key][j][1]) != int((dictionary[key][j + 1][1]) - 1)):
                    break

        # Create a noun phrase using the article, adjective phrase, and noun
        elif key == "noun":
            if len(dictionary[key]) == 1:
                np.append(' '.join(str(e) for e in art))
                np.append(' '.join(str(e) for e in adjp))
                np.append(str(dictionary[key][0][0]))
            else:
                noun_bool = False
                print("Only one noun is allowed in your sentence.")

        # If there is a word in the input that isn't in the parser, the sentence is invalid.
        elif key == "not_found":
            print("Your input contains a word not accepted by this parser. Please try again.")
            return False

    # Since subject and verb are the only non-nullable aspects of the grammar,
    # they must be present for a passing sentence. Also, only one subject, verb, article,
    # preposition, and noun are allowed.
    if subject_bool and verb_bool and prep_bool and art_bool and noun_bool:
        print("Your sentence has been broken down as follows: " +
              "Subject: " + ' '.join(str(e) for e in sub) + ", " +
              ("Adverb Phrase: " + ' '.join(str(e) for e in advp) + ", " if len(advp) > 0 else "") +
              "Verb: " + ' '.join(str(e) for e in verb) + ", " +
              ("Preposition: " + ' '.join(str(e) for e in prep) + ", " if len(prep) > 0 else "") +
              ("Noun Phrase: " + ' '.join(str(e) for e in np) + "\n" if len(np) > 0 else "\n"))
        return True

    # If subject and verb are not present, or are incorrectly placed the sentence automatically fails.
    else:
        return False
