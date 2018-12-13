from nltk.tokenize import sent_tokenize
import en_coref_lg
import en_coref_md
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
            inner_counter = 0
        
        temp_paragraph += sentence + " "
        inner_counter += 1
    return paragraph_list


def train_model(sentences):
    return gensim.models.Word2Vec(sentences, min_count=5, size=300, workers=4, window=10, sg=1, negative=5)


def train_and_save_model(book_name):
    print(book_name + ' train model start')
    sentences = LineSentence(book_name +  ".txt")
    model = train_model(sentences)
    print(book_name + ' trained')
    model.wv.save_word2vec_format(fname=book_name + "_model.model", binary=False)
    print(book_name + ' saved')


def replace_corefs(paragraph_list):
    nlp = en_coref_lg.load()
    result_text = ""
    paragraphs_len = len(paragraph_list)
    print("Replacing corefs... Total number of paragraphs: " + str(paragraphs_len))
    counter = 1
    for paragraph in paragraph_list:
        print("Processing paragraph " + str(counter) + "/" + str(paragraphs_len))
        spacy_result = nlp(paragraph)
        result_text += spacy_result._.coref_resolved + " "
        counter += 1
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
    # text_hp = open('cleaned_hp.txt', 'r', encoding='utf8').read()
    text_soiaf = open('cleaned_soiaf.txt', 'r', encoding='utf8').read()

    #train on hp_book
    # coref_replacing(text_hp, "1_sent_hp", sentence_count=1)
    # train_and_save_model("1_sent_hp")
    # coref_replacing(text_hp, "4_sent_hp", sentence_count=4)
    # train_and_save_model("4_sent_hp")
    train_and_save_model("cleaned_hp")

    #train on soiaf
    # coref_replacing(text_soiaf, "1_sent_soiaf", sentence_count=1)
    # train_and_save_model("1_sent_soiaf")
    #coref_replacing(text_soiaf, "4_sent_soiaf", sentence_count=4)
    #train_and_save_model("4_sent_soiaf")
    train_and_save_model("cleaned_soiaf")
