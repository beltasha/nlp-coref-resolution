def count_of_replaced_pronouns(spacy_result):
    clusters = spacy_result._.coref_clusters
    count = 0
    if clusters is not None:
        for cluster in clusters:
            if cluster[0].lemma_ != '-PRON-':
                for word in cluster.mentions:
                    if word.lemma_ == '-PRON-':
                        count += 1
    return count
