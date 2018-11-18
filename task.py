
from nltk.tokenize import sent_tokenize

def get_splitted_text(text, sentence_count=1):
    sentence_list = sent_tokenize(text)
    
    if sentence_count == 1:
        return sentence_list
    
    temp_paragraph = []
    paragraph_list = []
    for sentence in sentence_list:
        if len(temp_paragraph) == sentence_count:
            paragraph_list.append(temp_paragraph)
            temp_paragraph = []
        
        temp_paragraph.append(sentence)
    
    return paragraph_list


if __name__ == "__main__":
    text_hp = open('book_combined_sentences.txt', 'r', encoding='utf8').read()
    text_soiaf = open('soiaf4books.txt', 'r', encoding='utf8').read()
    paragraph_list = get_splitted_text(text_hp)
    print(paragraph_list[0])
    paragraph_list = get_splitted_text(text_hp, 5)
    print(paragraph_list[0])
