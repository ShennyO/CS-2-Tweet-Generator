import random
import sys


def reverse_words(words):
    reversed_word_list = []
    for word in words:
        reversed_word_list.insert(0, word)
    word_list = ' '.join(reversed_word_list)
    return word_list


def rearrange_words(words):
    print(words)
    word_list = []
    returning_word_list = []

    for word in words:
        word_list.append(word)

    used_random_numbers = []
    number_of_words = 0
    while number_of_words < len(word_list):
        rand_index = random.randint(0, len(word_list) - 1)
        # print(rand_index)

        if rand_index not in used_random_numbers:
            returning_word_list.append(word_list[rand_index])
            used_random_numbers.append(rand_index)
            print(number_of_words)
            number_of_words +=1


    return returning_word_list

if __name__ == '__main__':
    inputted = sys.argv[1:]
    quote = reverse_words(inputted)
    # quote = rearrange_words(inputted)
    # quote = ' '.join(quote)
    print(quote)
