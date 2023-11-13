grammar = {"sub": ['I', 'We'],
           "adv": ['never', 'always', 'often', 'quickly', 'slowly', 'frequently', 'silently', 'occasionally', 'now',
                   'daily'],
           "verb": ['am', 'are', 'run', 'swim', 'fight', 'go', 'eat', 'understand', 'enjoy', 'use'],
           "prep": ['at', 'in', 'with', 'to', 'below', 'along', 'above', 'on', 'over', 'off'],
           "adj": ['cold', 'sunny', 'mean', 'cool', 'rough', 'damp', 'smooth', 'warm', 'rainy', 'hot'],
           "art": ['the', 'a', 'an'],
           "noun": ['office', 'banana', 'dog', 'cat', "umbrella", "hat", "stone", "park", "car", "breakfast"]
           }


def find_in_dict(tokens, dictionary):
    i = 0
    for string in tokens:
        for key, value in grammar.items():
            if string in value:
                if key in dictionary.keys():
                    dictionary[key].append({string: i})
                else:
                    dictionary[key] = []
                    dictionary[key].append({string: i})
        i += 1
    return dictionary
