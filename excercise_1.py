import file_manager


def find_the_longest_word(list_of_lines):
    '''
    Find the longest word and its paramethers
    
    >>> find_the_longest_word(file_manager.read_from_file("words.txt"))
    [['ciasteczko', '10', '2'], ['krzysztofu', '10', '4']]
    '''

    max_length = 0
    max_item = ""
    max_index = 0
    longest_words = []

    for index in range(len(list_of_lines)):
        for item in list_of_lines[index]:
            if len(item) > max_length:
                longest_words.clear()
                max_length = len(item)
                max_item = item
                max_index = index
                longest_words.append([max_item, str(max_length), str(max_index)])
            elif len(item) == max_length:
                max_length = len(item)
                max_item = item
                max_index = index
                longest_words.append([max_item, str(max_length), str(max_index)])
    return longest_words


def main():
    list_of_lines = file_manager.read_from_file("words.txt")
    longest_words = find_the_longest_word(list_of_lines)
    file_manager.write_to_file(longest_words)

main()