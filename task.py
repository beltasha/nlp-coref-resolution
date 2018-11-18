
from nltk.tokenize import sent_tokenize
import en_coref_sm

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


if __name__ == "__main__":
    # split data
    text_hp = open('book_combined_sentences.txt', 'r', encoding='utf8').read()
    text_soiaf = open('soiaf4books.txt', 'r', encoding='utf8').read()
    
    paragraph_list = get_splitted_text(text_hp)
    print(paragraph_list[0])
    paragraph_list = get_splitted_text(text_hp, 5)
    print(paragraph_list[0])

    # replace corefs
    nlp = en_coref_sm.load()
    result_text = ""
    for paragraph in paragraph_list:
        spacy_result = nlp(paragraph)
        result_text += spacy_result._.coref_resolved + " "

    print(paragraph_list[:10])
    print(result_text[:1000])

