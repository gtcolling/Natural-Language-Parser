from grammar_dictionary import find_in_dict, check_grammar


def main():
    # Accept user input
    sentence = input("Please enter a sentence: ")

    # Tokenize string
    tokens = sentence.split()

    # Initialize empty dictionary to hold key:value pairs
    tree = {}

    # Find if tokens exist in predefined lists for the grammar, keeping location of
    # Each word in the string to form phrases
    tree.update(find_in_dict(tokens, tree))

    # Check and see if the sentence violates our grammar
    if not check_grammar(tree):
        print("Your input is not valid. Please try again.")
    else:
        print("Your input passes!")


if __name__ == '__main__':
    main()
