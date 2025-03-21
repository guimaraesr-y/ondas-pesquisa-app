import sys
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QPushButton,
    QLabel,
    QLineEdit,
    QFormLayout,
    QHBoxLayout,
)
from PyQt6.QtCore import Qt, QPropertyAnimation, QEasingCurve
from PyQt6.QtGui import QPixmap
from qt_material import apply_stylesheet


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("OndasPesquisa")
        self.setMinimumSize(800, 600)

        # Create central widget and main layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.setSpacing(20)

        # Add logo
        logo_label = QLabel()
        logo_pixmap = QPixmap("logo.png")
        scaled_pixmap = logo_pixmap.scaled(
            300,
            300,
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation,
        )
        logo_label.setPixmap(scaled_pixmap)
        layout.addWidget(logo_label, alignment=Qt.AlignmentFlag.AlignCenter)

        # Create container for the form
        form_container = QWidget()
        form_container_layout = QHBoxLayout(form_container)

        # Form layout for input fields
        form_layout = QFormLayout()
        form_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        form_layout.setSpacing(15)
        form_layout.setContentsMargins(20, 20, 20, 20)

        # Input fields
        self.ref_input = QLineEdit()
        self.ref_input.setFixedWidth(300)
        self.ref_input.setPlaceholderText("Digite a referência...")
        self.ref_input.setStyleSheet(
            """
                QLineEdit {
                    padding: 8px;
                    border-radius: 5px;
                    font-size: 14px;
                    margin-left: 10px;
                    color: white;
                }
            """
        )

        self.cor_input = QLineEdit()
        self.cor_input.setFixedWidth(300)
        self.cor_input.setPlaceholderText("Digite a cor...")
        self.cor_input.setStyleSheet(
            """
                QLineEdit {
                    padding: 8px;
                    border-radius: 5px;
                    font-size: 14px;
                    margin-left: 10px;
                    color: white;
                }
            """
        )

        # Add fields to form layout
        form_layout.addRow(self.ref_input)
        form_layout.addRow(self.cor_input)

        # Center the form using container
        form_container_layout.addStretch()
        form_container_layout.addLayout(form_layout)
        form_container_layout.addStretch()

        # Add form container to main layout
        layout.addWidget(form_container)

        # Create search button with animation
        self.search_button = QPushButton("Pesquisar")
        self.search_button.setFixedSize(200, 50)
        self.search_button.setStyleSheet(
            """
            QPushButton {
                border-radius: 25px;
                font-size: 16px;
                font-weight: bold;
            }
        """
        )
        self.search_button.clicked.connect(self.animate_button)
        layout.addWidget(
            self.search_button,
            alignment=Qt.AlignmentFlag.AlignCenter
        )

    def animate_button(self):
        # Create bounce animation
        self.animation = QPropertyAnimation(self.search_button, b"geometry")
        self.animation.setDuration(200)
        self.animation.setEasingCurve(QEasingCurve.Type.OutBounce)

        current_geometry = self.search_button.geometry()

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
        self.animation = QPropertyAnimation(self.search_button, b"geometry")
        self.animation.setDuration(200)
        self.animation.setEasingCurve(QEasingCurve.Type.OutBounce)
        self.animation.setStartValue(self.search_button.geometry())
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
