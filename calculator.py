import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QGridLayout, QLineEdit, QPushButton
from PyQt5.QtCore import Qt


class Calculator(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Calculator')
        self.setFixedSize(400, 500)

        # Create the display widget
        self.display = QLineEdit()
        self.display.setReadOnly(True)
        self.display.setAlignment(Qt.AlignRight)
        self.display.setFixedHeight(50)
        self.display.setStyleSheet("font-size: 24px; padding: 10px; border: 2px solid #000; border-radius: 10px;")

        # Create the layout
        mainLayout = QVBoxLayout()
        mainLayout.setSpacing(10)
        mainLayout.addWidget(self.display)

        # Create the grid layout for buttons
        gridLayout = QGridLayout()
        gridLayout.setSpacing(10)

        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+',
            'C'
        ]

        positions = [(i, j) for i in range(4) for j in range(4)] + [(4, 0)]

        for position, button in zip(positions, buttons):
            if button == '':
                continue
            btn = QPushButton(button)
            btn.setFixedSize(80, 80)
            btn.setStyleSheet("""
                QPushButton {
                    font-size: 24px; 
                    background-color: #f0f0f0; 
                    border: 2px solid #000; 
                    border-radius: 10px;
                }
                QPushButton:pressed {
                    background-color: #d0d0d0;
                }
            """)
            gridLayout.addWidget(btn, *position)

            # Connect buttons to the handler
            btn.clicked.connect(self.onButtonClick)

        mainLayout.addLayout(gridLayout)
        self.setLayout(mainLayout)
        self.show()

    def onButtonClick(self):
        button = self.sender()
        text = button.text()

        if text == '=':
            try:
                result = eval(self.display.text())
                self.display.setText(str(result))
            except Exception as e:
                self.display.setText('Error')
        elif text == 'C':
            self.display.clear()
        else:
            self.display.setText(self.display.text() + text)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    calc = Calculator()
    sys.exit(app.exec_())
