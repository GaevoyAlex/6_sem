import tkinter as tk
from tkinter import filedialog
import nltk
from nltk.corpus import wordnet


def get_wordnet_pos(word):
    # Определение части речи слова
    tag = nltk.pos_tag([word])[0][1][0].upper()
    tag_dict = {"J": wordnet.ADJ, "N": wordnet.NOUN, "V": wordnet.VERB, "R": wordnet.ADV}
    return tag_dict.get(tag, wordnet.NOUN)


def generate_word_forms(text):
    # Генерация форм слов
    lemmatizer = nltk.WordNetLemmatizer()
    tokens = nltk.word_tokenize(text)
    word_forms = []
    for token in tokens:
        lemma = lemmatizer.lemmatize(token, get_wordnet_pos(token))
        inflections = wordnet.synsets(token)
        inflection_forms = [inf.lemmas()[0].name() for inf in inflections]
        word_form = {'word': token, 'lemma': lemma, 'pos': nltk.pos_tag([token])[0][1], 'inflections': inflection_forms}
        word_forms.append(word_form)
    return word_forms


def process_text():
    # Обработка текста и вывод результатов
    file_path = filedialog.askopenfilename()
    if not file_path:
        return
    try:
        with open(file_path, "r") as file:
            text = file.read()
            word_forms = generate_word_forms(text)

            # Создание нового окна и текстового виджета
            result_window = tk.Toplevel(window)
            result_window.title("Result")
            
            result_text = tk.Text(result_window)
            result_text.pack()

            # Вывод результатов в текстовый виджет
            for word_form in word_forms:
                result_text.insert(tk.END, str(word_form) + "\n")

    except Exception as e:
        messagebox.showinfo("Error", str(e))


# Создание окна приложения
window = tk.Tk()
window.title("Text Processing")
window.geometry("400x200")

# Кнопка для выбора файла
button = tk.Button(window, text="Select File", command=process_text)
button.pack(pady=20)

# Запуск главного цикла приложения
window.mainloop()