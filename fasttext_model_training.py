import fasttext


def train_model(book_name):
    print(book_name + ' fasttext model train start')
    # extracting  file name
    model_name = book_name.split('.')
    # train and save model
    fasttext.skipgram(book_name, model_name[0] + "_fasttext_model")
    print(book_name + " fasttext model saved")

train_model('result_soiaf_1.txt')