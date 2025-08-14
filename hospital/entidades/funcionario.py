class FuncionarioSaude:
    def __init__(self, nome, registro):
        self.nome = nome
        self.registro = registro

    def __str__(self):
        return f"{self.nome} ({self.registro})"

class Medico(FuncionarioSaude):
    def __init__(self, nome, registro, especialidade):
        super().__init__(nome, registro)
        self.especialidade = especialidade

    def requisitar_exame(self, paciente, exame):
        paciente.solicitar_exame(exame)

    def receitar_medicamento(self, paciente, receita):
        paciente.adicionar_receita(receita)

class Enfermeiro(FuncionarioSaude):
    def __init__(self, nome, registro):
        super().__init__(nome, registro)
