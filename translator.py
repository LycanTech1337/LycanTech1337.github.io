from grammar import apply_grammar_rules
from utils import reverse_dict

class Translator:
    def __init__(self, data):
        self.data = data
        self.reverse = reverse_dict(data)

    def translate(self, word):
        word = word.lower().strip()
        if word in self.data:
            entry = self.data[word]
            return f"{word} → {entry['lagu']} ({entry['pos']})"
        elif word in self.reverse:
            entry = self.reverse[word]
            return f"{word} → {entry} ({self.data[entry]['pos']})"
        else:
            guess = apply_grammar_rules(word, self.data)
            return guess or "Word not found."

    def add_word(self, eng, lagu, pos, img="", audio=""):
        self.data[eng] = {"lagu": lagu, "pos": pos, "image": img, "audio": audio}
        self.reverse = reverse_dict(self.data)
        print(f"Added: {eng} ↔ {lagu} [{pos}]")

    def delete_word(self, word):
        if word in self.data:
            del self.data[word]
            print(f"Deleted English word: {word}")
        elif word in self.reverse:
            eng = self.reverse[word]
            del self.data[eng]
            print(f"Deleted Lagu word: {word}")
        else:
            print("Word not found.")
        self.reverse = reverse_dict(self.data)

    def search(self, word):
        matches = [k for k in self.data if word in k or word in self.data[k]['lagu']]
        return "\n".join(f"{k} ↔ {self.data[k]['lagu']}" for k in matches) or "No matches found."