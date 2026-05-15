from dataclasses import dataclass
from abc import ABC, abstractmethod

@dataclass
class Equipamento(ABC):

    id: int
    nome: str
    tipo: str
    disponivel: bool = True

    @abstractmethod
    def calcular_multa(self, dias_atraso):
        pass


@dataclass
class Notebook(Equipamento):

    def calcular_multa(self, dias_atraso):
        return max(0, dias_atraso * 10)


@dataclass
class Projetor(Equipamento):

    def calcular_multa(self, dias_atraso):
        return max(0, dias_atraso * 5)


@dataclass
class Camera(Equipamento):

    def calcular_multa(self, dias_atraso):
        return max(0, dias_atraso * 7)