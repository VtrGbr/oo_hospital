from datetime import datetime

class Prontuario:
    def __init__(self, profissional, descricao):
        self.profissional = profissional
        self.descricao = descricao
        self.data = datetime.now()

    def __str__(self):
        return f"{self.data.strftime('%d/%m/%Y %H:%M')} - {self.profissional}: {self.descricao}"

class Paciente:
    def __init__(self, nome, cpf=None, cartao_sus=None):
        self.nome = nome
        self.cpf = cpf
        self.cartao_sus = cartao_sus
        self.prontuarios = []
        self.receitas = []
        self.exames = []
        self.consultas = []

    def adicionar_prontuario(self, profissional, descricao):
        prontuario = Prontuario(profissional, descricao)
        self.prontuarios.append(prontuario)

    def adicionar_receita(self, receita):
        self.receitas.append(receita)

    def solicitar_exame(self, exame):
        self.exames.append(exame)

    def agendar_consulta(self, dia, profissional):
        self.consultas.append((dia, profissional))

    def __str__(self):
        return f"Paciente: {self.nome}"
