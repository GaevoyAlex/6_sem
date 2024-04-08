
import nltk
from nltk import pos_tag
from nltk.tokenize import sent_tokenize, word_tokenize
from tkinter import *
from tkinter import filedialog
import pickle

def load_text():
    file_path = filedialog.askopenfilename(filetypes=[('Text Files', '*.txt')])
    with open(file_path, 'r') as file:
        text = file.read()
    return text

# Синтаксический анализ текста
def parse_text(text):
    sentences = sent_tokenize(text)
    parsed_sentences = []
    for sentence in sentences:
        words = word_tokenize(sentence)
        words = [word for word in words if word.isalnum()]
        tagged_words = pos_tag(words)
        parsed_sentences.append(tagged_words)
    return parsed_sentences

def on_select_file():
    global result_text
    text = load_text()
    parsed_text = parse_text(text)
    result_text.delete(1.0, END)  # Очистить предыдущий результат
    for sentence in parsed_text:
        result_text.insert(END, str(sentence) + '\n\n')


def save_result():
    global result_data
    if result_data:
        file_path = filedialog.asksaveasfilename(defaultextension=".pkl", filetypes=[('Pickled Files', '*.pkl')])
        with open(file_path, 'wb') as file:
            pickle.dump(result_data, file)

def on_select_file():
    global result_text
    text = load_text()
    parsed_text = parse_text(text)
    result_text.delete(1.0, END)  # Очистить предыдущий результат
    for sentence in parsed_text:
        result_text.insert(END, str(sentence) + '\n\n')

def edit_sentence():
    global result_text
    selection = result_text.tag_ranges("sel")
    if selection:
        sentence = result_text.get(selection[0], selection[1])
        edited_sentence = input("Введите исправленное предложение: ")
        result_text.delete(selection[0], selection[1])
        result_text.insert(selection[0], edited_sentence)


# Главное окно приложения
def main():
    global result_text
    root = Tk()
    root.title("Синтаксический анализ текста")

    select_button = Button(root, text="Выбрать файл", command=on_select_file)
    select_button.pack()

    result_text = Text(root)
    result_text.pack()

    save_button = Button(root, text="Сохранить результат", command=save_result)
    save_button.pack()

    edit_button = Button(root, text="Редактировать предложение", command=edit_sentence)
    edit_button.pack()


    root.mainloop()

if __name__ == "__main__":
    main()
