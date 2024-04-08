import nltk
from nltk import pos_tag, RegexpParser
from nltk.tokenize import word_tokenize
import tkinter as tk
from tkinter import filedialog, scrolledtext
from nltk.draw import TreeWidget
from nltk import Tree
from nltk.draw.util import CanvasFrame

nltk.download('averaged_perceptron_tagger')
nltk.download('punkt')

def analyze_text(text):
    tokens = word_tokenize(text)
    tagged = pos_tag(tokens)
    grammar = r"""
    NP: {<DT|JJ|NN.*>+}          # Существительное с определителями и прилагательными
    P: {<IN>}                   # Предлог
    V: {<V.*>}                  # Глаголы
    PP: {<P> <NP>}              # Предложная группа
    VP: {<V> <NP|PP>*}          # Глагольная группа
    """
    parser = RegexpParser(grammar)
    result = parser.parse(tagged)
    return result


def draw_tree(tree, output_area):
    cf = CanvasFrame(width=800, height=600)  
    tc = TreeWidget(cf.canvas(), tree)
    cf.add_widget(tc, 10, 10)
    cf.print_to_file('tree.ps')
    cf.destroy()
    
    output_area.delete("1.0", tk.END)
    output_area.insert(tk.END, str(tree))
    
    # Нормализация и отображение дерева
    if isinstance(tree, Tree):
        tree.pretty_print(output=output_area, sentence_spacing=4, node_spacing=400, direction='horizontal', compact=False, empty_top=True)
        output_area.configure(font=("Courier", 14)) 


def create_gui():
    window = tk.Tk()
    window.title("Синтаксический анализатор")

    text_area = scrolledtext.ScrolledText(window, width=110, height=20, wrap=tk.WORD)
    text_area.pack(padx=10, pady=10)

    def open_file():
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        if file_path:
            with open(file_path, "r", encoding="utf-8") as file:
                text = file.read()
                text_area.delete("1.0", tk.END)
                text_area.insert(tk.END, text)

    btn_open_file = tk.Button(window, text="Открыть файл", command=open_file)
    btn_open_file.pack(pady=5)

    def analyze_and_draw():
        text = text_area.get("1.0", tk.END)
        result = analyze_text(text)
        draw_tree(result, output_area)

    btn_analyze = tk.Button(window, text="Анализировать текст", command=analyze_and_draw)
    btn_analyze.pack(pady=5)

    output_area = scrolledtext.ScrolledText(window, width=110, height=20, wrap=tk.WORD)
    output_area.pack(padx=10, pady=10)

    window.mainloop()

create_gui()
