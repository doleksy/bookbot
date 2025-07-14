from stats import get_num_words, get_num_chars

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def sort_on(items):
    print(items)
    return items

def main():
    filepath = "books/frankenstein.txt"
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}")

    book_text = get_book_text(filepath)

    num_words = get_num_words(book_text)
    
    print("----------- Word Count ----------")
    print(f"{num_words} words found in the document")

    num_chars = get_num_chars(book_text)

    print("--------- Character Count -------")
    #print(num_chars)
    list(num_chars).sort(reverse=True, key=sort_on)
    print(num_chars)
    for k, v in num_chars.items():
        print(f"{k}: {v}")

main()
