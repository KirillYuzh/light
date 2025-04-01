import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLabel

class ClickCounterApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.click_count = 0
        self.setWindowTitle("Click Counter")
        self.setGeometry(100, 100, 300, 200)
        
        # Central widget and layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout()
        
        # Click counter label
        self.label = QLabel(f"Clicks: {self.click_count}")
        self.label.setStyleSheet("font-size: 20px;")
        layout.addWidget(self.label)
        
        # Click button
        self.button = QPushButton("Click Me!")
        self.button.setStyleSheet("font-size: 16px; padding: 10px;")
        self.button.clicked.connect(self.increment_count)
        layout.addWidget(self.button)
        
        central_widget.setLayout(layout)
    
    def increment_count(self):
        self.click_count += 1
        self.label.setText(f"Clicks: {self.click_count}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ClickCounterApp()
    window.show()
    sys.exit(app.exec())