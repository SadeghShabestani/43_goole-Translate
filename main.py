# This Python file uses the following encoding: utf-8
import sys
from PySide6.QtWidgets import QApplication, QMessageBox
from functools import partial
import random
from PySide6.QtUiTools import QUiLoader


class Main:
    def __init__(self):
        super(Main, self).__init__()
        loader = QUiLoader()
        self.ui = loader.load("form.ui")
        self.ui.show()
        try:
            self.file = open("text.txt", "r", encoding="utf8")
        except Exception as e:
            print(e)
            message = QMessageBox()
            message.setText("متصل نشد")
            message.exec_()
            exit()

        self.all_file = self.file.read()
        self.split = self.all_file.split("\n")
        self.words = []
        i = 0
        while i < len(self.split):
            my_dict = {"english": self.split[i], "persian": self.split[i + 1]}
            self.words.append(my_dict)
            i += 2
        self.ui.btn_translate.clicked.connect(self.checked)

    def checked(self):
        if self.ui.english_to_persian.isChecked():
            self.space = ""
            self.text = self.ui.tb_text1.text()
            user_world = self.text.split(" ")

            for i in range(len(user_world)):
                for j in range(len(self.words)):
                    if self.words[j]["english"] == user_world[i]:
                        self.space = self.space + self.words[j]["persian"] + " "
                        self.ui.tb_text_2.setText(self.space)
                        break
                else:
                    self.space = self.space + user_world[i] + " "
                    self.ui.tb_text_2.setText(self.space)

        if self.ui.persian_to_english.isChecked():
            self.space = ""
            self.text = self.ui.tb_text1.text()
            user_world = self.text.split(" ")
            for i in range(len(user_world)):
                for j in range(len(self.words)):
                    if self.words[j]["persian"] == user_world[i]:
                        self.space = self.space + self.words[j]["english"] + " "
                        self.ui.tb_text_2.setText(self.space)
                        break
                else:
                    self.space = self.space + user_world[i] + " "
                    self.ui.tb_text_2.setText(self.space)


if __name__ == "__main__":
    app = QApplication([])
    window = Main()
    sys.exit(app.exec_())
