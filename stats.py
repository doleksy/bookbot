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

def sort_on(items):
    return items["num"]

def get_sorted_dict(chars_dict):
    list_of_dicts = []
    for k, v in chars_dict.items():
        list_of_dicts.append({"char": k, "num": v})
        
    list_of_dicts.sort(key=sort_on, reverse=True)

    return list_of_dicts
    
