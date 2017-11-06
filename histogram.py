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
    return all_words_array

def list_of_counts(source_file):
    tuple_list = []
    frequency_dictionary = histogram_dictionary(source_file)
    frequencys_of_words = []
    for key in frequency_dictionary:
        # frequencys_of_words = [[frequency_tuple[0]] for frequency_tuple in tuple_list]
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


def histogram_tuple(source_file):
    with open('%s' % source_file, 'r') as f:
        all_words = f.read()
        all_words = all_words.replace('\ufeff', '')
        all_words_array = all_words.split()
        cleaned_words_array = []
        for word in all_words_array:
            cleaned_word = ''
            for character in word:
                if character not in punctuation:
                    cleaned_word += character
            if cleaned_word.isalpha():
                cleaned_words_array.append(cleaned_word)
        unique_word_list = []
        tuple_array = []
        for word in cleaned_words_array:
            if word not in unique_word_list:
                word_tuple = (word, 1)
                unique_word_list.append(word)
                tuple_array.append(word_tuple)
            else:
                for tuple_index in tuple_array:
                    if tuple_index[0] == word:
                        selected_tuple_value = tuple_index[1]
                        new_tuple = (word, selected_tuple_value + 1)
                        index = tuple_array.index(tuple_index)
                        tuple_array[index] = new_tuple

        return tuple_array




def histogram_list(source_file):
    with open('%s' % source_file, 'r') as f:
        all_words = f.read()
        all_words = all_words.replace('\ufeff', '')
        all_words_array = all_words.split()
        cleaned_words_array = []
        for word in all_words_array:
            cleaned_word = ''
            for character in word:
                if character not in punctuation:
                    cleaned_word += character
            if cleaned_word.isalpha():
                cleaned_words_array.append(cleaned_word)


        unique_word_list = []
        all_words_list = []
        for first_looped_word in cleaned_words_array:
            if first_looped_word not in unique_word_list:
                count = 1
                new_word = [first_looped_word, count]
                unique_word_list.append(first_looped_word)
                all_words_list.append(new_word)
            else:
                for index in all_words_list:
                    if index[0] == first_looped_word:
                        index[1] +=1

        return all_words_list



if __name__ == '__main__':
    tuple_list = list_of_counts('76-0.txt')
    print(tuple_list)
    # inputted = sys.argv[1:]
    # word_count = int(inputted[0])
    # word_dict = histogram_dictionary('76-0.txt')
    # frequency = frequency_dictionary(word_dict, 'The')
    # word_list = histogram_list('76-0.txt')
    # word_list = histogram_tuple('76-0.txt')
    # number = frequency_list(word_list, 'the')
    # print(number)
    # print(word_list)
    # print(word_dict)
    # print(len(word_dict))
    # print(frequency)
    # print(word_array)
