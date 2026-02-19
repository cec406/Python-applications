# note_taker_gui.py
# Grizzly Note Taker - Direct Edit GUI
# Built by Grizzly System Engineering – East Helena, Montana
# https://grizzlyse.com | (406) 439-8127 | info@grizzlyse.com

import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox, simpledialog
import os
from datetime import datetime

class GrizzlyNoteTakerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Grizzly Note Taker")
        self.root.geometry("900x700")
        self.root.minsize(650, 500)
        self.root.configure(bg="#f0f4f8")

        self.script_dir = os.path.dirname(os.path.abspath(__file__))
        self.journal_file = None
        self.current_journal_name = ""

        self.status_var = tk.StringVar(value="Waiting for journal title...")
        ttk.Label(root, textvariable=self.status_var, foreground="#34495e", font=("Helvetica", 11, "bold")).pack(pady=5)

        self.show_title_prompt()

    def show_title_prompt(self):
        frame = ttk.Frame(self.root, padding=40)
        frame.pack(fill="both", expand=True)

        ttk.Label(frame, text="Enter journal title to start:", font=("Helvetica", 14)).pack(pady=15)

        entry = ttk.Entry(frame, width=50, font=("Helvetica", 14))
        entry.pack(pady=10)
        entry.focus()

        def submit():
            title = entry.get().strip()
            if not title:
                messagebox.showwarning("Required", "Please enter a title.")
                return

            clean = title.replace(" ", "_")
            self.current_journal_name = f"{clean}.txt"
            self.journal_file = os.path.join(self.script_dir, self.current_journal_name)

            self.initialize_journal()
            frame.destroy()
            self.build_main_ui()
            self.status_var.set(f"Editing: {self.current_journal_name}")

        ttk.Button(frame, text="Start Journal", command=submit).pack(pady=10)
        entry.bind("<Return>", lambda e: submit())

    def initialize_journal(self):
        if not os.path.exists(self.journal_file):
            date = datetime.now().strftime("%Y-%m-%d")
            with open(self.journal_file, "w", encoding="utf-8") as f:
                f.write(f"Date: {date}\n\n")
            self.status_var.set(f"New journal created: {self.current_journal_name}")

    def build_main_ui(self):
        main_frame = ttk.Frame(self.root, padding=15)
        main_frame.pack(fill="both", expand=True)

        ttk.Label(main_frame, text="Grizzly Note Taker", font=("Helvetica", 18, "bold"),
                  background="#2c3e50", foreground="white").pack(fill="x", pady=10)

        # Main editable text area - type notes here directly
        self.text_area = scrolledtext.ScrolledText(main_frame, wrap=tk.WORD, font=("Consolas", 12),
                                                   bg="white", fg="black", insertbackground="blue")
        self.text_area.pack(fill="both", expand=True, pady=(0, 10))

        # Bottom button bar - always visible
        button_bar = ttk.Frame(self.root, padding=10)
        button_bar.pack(fill="x", side="bottom")

        ttk.Button(button_bar, text="Save Changes", command=self.save_changes).pack(side="left", padx=8)
        ttk.Button(button_bar, text="Refresh / Show Saved", command=self.show_journal).pack(side="left", padx=8)
        ttk.Button(button_bar, text="Add Summary", command=self.add_summary).pack(side="left", padx=8)
        ttk.Button(button_bar, text="New Journal", command=self.new_journal).pack(side="left", padx=8)
        ttk.Button(button_bar, text="Exit", command=self.root.quit).pack(side="right", padx=8)

        tk.Label(self.root, text="Grizzly System Engineering • East Helena, MT • grizzlyse.com",
                 bg="#f0f4f8", fg="#555555", font=("Helvetica", 9)).pack(side="bottom", pady=5)

        # Load existing content into editor
        self.show_journal()

    def save_changes(self):
        content = self.text_area.get("1.0", tk.END).rstrip()
        if content:
            with open(self.journal_file, "w", encoding="utf-8") as f:
                f.write(content)
            messagebox.showinfo("Saved", "Changes saved to journal!")
            self.status_var.set(f"Saved: {self.current_journal_name} at {datetime.now().strftime('%H:%M:%S')}")
        else:
            messagebox.showinfo("Empty", "Nothing to save.")

    def show_journal(self):
        if not os.path.exists(self.journal_file):
            self.text_area.delete("1.0", tk.END)
            self.text_area.insert(tk.END, "Journal is empty.\nStart typing above and click Save Changes.")
            return

        with open(self.journal_file, "r", encoding="utf-8") as f:
            content = f.read()

        self.text_area.delete("1.0", tk.END)
        self.text_area.insert(tk.END, content)
        self.text_area.see("end")

    def add_summary(self):
        summary = simpledialog.askstring("Add Summary", "Paste/type your summary here:")
        if summary and summary.strip():
            with open(self.journal_file, "a", encoding="utf-8") as f:
                f.write(f"\nSummary:\n{summary}\n\n")
            messagebox.showinfo("Added", "Summary appended.")
            self.show_journal()

    def new_journal(self):
        self.root.quit()
        self.root.destroy()
        new_root = tk.Tk()
        GrizzlyNoteTakerGUI(new_root)
        new_root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    app = GrizzlyNoteTakerGUI(root)
    root.mainloop()