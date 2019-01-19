
## General principle:


## Requirements
- [Python 3](https://www.python.org/)
- [Nltk](https://www.nltk.org/)
- [Spacy](https://spacy.io/)
- [Fasttext](https://fasttext.cc/)
- [Gensim](https://radimrehurek.com/gensim/)
- [Argparse](https://docs.python.org/2/howto/argparse.html)
- [NeuralCoref](https://github.com/huggingface/neuralcoref)

# How to use this project
## handle_paragraph_coref_replacement.py
Designed to replace pronouns with customizable number of sentences in one paragraph.

Use the command line

**Required:**

- `` -in `` input file file

- `` -out `` output file name

- `` -pl `` number of sentences in paragraph > 0

**Optional:**

- `` -w2v `` save model in Word2vec format, output model name "output file name + _w2v.model" in the same directory as script

- `` -ft `` save the model in Fasttext format, output model name "output file name +_fasttext.model" in the same directory as script

- `` -st `` replacement statistics, information is contained at the end of the output file

**Example:**
```python
python handle_paragraph_coref_replacement.py -in in.txt -out out.txt -pl 1 -w2v -ft -st
```
## original_paragraph_coref_replacement.py
Designed to replace pronouns in texts separated by "/ n / n". Also you can choose number of random paragraphs with a optinal size. 

Use the command line

**Required:**

- `` -in `` input file file

- `` -out `` output file name

**Optional:**

- `` -pl ``   minimal number of sentences in paragraph> 0
- `` -cp `` number of randomly taken paragraphs

- `` -w2v `` save model in Word2vec format, output model name "output file name + _w2v.model" in the same directory as script

- `` -ft  ``save the model in Fasttext format, output model name "output file name +_fasttext.model" in the same directory as script

- `` -st `` replacement statistics, information is contained at the end of the output file


**Example:**
```python
python original_paragraph_coref_replacement.py -in in.txt -out out.txt -cp 20 -pl 3 -w2v -ft -st
```

`Evaluate trained model using [this project](https://github.com/gwohlgen/digitalhumanities_dataset_and_eval)

## Statistics
Statistics is at the end of the output file

- `"replace_counts"` number of replcements pronouns on proper names

- `"error_main_mantion_pronoun"` number of error replcements pronouns on pronouns

- `"error_mentiont_not_pronoun"` number not pronouns replacements

## Results 


