import tkinter as tk
from tkinter import filedialog, messagebox
from pypdf import PdfWriter
import os
import subprocess
import platform

def select_files():
    files = filedialog.askopenfilenames(
        title="PDFs auswählen",
        filetypes=[("PDF Dateien", "*.pdf")]
    )
    if files:
        file_list.set(f"{len(files)} Dateien ausgewählt")
        selected_files.extend(files)

def merge_and_show():
    if not selected_files:
        messagebox.showwarning("Keine Dateien", "Bitte wählen Sie PDFs aus")
        return
            
    merger = PdfWriter()
    for pdf in selected_files:
        merger.append(pdf)
    
    output = filedialog.asksaveasfilename(
        defaultextension=".pdf",
        filetypes=[("PDF Datei", "*.pdf")]
    )
    
    if output:
        merger.write(output)
        merger.close()
        messagebox.showinfo("Fertig", "PDFs zusammengeführt")
        
        # Datei öffnen
        if platform.system() == 'Windows':
            os.startfile(output)
        elif platform.system() == 'Darwin':
            subprocess.run(['open', output])
        else:
            subprocess.run(['xdg-open', output])
        
        selected_files.clear()
        file_list.set("Keine Dateien ausgewählt")

# GUI
root = tk.Tk()
root.title("PDF Zusammenführen")
root.geometry("400x150")

selected_files = []
file_list = tk.StringVar(value="Keine Dateien ausgewählt")

tk.Label(root, textvariable=file_list).pack(pady=20)
tk.Button(root, text="Dateien auswählen", command=select_files, width=20).pack(pady=5)
tk.Button(root, text="OK - Zusammenführen", command=merge_and_show, width=20).pack(pady=5)

root.mainloop()