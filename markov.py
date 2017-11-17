from string import punctuation
from dictogram import Dictogram
import random
import pdb

class Markov(dict):
    """docstring for Markov."""
    def __init__(self, word_list=None):
        super(Markov, self).__init__()

        if word_list != None:
            for index, word in enumerate(word_list):
                if word not in self:
                    selected_index = index
                    next_word = word_list[selected_index + 1]
                    self[word] = Dictogram()
                    self[word].tokens += 1
                    self[word][next_word] = 1
                else:
                    selected_index = index
                    if index < len(word_list) -1:
                        next_word = word_list[selected_index + 1]
                        if next_word not in self[word]:
                            self[word][next_word] = 1
                            self[word].tokens += 1
                        else:
                            self[word][next_word] +=1
                            self[word].tokens += 1
            


def generate_sentence(markov_dictionary, words_array):
    total_count = 0
    sentence = []
    for word in markov_dictionary:
        total_count += markov_dictionary[word].tokens


    random_num = random.randint(0, total_count)
    selected_word = ""
    for index in range(0, 20):

        if len(sentence) is 0:
            random_word = get_random_word(markov_dictionary, total_count)
            selected_word = random_word
            # pdb.set_trace()
            sentence.append(random_word)
        else:
            # pdb.set_trace()
            next_word = get_next_word(markov_dictionary, selected_word)
            sentence.append(next_word)
            selected_word = next_word
    return sentence

def get_next_word(markov_dictionary, word):
    next_word_choices = markov_dictionary[word]
    word_choices_count = next_word_choices.tokens
    random_num = random.randint(1, word_choices_count)
    for word in next_word_choices:
        if next_word_choices[word] < random_num:
            random_num -= next_word_choices[word]
        else:
            return word



def clean_words(words_array):
    cleaned_words_array = []
    for word in words_array:
        cleaned_word = ''
        for character in word:
            if character not in punctuation:
                cleaned_word += character
        if cleaned_word.isalpha():
            cleaned_words_array.append(cleaned_word)
    return cleaned_words_array

def read_source_file(source_file):
    with open('%s' % source_file, 'r') as f:
        all_words = f.read()
        all_words = all_words.replace('\ufeff', '')
        all_words_array = all_words.split()
        all_words_array = clean_words(all_words_array)
    return all_words_array

def main():
    all_words_array = read_source_file('76-0.txt')
    markovDict = Markov(all_words_array)
    # print(markovDict)
    sentence=generate_sentence(markovDict, all_words_array)
    print(' '.join(sentence))

def get_random_word(dictionary, total_word_count):

    random_num = random.randint(1, total_word_count)
    for word in dictionary:
        if dictionary[word].tokens < random_num:
            random_num -= dictionary[word].tokens
        else:
            return word


if __name__ == '__main__':
    main()
