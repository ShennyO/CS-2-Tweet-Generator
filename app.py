from flask import Flask
import dictionary_words

app = Flask(__name__)

@app.route('/')
def return_random_sentence():
    sentence = dictionary_words.generate_random_sentence(20)
    return sentence




if __name__ == "__main__":
   app.run(debug=True)
