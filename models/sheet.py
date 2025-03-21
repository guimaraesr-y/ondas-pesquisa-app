from dataclasses import dataclass


@dataclass
class Sheet:
    ref: str
    cor: str
    quantidade: int
    preco: float
    disponivel: bool
    localizacao: str

    @classmethod
    def from_dict(cls, data: dict) -> 'Sheet':
        return cls(
            ref=data.get('ref', ''),
            cor=data.get('cor', ''),
            quantidade=data.get('quantidade', 0),
            preco=data.get('preco', 0.0),
            disponivel=data.get('disponivel', False),
            localizacao=data.get('localizacao', '')
        )
