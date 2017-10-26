import random


words = ["Kaichi", "Chris", "Poops", "lots", "of", "eats", "super"]

def create_quote():
    word = []
    used_random_numbers = []
    number_of_words = 0
    while number_of_words < len(words):
        rand_index = random.randint(0, len(words) - 1)

        if rand_index not in used_random_numbers:
            word.append(words[rand_index])
            used_random_numbers.append(rand_index)
            number_of_words +=1


    return word

if __name__ == '__main__':
    quote = create_quote()
    quote = ' '.join(quote)
    print(quote)
