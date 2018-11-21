
from nltk.tokenize import sent_tokenize
import en_coref_lg
import gensim
from gensim.models.word2vec import LineSentence


def get_splitted_text(text, sentence_count=1):
    sentence_list = sent_tokenize(text)
    
    if sentence_count == 1:
        return sentence_list
    
    temp_paragraph = ""
    paragraph_list = []
    inner_counter = 0
    for sentence in sentence_list:
        if inner_counter == sentence_count:
            paragraph_list.append(temp_paragraph)
            temp_paragraph = "" 
        
        temp_paragraph += sentence + " "
        inner_counter += 1
    return paragraph_list


def train_model(sentences):
    return gensim.models.Word2Vec(sentences, min_count=5, size=300, workers=4, window=10, sg=1, negative=5)


def train_and_save_model(book_name):
    print(book_name + ' train model start')
    sentences = LineSentence(book_name +  "_replaced_corefs.txt")
    model = train_model(sentences)
    print(book_name + ' trained')
    model.wv.save_word2vec_format(fname=book_name + "_model.model", binary=False)
    print(book_name + ' saved')


def replace_corefs(paragraph_list):
    nlp = en_coref_lg.load()
    result_text = ""
    for paragraph in paragraph_list:
        spacy_result = nlp(paragraph)
        result_text += spacy_result._.coref_resolved + " "
    return result_text


def coref_replacing(book_text, book_name, sentence_count=1):
    book_paragraph_list = get_splitted_text(book_text, sentence_count)
    print(book_name + ' book splitted')
    book_replaced_corefs = replace_corefs(book_paragraph_list)
    book_file_name = book_name +  "_replaced_corefs.txt"
    print(book_replaced_corefs)
    open(book_file_name, "w", encoding='utf-8').writelines(book_replaced_corefs)
    print(book_name +'book corefs replaced')


if __name__ == "__main__":
    # split data
    text_hp = open('book_combined_sentences.txt', 'r', encoding='utf8').read()
    text_soiaf = open('soiaf4books.txt', 'r', encoding='utf8').read()

    paragraph_list = get_splitted_text(text_hp)
    print(paragraph_list[0])
    paragraph_list = get_splitted_text(text_hp, 5)
    print(paragraph_list[0])

    print(paragraph_list[:10])
    print(replace_corefs(paragraph_list)[:1000])
    #train on hp_book
    coref_replacing(text_hp, "hp")
    train_and_save_model("hp")
    #train on soiaf
    coref_replacing(text_soiaf, "soiaf")
    train_and_save_model("soiaf")

