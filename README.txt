# Lagu De Unn Translator

This package contains a CLI and GUI translator for the constructed language "Lagu De Unn".

## Files

- `translator.py` - Command-line interface translator.
- `gui.py` - Tkinter-based graphical user interface translator.
- `dictionary.json` - JSON dictionary file with English phrases and their Lagu De Unn translations.

## Requirements

- Python 3.x
- Tkinter (usually included with Python)
  
## Usage

### CLI

Run the translator in terminal:


Commands:
- `translate` - Translate a sentence from English to Lagu De Unn.
- `add` - Add a dictionary entry.
- `delete` - Delete a dictionary entry.
- `search` - Search dictionary entries.
- `quit` - Exit the program.

### GUI

Run the graphical app:


- Enter an English sentence and click **Translate**.
- Add or delete dictionary entries using the fields below.
- Toggle **Dark Mode** checkbox to switch themes.

## Notes

- The translator supports phrase matching and simple inflection rules.
- Unknown words are displayed in brackets `[word]` in the translation.
- You can edit the `dictionary.json` file to add more phrases manually.

---

Enjoy your Lagu De Unn learning journey!
