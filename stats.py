def get_num_words(text):
    # function that counts the number of words in the list that is created
    words = text.split()
    return len(words)

def get_num_chars(text):
    # function that counts the number of characters in the document
    text = text.lower()
    # convert string to lowercase
    char_count = {}
    for char in text:
        #iterate through each character
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    return char_count

def sort_on(char_count):
    # sort the character count dictionary in reverse order
    char_count.sort(reverse = True, key = sort_on)
    return char_count