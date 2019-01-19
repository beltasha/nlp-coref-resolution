import nltk
import random
import handle_paragraph_coref_replacement
import argparse
import fasttext_model_training
import w2v_model_training


def split_paragraphs(input_file, output_file, count_of_paragraph, minimal_paragraph_len, fast_text, word_2_vec, statistics):
        #splitting text to  paragraphs
        with open(input_file, encoding='utf-8') as input:
            text = input.read()
        print("Paragraph tokenize start")
        paragraphs_raw = text.split("\n\n")
        paragraphs = []
        #clean empty paragraphs
        for paragraph in paragraphs_raw:
            if paragraph != "" and not paragraph.isspace():
                paragraphs.append(paragraph)
        #creating gold standart paragraphs
        if count_of_paragraph is not None and minimal_paragraph_len is not None:
            gold_paragraphs = []
            while len(gold_paragraphs) < count_of_paragraph:
                current_paragraph = random.choice(paragraphs)
                #check minimal sentences count in paragraph
                if len(nltk.sent_tokenize(current_paragraph)) > minimal_paragraph_len:
                    gold_paragraphs.append(current_paragraph)
            shuffled_paragraphs = gold_paragraphs
        else:
            shuffled_paragraphs = paragraphs
        cleaned_paragraphs = []
        print("Paragraph clean start")
        #clear paragraphs
        for paragraph in shuffled_paragraphs:
            current_paragraph = ""
            sentences = nltk.sent_tokenize(paragraph)
            for sentence in sentences:
                tokens = nltk.word_tokenize(sentence)
                if len(tokens) > 0:
                    for token in tokens:
                        current_paragraph += token + ' '
            cleaned_paragraphs.append(current_paragraph)
        print("Replacing coref start")
        #replacing corefs
        paragraphs_replaced_corefs = handle_paragraph_coref_replacement.replace_corefs(cleaned_paragraphs, statistics)
        output = open(output_file, 'wt', encoding='UTF8')
        output.writelines(paragraphs_replaced_corefs)
        output.close()
        #saving models
        if fast_text:
            fasttext_model_training.train_model(output_file)

        if word_2_vec:
            w2v_model_training.train_and_save_model(output_file)


def create_parser():
    # working with command line
    main_parser = argparse.ArgumentParser()
    main_parser.add_argument('-in', '--input_fname', required=True)
    main_parser.add_argument('-out', '--output_fname', required=True)
    main_parser.add_argument('-cp', '--count_of_paragraphs', type=int)
    main_parser.add_argument('-pl', '--minimal_paragraph_len', type=int)
    main_parser.add_argument('-ft', '--fast_text', action='store_true', default=False)
    main_parser.add_argument('-w2v', '--word_2_vec', action='store_true', default=False)
    main_parser.add_argument('-st', '--statistics', action='store_true', default=False)
    return main_parser


if __name__ == "__main__":
    # work with command line and start replacing with given param
    parser = create_parser()
    namespace = parser.parse_args()
    split_paragraphs(namespace.input_fname, namespace.output_fname, namespace.count_of_paragraphs,
                     namespace.minimal_paragraph_len, namespace.fast_text, namespace.word_2_vec, namespace.statistics)


