import spacy
nlp = spacy.load('en_coref_md') # or en_coref_lg

IS_SPAN_CHECKING = True

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
            
            if (IS_SPAN_CHECKING):
                found_mentions = [mention for mention in found_cluster.mentions 
                                if mention.string.strip() in gold_mentions
                                and mention.start in gold_mentions[mention.string.strip()]] # check for the spans of mentions
            else:
                found_mentions = [mention for mention in found_cluster.mentions 
                                if mention.string.strip() in gold_mentions]
            
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
    {'Harry': ['Harry', 'He', 'his']},
    {'James': ['James'],
     'Lupin': ['Lupin', 'he', 'himself'],
     'Harry': ['Harry', 'he', 'He', 'his', 'him']},
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
    {'Hagrid': ['Hagrid', 'he'],
    'Harry': ['Harry'],
    'Ron': ['Ron'],
    'Hermione': ['Hermione']
    },
    {'Kreacher': ['Kreacher', 'he', 'He'],
     'Harry': ['Harry']
    },
    {'Harry': ['Harry', 'his'],
     'Petunia': ['Petunia'],
     'Dedalus': ['Dedalus']},
]

ggold_clusters_with_spans = [ 
{'Harry': {'Harry': [6], 'He': [14, 27], 'his': [17]}}, 
{'James': {'James': [1]}, 
'Lupin': {'Lupin':[4], 'he':[11], 'himself':[21]}, 
'Harry': {'Harry':[31], 'he': [38], 'He': [45], 'his': [55], 'him': [62]}}, 
{'Mr. Borgin': {'Mr. Borgin': [34], 'You': [1]}, 
'Mr. Malfoy': {'Mr. Malfoy': [18], 'I': [40]}}, 
{'Ron': {'Ron': [7, 33, 74], 'I': [0, 66, 71], 'him': [12], 'He': [13], 'he': [22, 38], 'his': [43], 'you': [50]}, 
'Harry': {'Harry': [9, 53]}, 
'Lavender': {'Lavender': [36], 'Lav-Lav': [37]}}, 
{'Ron': {'Ron': [4], 'him': [85], 'he': [65, 73, 93, 99,]}, 
'Hermione': {'Hermione': [25, 54], 'her': [37]}, 
'Harry': {'Harry': [81]}, 
'Crabbe': {'Crabbe': [87, 90]}}, 
{'Snape': {'Snape': [11], 'I': [0], 'his': [23], 'His': [56]}, 
'Hermione': {'Hermione': [25], 'her': [28, 36, 42], 'I': [44, 51]}, 
'Harry': {'Harry': [73]}}, 
{'Harry': {'Harry': [7], 'He': [25, 51], 'he': [65]}}, 
{'Harry , Ron , and Hermione': {'Harry , Ron , and Hermione': [0], 'they': [33]}}, 
{'Snape': {'Snape': [0, 40], 'his': [10], 'He': [41], 'he': [53], 'Severus': [71, 74]}, 
'Narcissa': {'Narcissa': [61], 'her': [7], 'She': [62], 'I': [49, 72, 80]}, 
'Wormtail': {'Wormtail': [31]}}, 
{'Krum': {'Krum': [3], 'he': [7], 'his': [11]}, 
'Harry': {'Harry': [22, 45]}, 
'Cedric': {'Cedric': [26, 49, 53], 'his': [36], 'you': [42]}}, 
{'Petunia': {'Petunia': [1, 43, 45], 'she': [5], 'She': [8], 'her': [15, 18]}, 
'Dudley': {'Dudley': [14, 48], 'his': [53, 55]}, 
'Vernon': {'Vernon': [35]}, 
'Harry': {'Harry': [63], 'his': [66, 70]} 
}, 
{'Harry': {'Harry': [0], 'his': [6, 10, 31], 'He': [17, 33], 'he': [35]}}, 
{'Potter': {'Potter': [7], 'you': [16, 29]}}, 
{'Harry': {'Harry': [0, 74], 'he': [16, 18, 33, 46, 93], 'import spacy
nlp = spacy.load('en_coref_md') # or en_coref_lg

IS_SPAN_CHECKING = True

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
            
            if (IS_SPAN_CHECKING):
                
                for mention in found_cluster.mentions:
                    if mention.string.strip() in gold_mentions:
                        print(mention.string, mention.start)
                        print(gold_mentions[mention.string.strip()])
                found_mentions = [mention for mention in found_cluster.mentions 
                                if mention.string.strip() in gold_mentions
                                and mention.start in gold_mentions[mention.string.strip()]] # check for the spans of mentions
            else:
                found_mentions = [mention for mention in found_cluster.mentions 
                                if mention.string.strip() in gold_mentions]
            
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
    {'Harry': ['Harry', 'He', 'his']},
    {'James': ['James'],'Lupin': ['Lupin', 'he', 'himself'],'Harry': ['Harry', 'he', 'He', 'his', 'him']},
    {'Mr. Borgin': ['Mr. Borgin', 'You'],'Mr. Malfoy': ['Mr. Malfoy', 'I']},
    {'Ron': ['Ron', 'I', 'him', 'He', 'he', 'his', 'you'],'Harry': ['Harry'],'Lavender': ['Lavender', 'Lav-Lav']},
    {'Ron': ['Ron', 'him', 'he'],'Hermione': ['Hermione', 'her'],'Harry': ['Harry'],'Crabbe': ['Crabbe']},
    {'Snape': ['I', 'his', 'His'],'Hermione': ['Hermione', 'her', 'I'],'Harry': ['Harry']},
    {'Harry': ['Harry', 'He', 'he']},
    {'Harry , Ron , and Hermione': ['Harry , Ron , and Hermione', 'they']},
    {'Snape': ['Snape', 'his', 'His', 'He', 'he', 'Severus'],'Narcissa': ['Narcissa', 'her', 'you', 'She', 'I'],'Wormtail': ['Wormtail']},
    {'Krum': ['Krum', 'he', 'his'],'Harry': ['Harry'],'Cedric': ['Cedric', 'his', 'you']},
    {'Harry': ['Harry', 'his', 'He', 'he']},
    {'Petunia': ['Petunia', 'she', 'She', 'her'],'Dudley': ['Dudley', 'his'],'Vernon': ['Vernon'],'Harry': ['Harry', 'his']},
    {'Potter': ['Potter', 'you']},
    {'Harry': ['Harry', 'he', 'his'],'Hermione': ['Hermione', 'her', 'she'],'Ginny': ['Ginny'],'Sirius': ['Sirius']},
    {'Hermione': ['Hermione', 'She', 'she']},
    {'Harry': ['Harry', 'he']},
    {'Hagrid': ['Hagrid', 'he'],'Harry': ['Harry'],'Ron': ['Ron'],'Hermione': ['Hermione']},
    {'Kreacher': ['Kreacher', 'he', 'He'],'Harry': ['Harry']},
    {'Harry': ['Harry', 'his'],'Petunia': ['Petunia'],'Dedalus': ['Dedalus']},
]

gold_clusters_with_spans = [ 
{'Harry': {'Harry': [6], 'He': [16, 33], 'his': [19]}}, 
{'James': {'James': [1]}, 
'Lupin': {'Lupin':[6], 'he':[17], 'himself':[27]}, 
'Harry': {'Harry':[39], 'he': [47], 'He': [55], 'his': [55], 'him': [75]}}, 
{'Mr. Borgin': {'Mr. Borgin': [34], 'You': [1]}, 
'Mr. Malfoy': {'Mr. Malfoy': [18], 'I': [40]}}, 
{'Ron': {'Ron': [11, 41, 97], 'I': [0, 66, 71], 'him': [12], 'He': [13], 'he': [22, 38], 'his': [66], 'you': [50]}, 
'Harry': {'Harry': [14, 70]}, 
'Lavender': {'Lavender': [36], 'Lav-Lav': [37]}}, 
{'Ron': {'Ron': [4], 'him': [85], 'he': [65, 73, 93, 99,]}, 
'Hermione': {'Hermione': [44, 66], 'her': [37]}, 
'Harry': {'Harry': [81]}, 
'Crabbe': {'Crabbe': [114, 118]}}, 
{'Snape': {'Snape': [11], 'I': [0], 'his': [23], 'His': [66]}, 
'Hermione': {'Hermione': [25], 'her': [28, 36, 42], 'I': [44, 51]}, 
'Harry': {'Harry': [73]}}, 
{'Harry': {'Harry': [7], 'He': [25, 51], 'he': [65]}}, 
{'Harry , Ron , and Hermione': {'Harry , Ron , and Hermione': [0], 'they': [33]}}, 
{'Snape': {'Snape': [0, 40], 'his': [10], 'He': [41], 'he': [53], 'Severus': [71, 74]}, 
'Narcissa': {'Narcissa': [61], 'her': [7], 'She': [62], 'I': [49, 72, 80]}, 
'Wormtail': {'Wormtail': [31]}}, 
{'Krum': {'Krum': [3], 'he': [7], 'his': [11]}, 
'Harry': {'Harry': [27, 56]}, 
'Cedric': {'Cedric': [26, 61, 70], 'his': [36], 'you': [42]}}, 
{'Petunia': {'Petunia': [1, 43, 45], 'she': [5], 'She': [8], 'her': [15, 18]}, 
'Dudley': {'Dudley': [14, 48], 'his': [66, 69]}, 
'Vernon': {'Vernon': [35]}, 
'Harry': {'Harry': [63], 'his': [82, 88]} 
}, 
{'Harry': {'Harry': [0], 'his': [6, 10, 31], 'He': [17, 33], 'he': [35]}}, 
{'Potter': {'Potter': [7], 'you': [16, 29]}}, 
{'Harry': {'Harry': [0, 74], 'he': [16, 18, 33, 46, 93], 'his': [23, 26, 30, 37, 44]}, 
'Hermione': {'Hermione': [51, 77], 'her': [53, 80, 87, 95], 'she': [63]}, 
'Ginny': {'Ginny': [68]}, 
'Sirius': {'Sirius': [103]}}, 
{'Hermione': {'Hermione': [18], 'She':[30], 'she': [45]}}, 
{'Harry': {'Harry': [10], 'he': [13]}}, 
{'Hagrid': {'Hagrid': [4], 'he': [17]}, 
'Harry': {'Harry': [7]}, 
'Ron': {'Ron': [9]}, 
'Hermione': {'Hermione': [12]} 
}, 
{'Kreacher': {'Kreacher': [1], 'he': [29], 'He': [43]}, 
'Harry': {'Harry': [12]} 
}, 
{'Harry': {'Harry': [0], 'his': [5]}, 
'Dursley': {'Dursleys': [17, 29]}, 
'Petunia': {'Petunia': [36]}, 
'Dudley': {'Dudley': [38]}}, 

]

## define the gold clusters for all your selected paragraphs
with open('hp_paragraphs.txt', encoding='utf8') as f:
    content = f.readlines()

for index, paragraph in enumerate(content, start=0):
    doc = nlp(paragraph)
    if (IS_SPAN_CHECKING):
        if (index <= len(gold_clusters_with_spans) - 1):
            evaluate_clusters(doc, gold_clusters_with_spans[index])
    else:
        if (index <= len(gold_clusters) - 1):
            evaluate_clusters(doc, gold_clusters[index])his': [23, 26, 30, 37, 44]}, 
'Hermione': {'Hermione': [51, 77], 'her': [53, 80, 87, 95], 'she': [63]}, 
'Ginny': {'Ginny': [68]}, 
'Sirius': {'Sirius': [103]}}, 
{'Hermione': {'Hermione': [18], 'She':[30], 'she': [45]}}, 
{'Harry': {'Harry': [10], 'he': [13]}}, 
{'Hagrid': {'Hagrid': [4], 'he': [17]}, 
'Harry': {'Harry': [7]}, 
'Ron': {'Ron': [9]}, 
'Hermione': {'Hermione': [12]} 
}, 
{'Kreacher': {'Kreacher': [1], 'he': [29], 'He': [43]}, 
'Harry': {'Harry': [12]} 
}, 
{'Harry': {'Harry': [0], 'his': [5]}, 
'Petunia': {'Petunia': [36]}, 
'Dudley': {'Dudley': [38]}}, 

]

## define the gold clusters for all your selected paragraphs
with open('hp_cleaned.txt', encoding='utf8') as f:
    content = f.readlines()

for index, paragraph in enumerate(content, start=0):
    doc = nlp(paragraph)
    if (IS_SPAN_CHECKING):
        if (index <= len(gold_clusters_with_spans) - 1):
            evaluate_clusters(doc, gold_clusters_with_spans[index])
    else:
        if (index <= len(gold_clusters) - 1):
            evaluate_clusters(doc, gold_clusters[index])