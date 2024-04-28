import tkinter as tk
from tkinter import filedialog, scrolledtext
from tkinter import messagebox
from tkinter import ttk
import csv
import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
from nltk.chunk import ne_chunk
from nltk.corpus import wordnet

# Загрузка данных и моделей NLTK
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')
nltk.download('wordnet')

def semantic_analysis(text):
    # Токенизация текста
    words = word_tokenize(text)
    
    # Определение частей речи
    pos_tags = pos_tag(words)

    # Извлечение семантических отношений из WordNet
    semantic_relations = {}
    for word, pos in pos_tags:
        synsets = wordnet.synsets(word)
        if synsets:
            definitions = [syn.definition() for syn in synsets]
            semantic_relations[word] = definitions

    return semantic_relations, pos_tags

def analyze_text():
    # Открытие диалогового окна для выбора файла
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if not file_path:
        return

    try:
        with open(file_path, "r") as file:
            text = file.read()

        # Выполнение семантического анализа и анализа синтаксиса
        semantic_relations, pos_tags = semantic_analysis(text)

        # Очистка таблицы и вывод результатов
        clear_table()
        for i, (word, definitions) in enumerate(semantic_relations.items()):
            table.insert("", "end", values=(word, pos_tags[i][1], pos_tags[i][0], " ".join(definitions)))

    except Exception as e:
        messagebox.showerror("Ошибка", f"Произошла ошибка: {e}")

def clear_table():
    # Очистка таблицы
    for row in table.get_children():
        table.delete(row)

def save_table():
    # Выбор места сохранения файла
    file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
    if not file_path:
        return

    try:
        # Открытие файла для записи
        with open(file_path, "w", newline="") as file:
            writer = csv.writer(file)

            # Запись заголовков
            writer.writerow(columns)

            # Запись данных из таблицы
            for row in table.get_children():
                values = table.item(row, "values")
                writer.writerow(values)

        messagebox.showinfo("Сохранение", "Таблица успешно сохранена.")
    except Exception as e:
        messagebox.showerror("Ошибка", f"Произошла ошибка при сохранении таблицы: {e}")

# Создание главного окна
root = tk.Tk()
root.title("Семантический и синтаксический анализ текста")

# Создание таблицы для вывода результатов
columns = ("Слово", "Часть речи", "Синтаксис", "Семантика")
table = ttk.Treeview(root, columns=columns, show="headings")
for col in columns:
    table.heading(col, text=col)
table.column("Семантика", width=400)  # Установка ширины колонки "Семантика"
table.pack(padx=10, pady=10, fill="both", expand=True)

# Создание кнопки для анализа текста
analyze_button = tk.Button(root, text="Анализировать текст", command=analyze_text)
analyze_button.pack(side="left", padx=5, pady=5)

# Создание кнопки для сохранения таблицы
save_button = tk.Button(root, text="Сохранить таблицу", command=save_table)
save_button.pack(side="left", padx=5, pady=5)

# Запуск главного цикла приложения
root.mainloop()
