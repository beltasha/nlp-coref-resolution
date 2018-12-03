# nlp-coref-resolution
1. Take the ASOIF and HP books - Split into short “paragraphs”
  - We will do co-ref resolution only within those “paragraphs”
  - Start eg. with only sentences  -- later we will add other units like short paragraphs
2. Replace corefs with main mention -- within the chosen units
  - Use spacy / huggingface coref for this?!
3. Recompute (retrain) word embedding models
  - https://github.com/gwohlgen/digitalhumanities_dataset_and_eval
4. Evaluate with the given scripts from the repo 
  - doesnt_match_evaluation.py and analogies_evaluation.py



## How to use this project
1. Perform preprocessing with preprocessor.py
```python
preprocess("soiaf4books.txt", "cleaned_soiaf.txt")
```
2. Train model
```python
text_soiaf = open('cleaned_soiaf.txt', 'r', encoding='utf8').read()
coref_replacing(text_soiaf, "1_soiaf_hp", sentence_count=1)
train_and_save_model("1_sent_soiaf")
```
3. Evaluate trained model using [this project](https://github.com/gwohlgen/digitalhumanities_dataset_and_eval)


## Results

*ASOIF*

* Analogies evaluation:

| 1-sentence paragraphs| 4-sentence paragraphs|
| ------------- |:-------------:|
|1_sent_soiaf_model  &  28.97 & 1.11 & 6.67 & 0.0 & 20.0 & 24.7  | 4_sent_soiaf_model  &  25.59 & 0.0 & 13.33 & 0.0 & 16.67 & 21.73 |




* Doesnt_match evaluation:

| 1-sentence paragraphs| 4-sentence paragraphs|
| ------------- |:-------------:|
|1_sent_soiaf_model                &  79.38 & 50.76 & 75.36 & 68.29 & 61.38   | 4_sent_soiaf_model                &  83.12 & 53.52 & 76.16 & 76.57 & 64.3 |


Coref resolution for 4-sentence paragraphs shows a slightly better results, expecially for doesnt_match evaluation, though it's not that obvious for analogies evaluation.