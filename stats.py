from helper import quick_sort_lists, format_to_string

def count_words(document: str) -> str:
    words = document.split()
    count = 0

    for word in words:
        count += 1
    
    return (f'Found {count} total words')


def count_repeated_letters(document: str) -> dict[str, int]: 
    letter_count: dict[str, int]= {}
    
    for letter in document:
        letter = letter.lower()
        if letter not in letter_count:
            letter_count[letter] = 1
        else:
            letter_count[letter] += 1
    return letter_count

def sort_letter_list(letter_count_list: dict[str, int]) -> dict[str, int]:
    letter_list = list(letter_count_list.items())

    # Sort tuples by count using quicksort
    sorted_list = quick_sort_lists(letter_list)
    
    # Convert sorted tuples back to dict
    sorted_dict = {}
    for char, count in sorted_list:
        if char.isalpha():
            sorted_dict[char] = count
    return sorted_dict

def format_to_console(book_path: str,count: str, the_list: dict[str, int]) -> str:

    string_list = format_to_string(the_list)

    title = f'============ BOOKBOT ============\n'
    subheader = f'Analysing book found at {book_path}...\n'
    header = f'----------- Word Count ----------\n'
    word_count = f'{count}\n'
    char_counter_header = f'--------- Character Count -------\n'
    char_count = f'{string_list}'
    footer = f'============= END ==============='

    message = title + subheader + header + word_count + char_counter_header + char_count + footer
    print(message)
    return message