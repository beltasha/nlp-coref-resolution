
## General principle:
The task of the project is to find all expressions that refer to the same entity in a text. In other words the programm will detect a pronoun in a corpus and replace it with a related name. Futhermore, the next step will convert the preprocessed text into the Word2vec or Fast text format model. Afterwards evaluate the results. 
The results are presented here: https://docs.google.com/spreadsheets/d/13vElCAhiOShK7PNgNVpLHSexgtcWHwIXFO4RRFOgGeU/edit#gid=909973966

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
 Average frequences of terms in datasets before and after coref resolution
 
 ![Harry Potter](https://github.com/beltasha/nlp-coref-resolution/blob/master/charts/Harry%20Potter%20Frequence.png)
 ![A song of ice and fire](https://github.com/beltasha/nlp-coref-resolution/blob/master/charts/A%20Song%20of%20Ice%20and%20Fire%20Frequence.png)
 
 Analogies and doesn't matches average evaluation results
 ![Harry Potter analogies](https://github.com/beltasha/nlp-coref-resolution/blob/master/charts/Harry%20Potter.%20Analogies.png)
 ![Harry Potter doesn't match](https://github.com/beltasha/nlp-coref-resolution/blob/master/charts/Harry%20Potter.%20Doesn't%20match.png)
 ![A sonf of ice and fire analogies](https://github.com/beltasha/nlp-coref-resolution/blob/master/charts/A%20song%20of%20ice%20and%20fire.%20Analogies.png)
 ![A sonf of ice and fire doesn't match](https://github.com/beltasha/nlp-coref-resolution/blob/master/charts/A%20song%20of%20ice%20and%20fire.%20Doesn't%20match.png)
 
 Correctness of the coref via B-cubed metric with and without checking the spans of the gold annotations
 
 Errors analysys
 
## Conclusions
Coref resolution results have strong dependences on text dividing. Good paragraphs dividing decreases number of errors for Coref resolution. It works better with text dividing by original paragraphs

