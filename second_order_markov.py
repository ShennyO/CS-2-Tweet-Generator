from string import punctuation
from dictogram import Dictogram
import random
import pdb

#Now, instead of having just 1 word as a key, we want a tuple as a key. We'll first start off by
#choosing two random consecutive words, and keep track of the second word
#next, we'll get the next word, and prepend the previous word into a tuple, and check if it
#exists in our outer dictionary
#The second order markov keeps track of the word we used previously, but only appends the new word
#to the inner dictionary


# first_word = word_list[0]
# second_word = word_list[1]
# tuple_key = (word, second_word)
# last_word = word_list[1]
# self[tuple_key] = Dictogram()
# #start with the third word since we already used 2
# for index, word in enumerate(word_list[2:]):
#     #first we'll handle the appending logic
#     if word not in self[tuple_key]:
#         self[tuple_key][word] = 1
#         self[tuple_key].tokens += 1
#     else:
#         self[tuple_key][word] += 1
#         self[tuple_key].tokens += 1
#     new_key = (last_word, word)
#     #now we handle making a new key or not
#     if new_key not in self:
#         self[new_key] = Dictogram()
#     #now we set the tuple_key and last_word
#     tuple_key = new_key
#     last_word = new_key[1]





class Markov(dict):
    """docstring for Markov."""
    def __init__(self, word_list=None):
        super(Markov, self).__init__()
        #if there is an array of words
        if word_list != None:
            #looping through all the array
            first_word = word_list[0]
            second_word = word_list[1]
            tuple_key = (first_word, second_word)
            last_word = word_list[1]
            self[tuple_key] = Dictogram()
            #start with the third word since we already used 2
            for index, word in enumerate(word_list[2:]):
                #first we'll handle the appending logic
                if word not in self[tuple_key]:
                    self[tuple_key][word] = 1
                    self[tuple_key].tokens += 1
                else:
                    self[tuple_key][word] += 1
                    self[tuple_key].tokens += 1
                new_key = (last_word, word)
                #now we handle making a new key or not
                if new_key not in self:
                    self[new_key] = Dictogram()
                #now we set the tuple_key and last_word
                tuple_key = new_key
                last_word = new_key[1]



def generate_sentence(markov_dictionary, words_array):
    total_count = 0
    sentence = []
    #Looping through the outer dictionary
    for word in markov_dictionary:
        total_count += markov_dictionary[word].tokens

    pdb.set_trace()

    random_num = random.randint(0, total_count)
    selected_tuple = ""
    for index in range(0, 20):

        if len(sentence) is 0:
            #if it's the first word, then pick a random word
            random_tuple = get_random_word(markov_dictionary, total_count)
            selected_tuple = random_tuple
            sentence.append(random_tuple[0])
        else:
            next_tuple = get_next_word(markov_dictionary, selected_tuple)
            sentence.append(next_tuple[0])
            selected_tuple = next_tuple
    return sentence

def get_next_word(markov_dictionary, last_tuple):
    next_word_choices = markov_dictionary[last_tuple]
    word_choices_count = next_word_choices.tokens
    random_num = random.randint(1, word_choices_count)
    for word in next_word_choices:
        if next_word_choices[word] < random_num:
            random_num -= next_word_choices[word]
        else:
            return (last_tuple[1], word)



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
    for tuple_key in dictionary:
        if dictionary[tuple_key].tokens < random_num:
            random_num -= dictionary[tuple_key].tokens
        else:
            return tuple_key


if __name__ == '__main__':
    main()
