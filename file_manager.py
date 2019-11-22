def read_from_file(filename='default_words.txt'):
    '''
    Reads lists from file

    >>> read_from_file()
    [['aaa', 'bbbb', 'cccccc'], ['dd', 'eeeeee', 'fffffffff']]
    '''
    list_of_lines = []
    file = open(filename, 'r')
    for line in file:
        line = line.strip().split(',')
        stripped_elements = [element.strip() for element in line]
        list_of_lines.append(stripped_elements)
    file.close()
    return list_of_lines


def write_to_file(words, filename='longest_words.txt'):
    pass
