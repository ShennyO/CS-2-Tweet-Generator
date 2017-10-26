import random


words = ["Kaichi", "Chris", "Poops", "lots", "of", "eats", "super"]

def create_quote():
    word = []
    for x in range(len(words)):
        rand_index = random.randint(0, len(words) - 1)
        word.append(words[rand_index])

    return word

if __name__ == '__main__':
    quote = create_quote()
    quote = ' '.join(quote)
    print(quote)
