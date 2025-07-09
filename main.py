from translator import Translator
from storage import load_dictionary, save_dictionary
from csv_io import export_to_csv, import_from_csv
from op_io import export_to_op, import_from_op
from utils import reverse_dict
from sentence_translator import translate_sentence # Added import

def main():
    data = load_dictionary()
    translator = Translator(data)

    print("🌐 Lagu De Unn Translator (English ↔ Lagu De Unn)")
    print("Commands: 'exit', 'add', 'delete', 'search <word>', 'export csv', 'import csv', 'export op', 'import op'\n")

    while True:
        user_input = input("Enter word or command: ").strip()
        if user_input == "exit":
            save_dictionary(translator.data)
            break
        elif user_input == "add":
            eng = input("English word: ").strip().lower()
            lagu = input("Lagu De Unn word: ").strip().lower()
            pos = input("Part of speech (noun/verb/...): ").strip().lower()
            img = input("Image path (optional): ").strip()
            audio = input("Audio path (optional): ").strip()
            translator.add_word(eng, lagu, pos, img, audio)
        elif user_input == "delete":
            word = input("Word to delete (English or Lagu): ").strip().lower()
            translator.delete_word(word)
        elif user_input.startswith("search"):
            word = user_input.split(" ", 1)[-1]
            print(translator.search(word))
        elif user_input == "export csv":
            export_to_csv(translator.data)
        elif user_input == "import csv":
            translator.data = import_from_csv()
            translator.reverse = reverse_dict(translator.data)
        elif user_input == "export op":
            pwd = input("Enter password: ")
            export_to_op(translator.data, password=pwd)
        elif user_input == "import op":
            pwd = input("Enter password: ")
            translator.data = import_from_op(password=pwd)
            translator.reverse = reverse_dict(translator.data)
        else:
            # Changed to translate full sentences
            print(translate_sentence(user_input, translator.data))
        print()

if __name__ == "__main__":
    main()

