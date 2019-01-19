def count_of_replaced_pronouns(spacy_result):
    clusters = spacy_result._.coref_clusters
    replace_counts = 0
    error_main_mantion_pronoun = 0
    error_mentiont_not_pronoun = 0
    if clusters is not None:
        for cluster in clusters:
            #looking for non pronouns main mentions
            if cluster[0].lemma_ != '-PRON-':
                for word in cluster.mentions[1:]:
                    #count a right replace
                    if word.lemma_ == '-PRON-':
                        replace_counts += 1
                    else:
                    #count not pronouns mentions
                        error_mentiont_not_pronoun += 1
            else:
                # main mantion pronoun it's a mistake!
                error_main_mantion_pronoun += 1
                for word in cluster.mentions[1:]:
                    if word.lemma_ != '-PRON-':
                        # count not pronouns mentions for this case
                        error_mentiont_not_pronoun += 1
    return [replace_counts, error_main_mantion_pronoun, error_mentiont_not_pronoun]


