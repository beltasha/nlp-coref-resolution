import fasttext


def train_model(book_name):
    print(book_name + ' fasttext model train start')
    model_name = book_name.split('.')
    fasttext.skipgram(book_name, model_name[0] + "_fasttext_model")
    print(book_name + " fasttext model saved")

