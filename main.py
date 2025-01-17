def main():
    
    global file_contents
    with open('books/frankenstein.txt') as f:
        file_contents = f.read()
        sort_by_count()
        
def sort_on(dict):
    return dict["count"]

def count_words(input):
    word_count = 0
    words = input.split()
    for word in words:
        word_count += 1
    return word_count

def count_chars(input):
    char_dictionary = {}
    lower_case_input = input.lower()

    for char in lower_case_input:
        if char == char in char_dictionary:
            char_dictionary[char] += 1
        else:
            char_dictionary[char] = 1

    return char_dictionary

def sort_by_count():
    word_count = count_words(file_contents)
    char_dictionary = count_chars(file_contents)
    list_of_dict = []
    count_up = 0
    counter = 0
    for char in char_dictionary:
        if char.isalpha() == False:
            pass
        else:    
            list_of_dict.append({"char": char, "count": char_dictionary[char]})
            count_up += 1
    list_of_dict.sort(reverse=True, key=sort_on)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document")
    print("")
    for dict in list_of_dict:
        print
        print(f"The '{dict['char']}' character was found {dict['count']} times")
        counter = counter + 1
    print("--- End report ---")

main()