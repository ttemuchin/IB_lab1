import sys
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QHBoxLayout, QVBoxLayout, QPushButton, QMessageBox, QGridLayout, QLabel
from PyQt5.QtCore import Qt
from passwords import generate

class Password_gen(QWidget):
    def __init__(self):
        super(Password_gen, self).__init__()

        self.setWindowTitle("Генератор паролей")           

        self.vbox = QVBoxLayout(self)
        self.hbox_first = QHBoxLayout()
        self.hbox_input = QHBoxLayout()
        self.hbox_second = QHBoxLayout()
        self.hbox_third = QHBoxLayout()

        self.vbox.addLayout(self.hbox_first)
        self.vbox.addLayout(self.hbox_input)
        self.vbox.addLayout(self.hbox_second)
        self.vbox.addLayout(self.hbox_third)

        self.input = QLineEdit(self)
        self.hbox_input.addWidget(self.input)

        self.b_1 = QPushButton("Generate password", self)
        self.hbox_second.addWidget(self.b_1)
        self.b_1.clicked.connect(lambda: self._show_password(self.input.text()))

        
        self.intro_label = QLabel("Поможем сформировать надёжный пароль!\n\nВведите идентификатор:", alignment=Qt.AlignLeft)
        self.pass_label = QLabel("Ваш пароль:", alignment=Qt.AlignLeft)

        self.hbox_first.addWidget(self.intro_label)                         
        self.hbox_third.addWidget(self.pass_label)                         

    # def keyPressEvent(self, event):
    #     if event.key() == QtCore.Qt.Key_Enter:
    #         # self._show_password(self.input.text())
    #         self._counter += 1
    #         self.pass_label.setText('Клавиша Q нажата {} раз'.format(self._counter))
    #     event.accept()

    def _show_password(self, login):
        correct = True
        for i in login:
            if i == " ":
                correct = False

        if login != "":
            if correct:
                self.pass_label.setText("Ваш пароль: \n"+ generate(login))
            else:
                self.pass_label.setText("Ваш пароль:")
                QMessageBox.about(self, "Ошибка", "Идентификатор не должен содержать пробелов")
        else:
            QMessageBox.about(self, "Ошибка", "Поле идентификатора не должно быть пустым")


if __name__ == '__main__':

    app = QApplication(sys.argv)
    win = Password_gen()
    win.resize(450, 160)
    win.move(700, 300)
    win.show()

    sys.exit(app.exec_())
