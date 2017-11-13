from string import punctuation


class Markov(dict):
    """docstring for Markov."""
    def __init__(self, word_list=None):
        super(Markov, self).__init__()
        if word_list != None:
            for index, word in enumerate(word_list):
                if word not in self:
                    selected_index = index
                    next_word = word_list[selected_index + 1]
                    self[word] = [next_word]
                else:

                    selected_index = index
                    if index < len(word_list) -1:
                        next_word = word_list[selected_index + 1]
                        if next_word not in self[word]:
                            self[word].append(next_word)
            print(self)

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

if __name__ == '__main__':
    main()
