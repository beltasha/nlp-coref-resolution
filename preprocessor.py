import nltk

def preprocess(input_file, output_file):
    with open(input_file, encoding='utf-8') as input:
        text = input.read()
    filtered_sentences = []
    sentences = nltk.sent_tokenize(text)
    for sentence in sentences:
        tokens = nltk.word_tokenize(sentence)
        if len(tokens) > 0:
            filtered_sentences.append(' '.join(tokens))

    output = open(output_file, 'wt', encoding='UTF8')
    output.writelines(sentence + '.\n' for sentence in filtered_sentences)
    output.close()

if __name__ == "__main__":
    preprocess("book_combined_sentences.txt", "cleaned_hp.txt")
    preprocess("soiaf4books.txt", "cleaned_soiaf.txt")


