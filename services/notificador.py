# Notificador: enviar notificações.

class Notificador:

    def notificar_emprestimo(self, email, data_devolucao):
        print(f"[EMAIL] Empréstimo registrado para {email}.")
        print(f"Devolução até: {data_devolucao}")

    def notificar_devolucao(self, email):
        print(f"[EMAIL] Devolução registrada para {email}.")

    def notificar_atraso(self, email):
        print(f"[EMAIL] Empréstimo em atraso para {email}.")