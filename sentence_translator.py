import re
from grammar import apply_grammar_rules

def tokenize(sentence):
    return re.findall(r"\b\w+\b", sentence.lower())

def translate_sentence(sentence, dictionary):
    words = tokenize(sentence)
    translated = []

    for word in words:
        # Direct match
        if word in dictionary:
            translated.append(dictionary[word]["lagu"])
        else:
            # Grammar rule fallback
            guess = apply_grammar_rules(word, dictionary)
            if guess:
                translated.append(guess.split("→")[-1].strip())
            else:
                translated.append(f"[{word}]")  # Unknown word
    return " ".join(translated)