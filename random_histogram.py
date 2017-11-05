# import histogram
import random
import pdb


def get_unique_words(sentence):
    sentence_array = sentence.split()
    unique_word_list = []
    for word in sentence_array:
        if word not in unique_word_list:
            unique_word_list.append(word)
    return unique_word_list

def histogram_dictionary(source_file):
    with open('%s' % source_file, 'r') as f:
        all_words = f.read()
        all_words = all_words.replace('\ufeff', '')
        all_words_array = all_words.split()
        print(len(all_words_array))
        all_words_dict = {}

        for word in all_words_array:
            if word not in all_words_dict:
                all_words_dict[word] = 1
            else:
                all_words_dict[word] += 1
        return all_words_dict

def get_total_words(dictionary):
    total_count = 0
    for word in dictionary:
        total_count += dictionary[word]
    return total_count

def get_random_word(dictionary, total_word_count):
    # random_num = random.randint(1, total_count)
    random_num = random.randint(1, total_word_count)
    
    for word in dictionary:
        if dictionary[word] < random_num:
            random_num -= dictionary[word]
        else:
            return word









def main():
    unique_word_dict = histogram_dictionary('76-0.txt')
    total = get_total_words(unique_word_dict)
    random_word = get_random_word(unique_word_dict, total)
    print(total)
    print(random_word)







if __name__ == '__main__':
    main()
