def replace_word(word_to_replace, somestory):

    replacement = input("Enter a " + word_to_replace + ": ")

    return somestory.replace(word_to_replace, replacement)


print(replace_word("animal", "I like to eat animal"))

