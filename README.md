# nlp-coref-resolution
1. Take the ASOIF and HP books - Split into short “paragraphs”
  - done
2. Replace corefs with main mention -- within the chosen units
  - done
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
Results for w2v in folder w2v_results
Results for fasttext in folder w2v_fasttext

##Settings
w2v model training settings (min_count=5, size=300, workers=4, window=10, sg=1, negative=5)
fasttext model training settings default