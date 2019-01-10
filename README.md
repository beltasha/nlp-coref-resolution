# nlp-coref-resolution
1. Take the ASOIF and HP books - Split into short “paragraphs”
  - done
2. Replace corefs with main mention -- within the chosen units
  - done
3. Recompute (retrain) word embedding models
  - https://github.com/gwohlgen/digitalhumanities_dataset_and_eval
4. Evaluate with the given scripts from the repo 
  - doesnt_match_evaluation.py and analogies_evaluation.py
## Project info
The project is designed to automatically replace pronouns with proper names, with the possibility of subsequent conversion into a Word2vec or Fast text format model, collecting data on the number of substitutions.
The project presents 2 main scripts:
handle_paragraph_coref_replacement.py
original_paragraph_coref_replacement.py


# General principle:
- Division of the text into paragraphs and their preprocessing
- Replacement pronouns
- Statistics collection
- Saving models


## Requirements
- Python 3
- Nltk
- Spacy
- Fasttext


## How to use this project
# Handle_paragraph_coref_replacement.py
Designed to replace pronouns with customizable number of sentences in one paragraph.
Use the command line:
Required:
"-in" input file file
"-out" output file name
"-pl" number of sentences in paragraph > 0
Optional:
"-w2v" save model in Word2vec format, output model name "output file name + _w2v.model" in the same directory as script
"-fasttext" save the model in Fasttext format, output model name "output file name +_fasttext.model" in the same directory as script
"-st" replacement statistics, information is contained at the end of the output file

# Original_paragraph_coref_replacement.py
Designed to replace pronouns in texts separated by "/ n / n". Also you can choose number of random paragraphs with a optinal size. 
Use the command line:
Required:
"-in" input file file
"-out" output file name
Optional:
"-cp" number of randomly taken paragraphs
"-w2v" save model in Word2vec format, output model name "output file name + _w2v.model" in the same directory as script
"-fasttext" save the model in Fasttext format, output model name "output file name +_fasttext.model" in the same directory as script
"-st" replacement statistics, information is contained at the end of the output file
"-pl" minimal number of sentences in paragraph> 0

Evaluate trained model using [this project](https://github.com/gwohlgen/digitalhumanities_dataset_and_eval)


## Results 
Results for w2v in folder w2v_results
Results for fasttext in folder w2v_fasttext

##Settings
w2v model training settings (min_count=5, size=300, workers=4, window=10, sg=1, negative=5)
fasttext model training settings default
