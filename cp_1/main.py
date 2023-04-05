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

        print('Num. of all the letters:', sum(letter_count.values()))

        return letter_count

def count_bigrams():
    input_file = 'output.txt'

    with open(input_file, 'r') as file:
        content = file.read()

        bigrams_count = collections.Counter(content[i : i + 2] for i in range(len(content) - 1))

        for bigram in sorted(bigrams_count):
            if bigram.isalpha():
                print(f'{bigram}: {bigrams_count[bigram]}')

        print('Num of all the bigrams is', sum(bigrams_count.values()))

        return bigrams_count

def entropy_1(letter_freq, total_letter_num):
    entropy = letter_freq / total_letter_num

    return entropy

letter = count_letters() #it's a dictionary
Z = letter.keys()

for z_i in sorted(Z):
    letter_frequency = entropy_1(letter[z_i], sum(letter.values()))
    print(f'For {z_i} the P = {letter_frequency:.3f}')
def entropy_2(bigram_freq, total_bigram_num):
    entropy = bigram_freq / total_bigram_num

    return entropy

bigram = count_bigrams() #it's a dictionary
Z = bigram.keys()

for z_i in sorted(Z):
    bigram_frequency = entropy_1(bigram[z_i], sum(bigram.values()))
    print(f'For {z_i} the P = {bigram_frequency:.3f}')
