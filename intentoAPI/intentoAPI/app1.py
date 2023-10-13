from flask import Flask, jsonify
from PySide2.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget, QLineEdit, QPushButton

app = Flask(__name__)

fib_cache = {}

def fibonacci(n):
    fib = [0] * (n + 1)
    fib[0], fib[1] = 0, 1

    for i in range(2, n + 1):
        fib[i] = fib[i - 1] + fib[i - 2]

    return fib[n]

@app.route('/fibonacci/<int:n>', methods=['GET'])
def get_fibonacci_number(n):
    fib_number = fibonacci(n)
    return jsonify({'fibonacci_number': fib_number})

def calculate_fibonacci():
    n = int(entry.text())
    fib_number = fibonacci(n)
    result_label.setText(f"The Fibonacci number at position {n} is: {fib_number}")

if __name__ == '__main__':
    app.run()

    app = QApplication([])
    window = QWidget()
    window.setWindowTitle("Fibonacci Calculator")

    label = QLabel("Enter a position:")
    entry = QLineEdit()
    button = QPushButton("Calculate")
    result_label = QLabel("")

    layout = QVBoxLayout()
    layout.addWidget(label)
    layout.addWidget(entry)
    layout.addWidget(button)
    layout.addWidget(result_label)

    button.clicked.connect(calculate_fibonacci)

    window.setLayout(layout)
    window.show()

    app.exec_()