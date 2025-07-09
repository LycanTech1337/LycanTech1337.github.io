def apply_grammar_rules(word, dictionary):
    if word.endswith("s"):
        singular = word[:-1]
        if singular in dictionary:
            return f"{singular} (plural) → {dictionary[singular]['lagu']}+ar"
    elif word.endswith("ed"):
        verb = word[:-2]
        if verb in dictionary and dictionary[verb]['pos'] == 'verb':
            return f"{verb} (past) → {dictionary[verb]['lagu']}+ta"
    elif word.endswith("ing"):
        verb = word[:-3]
        if verb in dictionary and dictionary[verb]['pos'] == 'verb':
            return f"{verb} (progressive) → {dictionary[verb]['lagu']}+in"
    return None