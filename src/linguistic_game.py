def read_file():
    """Читає дані з файлу."""
    with open('./test/resorses/input_linguistic.txt', 'r') as input_file:
        lines = input_file.readlines()
        words = [word.strip() for word in lines[1:]]
    return words


def result_file(result):
    """Записує результат у файл."""
    with open('./test/resorses/output_linguistic.txt', 'w') as output_file:
        output_file.write(str(result))


def find_the_longest_chain(words):
    """Знаходить найдовший ланцюжок слів."""
    word_chain_lengths = {}
    if not words:
        return None

    for word in words:
        word_chain_lengths[word] = 1

    sorted_words = sorted(words, key=len)

    for word in sorted_words:
        for letter in range(len(word)):
            cut_word = word[:letter] + word[letter + 1:]
            if cut_word in word_chain_lengths and word_chain_lengths[cut_word] + 1 > word_chain_lengths[word]:
                word_chain_lengths[word] = word_chain_lengths[cut_word] + 1

    result_file(max(word_chain_lengths.values()))
    return max(word_chain_lengths.values())


