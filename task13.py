import spacy
nlp = spacy.load('en_coref_md') # or en_coref_lg

def evaluate_clusters (current_doc, current_gold):
    # clusters "mains" found by spacy
    current_doc_mains = [c.main.string for c in doc._.coref_clusters]
    print('\ncurrent_doc_mains:', current_doc_mains)
    
    # this will contrain: (len(gold_mentions), precision, recall, f1)
    cluster_results = []
    
    for gold_main, gold_mentions in current_gold.items():
        print('gold_main', gold_main)
        
        # 1.) find if the gold_main is in the document custering
        gold_in_spacy, found_cluster = False, None
        
        for cluster in doc._.coref_clusters:
            #print(cluster.main.string, gold_main, type(cluster.main.string), type(gold_main),
            #      len(cluster.main.string), len(gold_main))
            if cluster.main.string.strip() == gold_main.strip():
                print('Found cluster main:', gold_main)
                gold_in_spacy = True
                found_cluster = cluster
            
        if gold_in_spacy:    
            ## precision: number of cluster_items which are in the gold cluster
            ## TODO .. extend this to check for the spans of mentions
            found_mentions = [mention for mention in found_cluster.mentions 
                                  if mention.string.strip() in gold_mentions]
                
            # print('found_mentions', found_mentions)
            precision = len(found_mentions) / len(found_cluster.mentions)
            recall = len(found_mentions) / len(gold_mentions)
            f1 = 2* (precision*recall) / (precision + recall)
            print('P, R, F1:', precision, recall, f1)

            cluster_results.append((len(gold_mentions), precision, recall, f1))
        else:
            ## TODO add zero result for Precision and Recall for this cluster
            cluster_results.append((len(gold_mentions), 0, 0, 0))
                
    pprint(cluster_results)
                
    ## compute final b-cubed
    b3_avg = np.mean([f1 for _,_,_,f1 in cluster_results])
    print('b3_avg', b3_avg)
    
    total_num_gold = np.sum([len(gold_mentions) for gold_main, gold_mentions in current_gold.items()])
    b3_weighted = np.sum([f1*len_gold/total_num_gold for len_gold,_,_,f1 in cluster_results])
    print('b3_weighted', b3_weighted)

import numpy as np
from pprint import pprint

## define the gold clusters for all your selected paragraphs
gold_clusters = [
    {'Harry': ['Harry', 'his'],
     'Sirius': ['Sirius', 'his']},
    {'Harry': ['Harry', 'He', 'he']},
    {'James': ['James'],
     'Lupin': ['Lupin', 'he', 'himself'],
     'Harry': ['Harry', 'he', 'He', 'his', 'him'],
     'Sirius': ['Sirius']},
    {'Mr. Borgin': ['Mr. Borgin', 'You'],
     'Mr. Malfoy': ['Mr. Malfoy', 'I']},
    {'Ron': ['Ron', 'I', 'him', 'He', 'he', 'his', 'you'],
     'Harry': ['Harry'],
     'Lavender': ['Lavender', 'Lav-Lav']},
    {'Ron': ['Ron', 'him', 'he'],
     'Hermione': ['Hermione', 'her'],
     'Harry': ['Harry'],
     'Crabbe': ['Crabbe']},
    {'Snape': ['I', 'his', 'His'],
     'Hermione': ['Hermione', 'her', 'I'],
     'Harry': ['Harry']},
    {'Harry': ['Harry', 'He', 'he']},
    {'Harry , Ron , and Hermione': ['Harry , Ron , and Hermione', 'they']},
    {'Snape': ['Snape', 'his', 'His', 'He', 'he', 'Severus'],
     'Narcissa': ['Narcissa', 'her', 'you', 'She', 'I'],
     'Wormtail': ['Wormtail']},
    {'Krum': ['Krum', 'he', 'his'],
     'Harry': ['Harry'],
     'Cedric': ['Cedric', 'his', 'you']},
    {'Petunia': ['Petunia', 'she', 'She', 'her'],
     'Dudley': ['Dudley', 'his'],
     'Vernon': ['Vernon'],
     'Harry': ['Harry', 'his']
    },
    {'Harry': ['Harry', 'his', 'He', 'he']},
    {'Potter': ['Potter', 'you']},
    {'Harry': ['Harry', 'he', 'his'],
     'Hermione': ['Hermione', 'her', 'she'],
     'Ginny': ['Ginny'],
     'Sirius': ['Sirius']},
    {'Hermione': ['Hermione', 'She', 'she']},
    {'Harry': ['Harry', 'he']},
    {'Hagrid': ['Hagrid', 'he']},
    {'Kreacher': ['Kreacher', 'he']},
    {'Harry': ['Harry', 'his'],
     'Dursley': ['Dudley', 'Dursleys'],
     'Petunia': ['Petunia'],
     'Dedalus': ['Dedalus']},
]

with open('hp_cleaned.txt', encoding='utf8') as f:
    content = f.readlines()

for index, paragraph in enumerate(content, start=0):
    doc = nlp(paragraph)
    evaluate_clusters(doc, gold_clusters[index])