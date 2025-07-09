import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from translator import Translator
from storage import load_dictionary, save_dictionary
from csv_io import export_to_csv, import_from_csv
from op_io import export_to_op, import_from_op
from utils import reverse_dict
import os
from PIL import Image, ImageTk
import pygame

class TranslatorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Lagu De Unn Translator")
        self.dark_mode = False
        self.data = load_dictionary()
        self.translator = Translator(self.data)
        self.init_ui()
        pygame.mixer.init()

    def init_ui(self):
        self.top_frame = ttk.Frame(self.root, padding=10)
        self.top_frame.pack(fill="x")

        self.lang_var = tk.StringVar(value="English → Lagu")
        self.lang_menu = ttk.OptionMenu(self.top_frame, self.lang_var, "English → Lagu", "English → Lagu", "Lagu → English")
        self.lang_menu.pack(side="left")

        self.entry_var = tk.StringVar()
        self.entry = ttk.Entry(self.top_frame, textvariable=self.entry_var, width=40)
        self.entry.pack(side="left", padx=5)
        self.entry.bind("<KeyRelease>", self.live_search)

        self.search_button = ttk.Button(self.top_frame, text="Translate", command=self.translate)
        self.search_button.pack(side="left", padx=5)

        self.toggle_dark = ttk.Button(self.top_frame, text="🌓", width=3, command=self.toggle_dark_mode)
        self.toggle_dark.pack(side="left")

        self.middle_frame = ttk.Frame(self.root, padding=10)
        self.middle_frame.pack(fill="both", expand=True)

        self.results = tk.Text(self.middle_frame, height=10, wrap="word")
        self.results.pack(fill="both", expand=True)

        self.media_frame = ttk.Frame(self.root, padding=10)
        self.media_frame.pack(fill="x")

        self.image_label = ttk.Label(self.media_frame, text="Image: ")
        self.image_label.pack(side="left")

        self.img_display = tk.Label(self.media_frame)
        self.img_display.pack(side="left", padx=10)

        self.audio_button = ttk.Button(self.media_frame, text="Play Audio", command=self.play_audio)
        self.audio_button.pack(side="left")

        self.bottom_frame = ttk.Frame(self.root, padding=10)
        self.bottom_frame.pack(fill="x")

        ttk.Button(self.bottom_frame, text="Add Word", command=self.add_word).pack(side="left")
        ttk.Button(self.bottom_frame, text="Export CSV", command=lambda: export_to_csv(self.translator.data)).pack(side="left")
        ttk.Button(self.bottom_frame, text="Import CSV", command=self.import_csv).pack(side="left")
        ttk.Button(self.bottom_frame, text="Export OP", command=self.export_op).pack(side="left")
        ttk.Button(self.bottom_frame, text="Import OP", command=self.import_op).pack(side="left")

    def toggle_dark_mode(self):
        self.dark_mode = not self.dark_mode
        style = ttk.Style()
        style.theme_use("clam" if self.dark_mode else "default")

    def live_search(self, event):
        text = self.entry_var.get()
        matches = self.translator.search(text)
        self.results.delete(1.0, tk.END)
        self.results.insert(tk.END, matches)

    def translate(self):
        word = self.entry_var.get().strip()
        direction = "en" if "English" in self.lang_var.get() else "lagu"
        result = self.translator.translate(word)
        self.results.delete(1.0, tk.END)
        self.results.insert(tk.END, result)

        # Load media if exists
        entry = self.translator.data.get(word) or self.translator.reverse.get(word)
        if isinstance(entry, str):
            entry = self.translator.data.get(entry)

        if entry:
            img_path = entry.get("image")
            audio_path = entry.get("audio")

            if img_path and os.path.exists(img_path):
                img = Image.open(img_path).resize((100, 100))
                self.tk_img = ImageTk.PhotoImage(img)
                self.img_display.config(image=self.tk_img)
            else:
                self.img_display.config(image="")

            self.audio_path = audio_path if audio_path and os.path.exists(audio_path) else ""

    def play_audio(self):
        if hasattr(self, 'audio_path') and self.audio_path:
            pygame.mixer.music.load(self.audio_path)
            pygame.mixer.music.play()
        else:
            messagebox.showinfo("Info", "No audio file to play.")

    def add_word(self):
        win = tk.Toplevel(self.root)
        win.title("Add Word")

        tk.Label(win, text="English:").grid(row=0, column=0)
        tk.Label(win, text="Lagu:").grid(row=1, column=0)
        tk.Label(win, text="POS:").grid(row=2, column=0)
        tk.Label(win, text="Image:").grid(row=3, column=0)
        tk.Label(win, text="Audio:").grid(row=4, column=0)

        eng = tk.Entry(win); lagu = tk.Entry(win); pos = tk.Entry(win)
        img = tk.Entry(win); audio = tk.Entry(win)

        eng.grid(row=0, column=1); lagu.grid(row=1, column=1)
        pos.grid(row=2, column=1); img.grid(row=3, column=1); audio.grid(row=4, column=1)

        def save():
            self.translator.add_word(eng.get(), lagu.get(), pos.get(), img.get(), audio.get())
            win.destroy()

        ttk.Button(win, text="Save", command=save).grid(row=5, column=0, columnspan=2)

    def import_csv(self):
        self.translator.data = import_from_csv()
        self.translator.reverse = reverse_dict(self.translator.data)

    def export_op(self):
        pwd = filedialog.asksaveasfilename(defaultextension=".op")
        if pwd:
            export_to_op(self.translator.data, filepath=pwd, password="secret")

    def import_op(self):
        path = filedialog.askopenfilename(filetypes=[("OP files", "*.op")])
        if path:
            self.translator.data = import_from_op(filepath=path, password="secret")
            self.translator.reverse = reverse_dict(self.translator.data)

if __name__ == "__main__":
    root = tk.Tk()
    app = TranslatorGUI(root)
    root.mainloop()