def count_of_replaced_pronouns(spacy_result):
    clusters = spacy_result._.coref_clusters
    replace_counts = 0
    error_main_mantion_pronoun = 0
    error_mentiont_not_pronoun = 0
    if clusters is not None:
        for cluster in clusters:
            if cluster[0].lemma_ != '-PRON-':
                for word in cluster.mentions[1:]:
                    if word.lemma_ == '-PRON-':
                        replace_counts += 1
                    else:
                        error_mentiont_not_pronoun += 1
            else:
                error_main_mantion_pronoun += 1
                for word in cluster.mentions[1:]:
                    if word.lemma_ != '-PRON-':
                        error_mentiont_not_pronoun += 1
    return [replace_counts, error_main_mantion_pronoun, error_mentiont_not_pronoun]

