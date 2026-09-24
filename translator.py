import tkinter as tk
from tkinter import ttk, messagebox
from deep_translator import MyMemoryTranslator


def translate_text():
    text = input_text.get("1.0", tk.END).strip()

    if text == "":
        messagebox.showwarning("Warning", "Please enter some text.")
        return

    source = source_language.get()
    target = target_language.get()

    try:
        translated = MyMemoryTranslator(
            source=source,
            target=target
        ).translate(text)

        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, translated)

    except Exception as e:
        messagebox.showerror("Error", str(e))


# Main window
window = tk.Tk()
window.title("AI Language Translation Tool")
window.geometry("700x500")

# Heading
title = tk.Label(
    window,
    text="AI Language Translation Tool",
    font=("Arial", 20, "bold")
)
title.pack(pady=15)

# Source language
tk.Label(window, text="Source Language").pack()

source_language = ttk.Combobox(
    window,
    values=["english", "hindi", "marathi", "french", "german", "spanish"],
    state="readonly"
)
source_language.set("english")
source_language.pack(pady=5)

# Input
tk.Label(window, text="Enter Text").pack()

input_text = tk.Text(window, height=7, width=70)
input_text.pack(pady=5)

# Target language
tk.Label(window, text="Target Language").pack()

target_language = ttk.Combobox(
    window,
    values=["english", "hindi", "marathi", "french", "german", "spanish"],
    state="readonly"
)
target_language.set("marathi")
target_language.pack(pady=5)

# Translate button
translate_button = tk.Button(
    window,
    text="Translate",
    command=translate_text,
    font=("Arial", 12, "bold")
)
translate_button.pack(pady=15)

# Output
tk.Label(window, text="Translated Text").pack()

output_text = tk.Text(window, height=7, width=70)
output_text.pack(pady=5)

window.mainloop()