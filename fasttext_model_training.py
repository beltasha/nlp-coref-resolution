import fasttext
def train_model(book_name):
    print(book_name + ' train model start')
    fasttext.skipgram(book_name + ".txt", book_name + "_fasttext_model")
    print(book_name + "_fasttext model saved")

if __name__ == "__main__":
    train_model("1_sent_hp_replaced_corefs")
    train_model("4_sent_hp_replaced_corefs")
    train_model("1_sent_soiaf_replaced_corefs")
    train_model("4_sent_soiaf_replaced_corefs")
    train_model("cleaned_hp")
    train_model("cleaned_soiaf")