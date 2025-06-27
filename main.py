from stats import get_num_words, get_num_chars, sort_on
    # imports get_num_words value into script

def main():
    # defines main function that produces desired output
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars = get_num_chars(text)
    char_sort = sort_on(text)
    print(f"{num_words} words found in the document")
    print(char_sort)
    


def get_book_text(path):
    # defines a function that takes a document from a path and ingests entire text
    with open(path) as f:
        return f.read()

main()
    # calls the main function
