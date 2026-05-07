# RepositorioEmprestimo: armazenar e recuperar dados.

from models.equipamento import Equipamento
from models.emprestimo import Emprestimo

class RepositorioEmprestimo:

    def __init__(self):
        self.equipamentos = [
            Equipamento(1, "Notebook Dell", "notebook"),
            Equipamento(2, "Projetor Epson", "projetor"),
            Equipamento(3, "Camera Canon", "camera")
        ]

        self.emprestimos = []

    def buscar_equipamento(self, equip_id):
        for equipamento in self.equipamentos:
            if equipamento.id == equip_id:
                return equipamento
        return None

    def salvar_emprestimo(self, emprestimo):
        self.emprestimos.append(emprestimo)