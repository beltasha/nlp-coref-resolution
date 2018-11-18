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

