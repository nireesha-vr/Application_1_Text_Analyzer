import tkinter as tk
from tkinter import messagebox
import re
from collections import Counter


def analyze_text():
    text = text_input.get("1.0", tk.END).strip()

    if not text:
        messagebox.showwarning("Warning", "Please enter some text.")
        return

    # Character count
    characters = len(text)

    # Extract words
    words = re.findall(r"\b[a-zA-Z]+\b", text.lower())
    word_count = len(words)

    # Sentence count
    sentences = re.split(r"[.!?]+", text)
    sentences = [s.strip() for s in sentences if s.strip()]
    sentence_count = len(sentences)

    # Word frequency
    frequency = Counter(words)

    # Display results
    result_text.delete("1.0", tk.END)

    result_text.insert(tk.END, "TEXT ANALYSIS RESULT\n")
    result_text.insert(tk.END, "=" * 40 + "\n\n")

    result_text.insert(tk.END, f"Characters : {characters}\n")
    result_text.insert(tk.END, f"Words      : {word_count}\n")
    result_text.insert(tk.END, f"Sentences  : {sentence_count}\n\n")

    result_text.insert(tk.END, "WORD FREQUENCY\n")
    result_text.insert(tk.END, "-" * 30 + "\n")

    for word, count in frequency.most_common(10):
        result_text.insert(tk.END, f"{word:<15} : {count}\n")


def clear_text():
    text_input.delete("1.0", tk.END)
    result_text.delete("1.0", tk.END)


# Main window
window = tk.Tk()
window.title("Text Analyzer")
window.geometry("700x650")
window.resizable(False, False)


# Title
title = tk.Label(
    window,
    text="TEXT ANALYZER",
    font=("Arial", 24, "bold")
)
title.pack(pady=15)


subtitle = tk.Label(
    window,
    text="Analyze text using Python NLP techniques",
    font=("Arial", 12)
)
subtitle.pack()


# Input section
input_label = tk.Label(
    window,
    text="Enter Your Text:",
    font=("Arial", 14, "bold")
)
input_label.pack(anchor="w", padx=30, pady=(20, 5))


text_input = tk.Text(
    window,
    height=10,
    width=75,
    font=("Arial", 12)
)
text_input.pack(padx=30)


# Buttons
button_frame = tk.Frame(window)
button_frame.pack(pady=15)


analyze_button = tk.Button(
    button_frame,
    text="Analyze Text",
    font=("Arial", 12, "bold"),
    command=analyze_text,
    padx=20,
    pady=8
)
analyze_button.grid(row=0, column=0, padx=10)


clear_button = tk.Button(
    button_frame,
    text="Clear",
    font=("Arial", 12, "bold"),
    command=clear_text,
    padx=30,
    pady=8
)
clear_button.grid(row=0, column=1, padx=10)


# Result section
result_label = tk.Label(
    window,
    text="Analysis Result:",
    font=("Arial", 14, "bold")
)
result_label.pack(anchor="w", padx=30, pady=(10, 5))


result_text = tk.Text(
    window,
    height=12,
    width=75,
    font=("Courier New", 12)
)
result_text.pack(padx=30)


# Start application
window.mainloop()