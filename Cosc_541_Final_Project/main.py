from grammar_dictionary import find_in_dict, check_grammar


def main():
    # accept user input
    sentence = input("Please enter a sentence: ")
    print("You entered: " + sentence)

    # tokenize string
    tokens = sentence.split()

    # initialize empty dictionary to hold key:value pairs
    tree = {}

    # find if tokens exist in predefined lists for the grammar, keeping location of
    # each word in the string to form phrases
    tree.update(find_in_dict(tokens, tree))

    # check and see if the sentence violates our grammar
    if not check_grammar(tree):
        print("Your input is not a valid sentence.")
    else:
        print("Your input passes!")

if __name__ == '__main__':
    main()
