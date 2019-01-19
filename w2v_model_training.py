import gensim
from gensim.models.word2vec import LineSentence


def train_model(sentences):
    #training w2v model
    return gensim.models.Word2Vec(sentences, min_count=5, size=300, workers=4, window=10, sg=1, negative=5)


def train_and_save_model(book_name):
    print(book_name + ' w2v model train start')
    sentences = LineSentence(book_name)
    model = train_model(sentences)
    print(book_name + ' w2v model trained')
    # extracting  file name
    model_name = book_name.split('.')
    # saving model
    model.wv.save_word2vec_format(fname=model_name[0] + "_w2v.model", binary=False)
    print(book_name + ' w2v model saved')
