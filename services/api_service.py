from typing import List
import time
from models.sheet import Sheet


class APIService:
    def __init__(self):
        # Mock data for testing
        self._mock_data = [
            {
                "ref": "ABC123",
                "cor": "Azul",
                "quantidade": 50,
                "preco": 29.99,
                "disponivel": True,
                "localizacao": "Estoque A",
            },
            {
                "ref": "XYZ789",
                "cor": "Verde",
                "quantidade": 30,
                "preco": 39.99,
                "disponivel": True,
                "localizacao": "Estoque B",
            },
            {
                "ref": "DEF456",
                "cor": "Vermelho",
                "quantidade": 0,
                "preco": 19.99,
                "disponivel": False,
                "localizacao": "Estoque C",
            },
        ]

    async def search_sheets(self, ref: str, cor: str) -> List[Sheet]:
        """
        Mock API call to search for sheets
        In a real implementation, this would make an HTTP request
        """
        # Simulate API delay
        time.sleep(0.5)

        # Filter mock data based on search criteria
        results = []
        for item in self._mock_data:
            if (
                ref.lower() in item["ref"].lower()
                and cor.lower() in item["cor"].lower()
            ):
                results.append(Sheet.from_dict(item))

        return results * 100
