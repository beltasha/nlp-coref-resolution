from nltk.tokenize import sent_tokenize
import en_coref_lg
import nltk
import argparse
import fasttext_model_training
import w2v_model_training
import coref_statistics

def get_splitted_text(text, sentence_count):
    sentence_list = sent_tokenize(text)
    
    if sentence_count == 1:
        clear_paragraphs = []
        for sentence in sentence_list:
            tokens = nltk.word_tokenize(sentence)
            clear_paragraphs.append(' '.join(tokens))
        return clear_paragraphs
    
    temp_paragraph = ""
    paragraph_list = []
    inner_counter = 0
    for sentence in sentence_list:
        tokens = nltk.word_tokenize(sentence)
        clear_sentence = ""
        if len(tokens) > 0:
            for token in tokens:
                clear_sentence += token + " "
        if inner_counter == sentence_count:
            paragraph_list.append(temp_paragraph)
            temp_paragraph = ""
            inner_counter = 0
        temp_paragraph += clear_sentence + " "
        inner_counter += 1
    return paragraph_list


def replace_corefs(paragraph_list, statistics):
    nlp = en_coref_lg.load()
    result_text = ""
    paragraphs_len = len(paragraph_list)
    print("Replacing corefs... Total number of paragraphs: " + str(paragraphs_len))
    counter = 1
    replaced_coref_counter = 0
    error_main_mantion_pronoun = 0
    error_mention_not_pronoun = 0
    for paragraph in paragraph_list:

        print("Processing paragraph " + str(counter) + "/" + str(paragraphs_len))
        spacy_result = nlp(paragraph)
        result_text += spacy_result._.coref_resolved + " "
        counter += 1
        if statistics:
            result_stat = coref_statistics.count_of_replaced_pronouns(spacy_result)
            replaced_coref_counter += result_stat[0]
            error_main_mantion_pronoun += result_stat[1]
            error_mention_not_pronoun += result_stat[2]
    if statistics:
        result_text += "/n /n Count of correct raplaced pronouns: " + str(replaced_coref_counter)
        result_text += "/n Count of error: main mentions pronouns: " + str(error_main_mantion_pronoun)
        result_text += "/n Count of error: mention not a pronoun: " + str(error_mention_not_pronoun)
        print("Count of raplced pronouns: " + str(replaced_coref_counter))
        print("Count of error: main mentions pronouns: " + str(error_main_mantion_pronoun))
        print("Count of error: mention not a pronoun: " + str(error_mention_not_pronoun))
    return result_text


def coref_replacing(input_file, output_file, sentence_count, fast_text, word_2_vec, statistics):
    text = open(input_file, 'r', encoding='utf8').read()
    book_paragraph_list = get_splitted_text(text, sentence_count)
    print(input_file + ' splitted')
    book_replaced_corefs = replace_corefs(book_paragraph_list, statistics)
    open(output_file, "w", encoding='utf-8').writelines(book_replaced_corefs)
    print(input_file + ' corefs replaced')

    if fast_text:
        fasttext_model_training.train_model(output_file)

    if word_2_vec:
        w2v_model_training.train_and_save_model(output_file)


def create_parser():
    main_parser = argparse.ArgumentParser()
    main_parser.add_argument('-in', '--input_fname', required=True)
    main_parser.add_argument('-out', '--output_fname', required=True)
    main_parser.add_argument('-pl', '--paragraph_len', type=int, required=True)
    main_parser.add_argument('-ft', '--fast_text', action='store_true', default=False)
    main_parser.add_argument('-w2v', '--word_2_vec', action='store_true', default=False)
    main_parser.add_argument('-st', '--statistics', action='store_true', default=False)
    return main_parser


if __name__ == "__main__":
    parser = create_parser()
    namespace = parser.parse_args()
    coref_replacing(namespace.input_fname, namespace.output_fname, namespace.paragraph_len,
                    namespace.fast_text, namespace.word_2_vec, namespace.statistics)