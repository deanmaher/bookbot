def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    chars_dict = get_chars_dict(text)
    chars_sorted_list = chars_dict_to_sorted_list(chars_dict)

    print(f"~~~ Begin report of {book_path} ~~~")
    num_words = get_num_words(text)
    print(f"{num_words} words found in the document")

    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['count']} times")

    print("--- End report ---")

#This function will tell sort() to compare dictionaries based on their 'count' field
def sort_on(dict):
    return dict["count"]

#This function converts the characters and their counts dictionary to a list of dictionaries 
def chars_dict_to_sorted_list(dict):
    list_of_dicts = []

    for char, count in dict.items():
        new_dict = {"char": char, "count": count}
        list_of_dicts.append(new_dict)
    list_of_dicts.sort(key=sort_on, reverse=True)
    return list_of_dicts

#This function counts how much each character occurs in the text and returns this info in a dictionary as char, count
def get_chars_dict(text):
    lowered_text = text.lower()
    char_count = {}
    for char in lowered_text:
        if char not in char_count:
            char_count[char] = 1
        else:
            char_count[char]+=1
    return char_count

#This function counts how many words are in the text 
def get_num_words(text):
    words = text.split()
    return len(words)

#This function reads the input file
def get_book_text(path):
    with open(path) as f:
        return f.read()


main()