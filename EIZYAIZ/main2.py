import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QPushButton, QVBoxLayout, QWidget, QLabel, QFileDialog, QMessageBox
from PyQt5.QtGui import QIcon
from pymorphy2 import MorphAnalyzer
import docx
import nltk
import json
from IPython.display import display

from docx import displacy
import spacy
nltk.download('punkt')
nltk.download('dependency_treebank')

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Автоматический синтаксический анализатор')
        self.setGeometry(100, 100, 800, 600)

        self.textEdit = QTextEdit()
        self.btnOpen = QPushButton('Открыть файл')
        self.btnOpen.clicked.connect(self.openFile)

        self.btnSave = QPushButton('Сохранить результат')
        self.btnSave.clicked.connect(self.saveResult)

        self.btnLoad = QPushButton('Загрузить результат')
        self.btnLoad.clicked.connect(self.loadResult)

        self.btnAnalyze = QPushButton('Проанализировать')
        self.btnAnalyze.clicked.connect(self.analyzeText)

        self.btnEdit = QPushButton('Редактировать результат')
        self.btnEdit.clicked.connect(self.editResult)

        self.btnHelp = QPushButton('Помощь')
        self.btnHelp.clicked.connect(self.showHelp)

        self.resultLabel = QTextEdit()
        self.resultLabel.setReadOnly(True)
        
        
        self.btnShowTree = QPushButton('Показать дерево')
        self.btnShowTree.clicked.connect(self.showDependencyTree)

        layout = QVBoxLayout()
        layout.addWidget(self.textEdit)
        layout.addWidget(self.btnOpen)
        layout.addWidget(self.btnAnalyze)
        layout.addWidget(self.resultLabel)

        layout.addWidget(self.btnSave)
        layout.addWidget(self.btnLoad)
        layout.addWidget(self.btnEdit)
        layout.addWidget(self.btnHelp)
        layout.addWidget(self.btnShowTree)
       
        centralWidget = QWidget()
        centralWidget.setLayout(layout)
        self.setCentralWidget(centralWidget)

        self.morph = MorphAnalyzer()

    def openFile(self):
        try:
            fileName, _ = QFileDialog.getOpenFileName(self, "Открыть файл", "", "Документы (*.docx)")
            if fileName:
                doc = docx.Document(fileName)
                text = ""
                for paragraph in doc.paragraphs:
                    text += paragraph.text + "\n"
                self.textEdit.setText(text)
        except Exception as e:
            QMessageBox.critical(self, "Ошибка", str(e))

    def saveResult(self):
        try:
            # Получаем текст результата
            result_text = self.resultLabel.toPlainText()

            # Определяем имя файла для сохранения
            fileName, _ = QFileDialog.getSaveFileName(self, "Сохранить файл", "", "JSON файлы (*.json)")

            # Если пользователь выбрал файл
            if fileName:
                # Создаем словарь для сохранения
                data = {'result': result_text}

                # Записываем данные в файл
                with open(fileName, 'w', encoding='utf-8') as f:
                    json.dump(data, f, ensure_ascii=False)

        except Exception as e:
            QMessageBox.critical(self, "Ошибка", str(e))
    
    
    def showDependencyTree(self):
        try:
            # Загружаем модель для русского языка
            nlp = spacy.load("ru_core_news_sm")
            
            # Получаем текст из QTextEdit
            text = self.textEdit.toPlainText()
            
            # Обрабатываем текст с помощью модели
            doc = nlp(text)
            
            # Для каждого предложения в тексте строим дерево зависимостей
            for sent in doc.sents:
                svg = displacy.render(sent, style="dep", jupyter=False)
                filename = f"D:/rabstol/Сокровище 6 семестра/ЕЯзИИС/Lab3/dependency_tree_{sent.start}.svg"
                with open(filename, "w", encoding="utf-8") as file:
                    file.write(svg)
                print(f"Дерево зависимостей сохранено в файл: {filename}")
                
                # Также вы можете отобразить деревья зависимостей в интерфейсе, но это потребует дополнительной интеграции
        except Exception as e:
            QMessageBox.critical(self, "Ошибка", str(e))
    def loadResult(self):
        try:
            # Открываем диалоговое окно для выбора файла
            fileName, _ = QFileDialog.getOpenFileName(self, "Открыть файл", "", "JSON файлы (*.json)")

            # Если пользователь выбрал файл
            if fileName:
                # Читаем данные из файла
                with open(fileName, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    # Получаем результат из данных
                    result_text = data.get('result', '')
                    # Устанавливаем текст результата в текстовое поле
                    self.resultLabel.setText(result_text)
        except Exception as e:
            QMessageBox.critical(self, "Ошибка", str(e))

    def editResult(self):
        try:
            # Включаем редактирование текста в resultLabel
            self.resultLabel.setReadOnly(False)
        except Exception as e:
            QMessageBox.critical(self, "Ошибка", str(e))

    def analyzeText(self):
        try:
            text = self.textEdit.toPlainText()

            # Разбиваем текст на предложения с помощью nltk
            sentences = nltk.sent_tokenize(text)

            # Проводим анализ частей речи каждого слова
            result = ""
            for i, sentence in enumerate(sentences, 1):
                result += f"Анализ предложения {i}:\n"
                tokens = nltk.word_tokenize(sentence)
                for token in tokens:
                    # Получаем нормальную форму слова
                    normalized_token = self.morph.parse(token)[0].normal_form
                    # Получаем часть речи слова на русском языке
                    pos_tag = self.morph.parse(token)[0].tag.POS
                    # Преобразуем тег части речи в русское название
                    pos_tag_ru = self.translate_pos_tag(pos_tag)
                    result += f"Слово: {normalized_token}, Часть речи: {pos_tag_ru}\n"
                result += "\n"

            self.resultLabel.setText(result)
        except Exception as e:
            QMessageBox.critical(self, "Ошибка", str(e))

    def showHelp(self):
        help_text = """
        Автоматический синтаксический анализатор

        Данная программа предназначена для проведения автоматического синтаксического анализа текста на русском языке. 
        Она позволяет определить части речи для каждого слова в предложениях текста.

        Инструкция по использованию:

        1. Открыть файл: нажмите кнопку "Открыть файл" и выберите файл в формате .docx с текстом для анализа.
        2. Проанализировать: после открытия файла нажмите кнопку "Проанализировать", чтобы выполнить анализ текста.
        3. Редактирование результата: после анализа текста вы можете редактировать результат прямо в окне программы.
        4. Сохранение результата: для сохранения результата нажмите кнопку "Сохранить результат" и выберите местоположение и имя файла для сохранения в формате .json.
        5. Помощь: для получения дополнительной информации о программе и ее функциях нажмите кнопку "Помощь".

        Приятного использования!
        """
        QMessageBox.information(self, "Справка", help_text)

    def translate_pos_tag(self, pos_tag):
        # Словарь для соответствия тегов частей речи и их русских названий
        pos_tag_dict = {
            'NOUN': 'существительное',
            'ADJF': 'прилагательное',
            'ADJS': 'краткое прилагательное',
            'COMP': 'компаратив',
            'VERB': 'глагол',
            'INFN': 'инфинитив',
            'PRTF': 'причастие (полное)',
            'PRTS': 'причастие (краткое)',
            'GRND': 'деепричастие',
            'NUMR': 'числительное',
            'ADVB': 'наречие',
            'NPRO': 'местоимение-существительное',
            'PRED': 'предикатив',
            'PREP': 'предлог',
            'CONJ': 'союз',
            'PRCL': 'частица',
            'INTJ': 'междометие',
            'None': 'неизвестно'
        }
        return pos_tag_dict.get(pos_tag, pos_tag)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())
