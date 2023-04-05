import string
import collections


def remove_punct():
    input_file = 'input.txt'
    output_file = 'output.txt'

    addit_punct = ['—', '«', '»']
    translator = str.maketrans('', '', string.punctuation + ''.join(addit_punct) + ' ' * len(string.punctuation) + '\n\r\t')

    with open(input_file, 'r', encoding='utf-8') as file:
        content = file.read()

        content = content.translate(translator).lower()
        content = ' '.join(content.split())

        with open(output_file, 'w') as output:
            output.write(content)


def count_letters():
    input_file = 'output.txt'

    with open(input_file, 'r') as file:
        content = file.read()

        letter_count = collections.Counter(content)

        for letter in sorted(letter_count):
            if letter.isalpha():
                print(f'{letter}: {letter_count[letter]}')

def count_bigrams():
    input_file = 'output.txt'

    with open(input_file, 'r') as file:
        content = file.read()

        bigrams_count = collections.Counter(content[i : i + 2] for i in range(len(content) - 1))

        for letter in sorted(bigrams_count):
            if letter.isalpha():
                print(f'{letter}: {bigrams_count[letter]}')

