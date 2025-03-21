import sys
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QPushButton,
    QLabel,
)
from PyQt6.QtCore import Qt, QPropertyAnimation, QEasingCurve
from qt_material import apply_stylesheet


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Modern Python App")
        self.setMinimumSize(800, 600)

        # Create central widget and main layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.setSpacing(20)

        # Welcome text with custom styling
        welcome_label = QLabel("Welcome to Modern App")
        welcome_label.setStyleSheet(
            """
            QLabel {
                font-size: 32px;
                font-weight: bold;
                color: #2196F3;
            }
        """
        )
        layout.addWidget(welcome_label, alignment=Qt.AlignmentFlag.AlignCenter)

        # Create animated button
        self.button = QPushButton("Click Me!")
        self.button.setFixedSize(200, 50)
        self.button.setStyleSheet(
            """
            QPushButton {
                border-radius: 25px;
                font-size: 16px;
                font-weight: bold;
            }
        """
        )
        self.button.clicked.connect(self.animate_button)
        layout.addWidget(self.button, alignment=Qt.AlignmentFlag.AlignCenter)

    def animate_button(self):
        # Create bounce animation
        self.animation = QPropertyAnimation(self.button, b"geometry")
        self.animation.setDuration(200)
        self.animation.setEasingCurve(QEasingCurve.Type.OutBounce)

        current_geometry = self.button.geometry()

        # Animate up
        self.animation.setStartValue(current_geometry)
        bounce_geometry = current_geometry.translated(0, -20)
        self.animation.setEndValue(bounce_geometry)

        # Connect animation finish to return to original position
        self.animation.finished.connect(
            lambda: self.return_animation(current_geometry)
        )
        self.animation.start()

    def return_animation(self, original_geometry):
        self.animation = QPropertyAnimation(self.button, b"geometry")
        self.animation.setDuration(200)
        self.animation.setEasingCurve(QEasingCurve.Type.OutBounce)
        self.animation.setStartValue(self.button.geometry())
        self.animation.setEndValue(original_geometry)
        self.animation.start()


def main():
    app = QApplication(sys.argv)

    # Apply material design theme
    apply_stylesheet(app, theme="dark_blue.xml")

    window = MainWindow()
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
