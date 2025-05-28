import os
from deep_translator import GoogleTranslator
import pyttsx3
import tkinter as tk
from tkinter import filedialog, messagebox


def vertaal_bestanden(source_folder, target_folder, source_lang='en', target_lang='nl', chunk_size=4500):
    os.makedirs(target_folder, exist_ok=True)

    for filename in os.listdir(source_folder):
        if filename.endswith('.txt'):
            filepath = os.path.join(source_folder, filename)
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()

            chunks = [content[i:i+chunk_size] for i in range(0, len(content), chunk_size)]
            vertaalde_chunks = []

            for chunk in chunks:
                try:
                    vertaalde_chunks.append(
                        GoogleTranslator(source=source_lang, target=target_lang).translate(chunk)
                    )
                except Exception as e:
                    print(f"Fout bij vertalen: {e}")
                    vertaalde_chunks.append("[Fout bij vertalen]")

            vertaald_pad = os.path.join(target_folder, filename)
            with open(vertaald_pad, 'w', encoding='utf-8') as f_out:
                f_out.write('\n'.join(vertaalde_chunks))

            print(f"Vertaald: {filename}")


def voorlees_bestand():
    bestandspad = filedialog.askopenfilename(
        title="Kies een vertaald tekstbestand",
        filetypes=[("Text Files", "*.txt")],
        initialdir="Vertaalde teksten"
    )
    if bestandspad:
        try:
            with open(bestandspad, 'r', encoding='utf-8') as f:
                tekst = f.read()
                engine = pyttsx3.init()
                engine.say(tekst)
                engine.runAndWait()
        except Exception as e:
            messagebox.showerror("Fout", f"Kon tekst niet voorlezen:\n{e}")


def start_gui():
    root = tk.Tk()
    root.title("Voorleesfunctie")
    root.geometry("350x150")
    tk.Label(root, text="Kies een vertaald tekstbestand om voor te lezen").pack(pady=10)
    tk.Button(root, text="Bestand kiezen", command=voorlees_bestand).pack(pady=20)
    root.mainloop()


if __name__ == "__main__":
    bron_map = "teksten"
    vertaalde_map = "Vertaalde teksten"

    print("Teksten worden vertaald...")
    vertaal_bestanden(bron_map, vertaalde_map)
    print("Vertaling voltooid.")

    print("Start GUI...")
    start_gui()
