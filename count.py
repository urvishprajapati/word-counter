import string

def count_words(user_input):
    """
    Count the number of words in the given input.
    """
    if not user_input.strip():
        return "Input cannot be empty. Please enter some text."
    words = user_input.split()
    word_count = len(words)
    return word_count, words


def count_characters(user_input):
    """
    Count the number of characters (excluding spaces) in the input.
    """
    characters = len(user_input.replace(" ", ""))
    return characters


def word_frequency(words):
    """
    Count the frequency of each word in the input.
    """
    frequency = {}
    for word in words:
        cleaned_word = word.strip(string.punctuation).lower()
        frequency[cleaned_word] = frequency.get(cleaned_word, 0) + 1
    return frequency


def main():
    """
    Main function to interact with the user and provide word and character statistics.
    """
    print("\n" + "=" * 40)
    print("   Welcome to the Advanced Word Counter!")
    print("=" * 40 + "\n")
    print("Type or paste your paragraph below:")

    user_input = input("> ")

    if not user_input.strip():
        print("\nOops! You entered an empty input. Please try again.")
        return

    # Get word count and list of words
    word_count, words = count_words(user_input)

    # Get character count
    char_count = count_characters(user_input)

    # Get word frequency
    frequency = word_frequency(words)

    # Display results
    print("\n" + "=" * 40)
    print("           Here are your results!")
    print("=" * 40)
    print(f"Total Words: {word_count}")
    print(f"Total Characters (excluding spaces): {char_count}")
    print("\nWord Frequencies:")
    for word, count in frequency.items():
        print(f"  - {word}: {count}")

    print("\nThank you for using the Advanced Word Counter!\n")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print("An unexpected error occurred:", str(e))
