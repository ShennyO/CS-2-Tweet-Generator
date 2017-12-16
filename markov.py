from string import punctuation
from dictogram import Dictogram
import random
import pdb

class Markov(dict):
    """docstring for Markov."""
    def __init__(self, word_list=None):
        super(Markov, self).__init__()
        #if there is an array of words
        if word_list != None:
            #looping through all the array
            for index, word in enumerate(word_list):
                #self refers to the outer dictionary
                if word not in self:
                    #make a dictogram with the key being the selected word, and append the next word as the first value
                    #and increase that dictogram's tokens, the amount of unique words it has, by 1
                    selected_index = index
                    next_word = word_list[selected_index + 1]
                    self[word] = Dictogram()
                    self[word].tokens += 1
                    self[word][next_word] = 1
                else:
                    #if the word(key) is in our outer dictionary
                    selected_index = index
                    #if the index is not the last word in the word list
                    if index < len(word_list) -1:
                        next_word = word_list[selected_index + 1]
                        if next_word not in self[word]:
                            #add the new word as a key, and the next word as a value
                            self[word][next_word] = 1
                            self[word].tokens += 1
                        else:
                            self[word][next_word] +=1
                            self[word].tokens += 1



def generate_sentence(markov_dictionary, words_array):
    total_count = 0
    sentence = []
    #Looping through the outer dictionary
    for word in markov_dictionary:
        total_count += markov_dictionary[word].tokens
    random_num = random.randint(0, total_count)
    selected_word = ""
    for index in range(0, 20):

        if len(sentence) is 0:
            #if it's the first word, then pick a random word
            random_word = get_random_word(markov_dictionary, total_count)
            selected_word = random_word
            sentence.append(random_word)
        else:
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
    print(markovDict)
    # sentence=generate_sentence(markovDict, all_words_array)
    # print(' '.join(sentence))
#I dont get this func
def get_random_word(dictionary, total_word_count):

    random_num = random.randint(1, total_word_count)
    for word in dictionary:
        if dictionary[word].tokens < random_num:
            random_num -= dictionary[word].tokens
        else:
            return word


if __name__ == '__main__':
    main()
