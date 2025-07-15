import sys
from stats import get_num_words, get_num_chars, get_sorted_dict

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    args = sys.argv
    if len(args) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    filepath = args[1]
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}")

    book_text = get_book_text(filepath)

    num_words = get_num_words(book_text)
    
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")

    num_chars = get_num_chars(book_text)

    print("--------- Character Count -------")
    sorted_dicts = get_sorted_dict(num_chars)
    for p in sorted_dicts:
        if (p["char"].isalpha()):
            print(f"{p["char"]}: {p["num"]}")

main()
