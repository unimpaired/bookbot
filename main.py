from stats import count_words, count_repeated_letters, sort_letter_list, format_to_console

import sys

def main():
    if len(sys.argv) != 2:
        print(f'Usage: python3 main.py <path_to_book>')
        sys.exit(1)

    filepath = sys.argv[1]

    try:
        document = open_file(filepath)
        word_count = count_words(document)
        repeated_letter_count = count_repeated_letters(document)
        sorted_list = sort_letter_list(repeated_letter_count)
        formatted_message = format_to_console(filepath, word_count,sorted_list)
        return formatted_message
    except Exception as error:
         print(error)

def open_file(filepath):
    with open(filepath, "r", encoding="utf-8") as file:
        text = file.read()
        return text

main()