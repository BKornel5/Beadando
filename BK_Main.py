import tkinter as tk
import sqlite3
from BK_Morse import BK_Morse

translater = BK_Morse()

def text_to_morse():
    input_text = input_textbox.get("1.0", tk.END).strip()
    morse = translater.text_to_morse(input_text)
    output_textbox.delete("1.0", tk.END)
    output_textbox.insert(tk.END, morse)

def morse_to_text():
    input_text = input_textbox.get("1.0", tk.END).strip()
    text = translater.morse_to_text(input_text)
    output_textbox.delete("1.0", tk.END)
    output_textbox.insert(tk.END, text)

def database_init():
    conn = sqlite3.connect("forditasok.db")
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS forditasok
                 (bemenet TEXT, kimenet TEXT)''')
    conn.commit()
    conn.close()

def save_to_database():
    input = input_textbox.get("1.0", tk.END).strip()
    output = output_textbox.get("1.0", tk.END).strip()
    if input and output:
        conn = sqlite3.connect("forditasok.db")
        c = conn.cursor()
        c.execute("INSERT INTO forditasok (bemenet, kimenet) VALUES (?, ?)", (input, output))
        conn.commit()
        conn.close()

# GUI létrehozása
root = tk.Tk()
root.title("Morse kód fordító")

# Bemeneti mező
input_label = tk.Label(root, text="Bemenet:")
input_label.pack()
input_textbox = tk.Text(root, height=5, width=45)
input_textbox.pack()

# Fordító gombok
to_morse_button = tk.Button(root, text="Szöveg → Morse", command=text_to_morse)
to_morse_button.pack()

to_text_button = tk.Button(root, text="Morse → Szöveg", command=morse_to_text)
to_text_button.pack()

# Kimeneti mező
output_label = tk.Label(root, text="Kimenet:")
output_label.pack()
output_textbox = tk.Text(root, height=5, width=45)
output_textbox.pack()

# Adatbázis
database_button = tk.Button(root, text="Fordítás mentése adatbázisba", command=save_to_database)
database_button.pack()

# Adatbázis inicializálása
database_init()

# Alkalmazás indítása
root.mainloop()


