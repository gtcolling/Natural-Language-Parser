import grammar_dictionary


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
    tree.update(grammar_dictionary.find_in_dict(tokens, tree))

    print(tree)


if __name__ == '__main__':
    main()
