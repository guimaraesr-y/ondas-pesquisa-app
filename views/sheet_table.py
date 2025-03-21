from typing import List
from PyQt6.QtWidgets import (
    QTableWidget,
    QTableWidgetItem,
    QHeaderView,
)
from models.sheet import Sheet


class SheetTable(QTableWidget):
    def __init__(self):
        super().__init__()
        self.setup_table()

    def setup_table(self):
        # Set up columns
        columns = [
            "Referência",
            "Cor",
            "Quantidade",
            "Preço",
            "Disponível",
            "Localização",
        ]
        self.setColumnCount(len(columns))
        self.setHorizontalHeaderLabels(columns)

        # Style the table
        self.setStyleSheet(
            """
            QTableWidget {
                background-color: #2D2D2D;
                gridline-color: #444444;
                border: none;
            }
            QTableWidget::item {
                padding: 5px;
                border-bottom: 1px solid #444444;
            }
            QHeaderView::section {
                background-color: #2196F3;
                padding: 5px;
                border: 1px solid #1976D2;
                font-weight: bold;
            }
        """
        )

        # Set column behavior
        header = self.horizontalHeader()
        for i in range(len(columns)):
            header.setSectionResizeMode(i, QHeaderView.ResizeMode.Stretch)

    def update_data(self, sheets: List[Sheet]):
        self.setRowCount(0)  # Clear existing rows

        for sheet in sheets:
            row_position = self.rowCount()
            self.insertRow(row_position)
            quantity = str(sheet.quantidade)
            price = f"R$ {sheet.preco:.2f}"
            available = "Sim" if sheet.disponivel else "Não"

            # Add data to cells
            self.setItem(row_position, 0, QTableWidgetItem(sheet.ref))
            self.setItem(row_position, 1, QTableWidgetItem(sheet.cor))
            self.setItem(row_position, 2, QTableWidgetItem(quantity))
            self.setItem(row_position, 3, QTableWidgetItem(price))
            self.setItem(row_position, 4, QTableWidgetItem(available))
            self.setItem(row_position, 5, QTableWidgetItem(sheet.localizacao))
