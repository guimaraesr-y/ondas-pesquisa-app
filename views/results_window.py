from PyQt6.QtWidgets import (
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QScrollArea,
    QLabel,
)
from PyQt6.QtCore import Qt
from typing import List
from models.sheet import Sheet
from views.sheet_table import SheetTable


class ResultsWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setup_ui()

    def setup_ui(self):
        self.setWindowTitle("Resultados da Pesquisa")
        self.setMinimumSize(1200, 600)

        # Create central widget and main layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)
        layout.setContentsMargins(10, 10, 10, 10)

        # Add title label
        title_label = QLabel("Resultados da Pesquisa")
        title_label.setStyleSheet("""
            QLabel {
                font-size: 24px;
                font-weight: bold;
                color: #2196F3;
                padding: 10px;
            }
        """)
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(title_label)

        # Create scroll area
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setHorizontalScrollBarPolicy(
            Qt.ScrollBarPolicy.ScrollBarAsNeeded
        )
        scroll_area.setVerticalScrollBarPolicy(
            Qt.ScrollBarPolicy.ScrollBarAsNeeded
        )

        # Create container for the table
        table_container = QWidget()
        table_layout = QVBoxLayout(table_container)

        # Create and add table
        self.table = SheetTable()
        table_layout.addWidget(self.table)

        # Set the container as the scroll area widget
        scroll_area.setWidget(table_container)

        # Add scroll area to main layout
        layout.addWidget(scroll_area)

    def update_results(self, sheets: List[Sheet]):
        """Update the table with new search results"""
        self.table.update_data(sheets)
        self.show()
        self.raise_()
