import pdb
import matplotlib.pyplot as plt
import numpy as np
from string import punctuation

def histogram_dictionary(source_file):
        all_words_array = read_source_file(source_file)
        all_words_dict = {}

        for word in all_words_array:
            if word not in all_words_dict:
                all_words_dict[word] = 1
            else:
                all_words_dict[word] += 1


        return all_words_dict


def read_source_file(source_file):
    with open('%s' % source_file, 'r') as f:
        all_words = f.read()
        all_words = all_words.replace('\ufeff', '')
        all_words_array = all_words.split()
        all_words_array = clean_words(all_words_array)
    return all_words_array

def list_of_counts(source_file):
    tuple_list = []
    frequency_dictionary = histogram_dictionary(source_file)
    frequencys_of_words = []
    for key in frequency_dictionary:

        if frequency_dictionary[key] not in frequencys_of_words:
            new_tuple = (frequency_dictionary[key], [key])
            tuple_list.append(new_tuple)
            frequencys_of_words.append(frequency_dictionary[key])
        else:

            for index, frequency in enumerate(frequencys_of_words):
                if frequency_dictionary[key] == frequency:
                    tuple_list[index][1].append(key)
    return tuple_list




def frequency_dictionary(word_dictionary, word):
    return word_dictionary[word]

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


def histogram_tuple(source_file):
    all_words_array = read_source_file(source_file)
    tuple_array = []
    tuple_array_words = [index[0] for index in tuple_array]
    for word in all_words_array:
        if word not in tuple_array_words:
            word_tuple = (word, 1)
            tuple_array_words.append(word)
            tuple_array.append(word_tuple)
        else:
            word_index = tuple_array_words.index(word)
            selected_tuple_value = tuple_array[word_index][1]
            new_tuple = (word, selected_tuple_value + 1)
            tuple_array[word_index] = new_tuple


    return tuple_array




def histogram_list(source_file):

    all_words_array = read_source_file(source_file)

    unique_word_list = []
    all_words_list = []
    for word in all_words_array:
        if word not in unique_word_list:
            new_word_array = [word, 1]
            unique_word_list.append(word)
            all_words_list.append(new_word_array)
        else:
            selected_word_index = unique_word_list.index(word)
            all_words_list[selected_word_index][1] += 1
            

    return all_words_list



if __name__ == '__main__':

    word_list = histogram_list('76-0.txt')
    print(word_list)
