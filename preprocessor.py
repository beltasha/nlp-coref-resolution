import nltk
from nltk.stem.wordnet import WordNetLemmatizer

def preprocess(input_file, output_file):
    lmtzr = WordNetLemmatizer()
    tokenize_sentences = nltk.sent_tokenize(open(input_file, encoding= 'utf - 8').read())
    result = ""
    for sentence in tokenize_sentences:
        words_raw = nltk.word_tokenize(sentence)
        words = [word for word in words_raw if word.isalpha()]
        if len(words) > 0:
            clear_sentence = ''
            for word in words:
                clear_sentence += lmtzr.lemmatize(word) + ' '

            clear_sentence = clear_sentence.strip() + '. '
            result += clear_sentence

    clear_file = open(output_file,'wt', encoding='utf-8')
    clear_file.writelines(result)

if __name__ == "__main__":
    preprocess("book_combined_sentences.txt", "cleaned_hp.txt")
    preprocess("soiaf4books.txt", "cleaned_soiaf.txt")


