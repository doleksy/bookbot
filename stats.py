def get_num_words(book_text):
    return len(book_text.split())

def get_num_chars(book_text):
    char_dict = {}
    for ch in book_text:
        lower_ch = ch.lower()
        if (lower_ch in char_dict):
            char_dict[lower_ch] += 1
        else:
            char_dict[lower_ch] = 1
    return char_dict
