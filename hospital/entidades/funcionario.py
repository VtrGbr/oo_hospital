from abc import ABC, abstractmethod
from paciente import Paciente
paciente = Paciente()

funcionarios = {
    "Medico":"Ricardo",
    "Enfermeiro" : "Lucas",
    "Dentista": "Aurora",
    "Psicologa":"Talhya",
}

class FuncionarioSaude(ABC):
    def __init__(self, nome, registro):
        self.nome = nome
        self.registro = registro

    @abstractmethod
    def requisitarExame(self,exame):
        pass
    
    @abstractmethod
    def atenderPaciente(self,nome):
        pass

   
    def registrarProntuario(self,profissional,descricao):

        paciente.adicionar_prontuario(profissional,descricao)
        print("Prontuario registrado")

    def __str__(self):
        return f"{self.nome} ({self.registro})"

class Medico(FuncionarioSaude):
    def __init__(self, nome, registro, especialidade = None):
        super().__init__(nome, registro)
        self.especialidade = especialidade
    #O nome seria o do paciente
    def atenderPaciente(self, nome):
        print(f"O médico {funcionarios['Medico']} está diagnosticando o paciente: {nome}")

    def requisitarExame(self, paciente, exame):
        paciente.solicitar_exame(exame)

    def receitar_medicamento(self, paciente, receita):
        paciente.adicionar_receita(receita)

    def requisitarExame(self, exame):
        paciente.solicitar_exame(exame)

class Enfermeiro(FuncionarioSaude):
    def __init__(self, nome, registro):
        super().__init__(nome, registro)

    def requisitarExame(self, exame):
        paciente.solicitar_exame(exame)
    
    def atenderPaciente(self, nome):
        print(f"O enfermeiro {funcionarios['Enfermeiro']} está checando os sinais vitais do paciente {nome}")

    def registrarProntuario(self, profissional, descricao):
        paciente.adicionar_prontuario(profissional,descricao)
        
class Dentista(FuncionarioSaude):

    def __init__(self, nome, registro):
        super().__init__(nome, registro)

    def requisitarExame(self, exame):
        paciente.solicitar_exame(exame)

    def atenderPaciente(self, nome):
        print(f"A dentista {funcionarios['Dentista']} está fazendo uma análise bucal no paciente: {nome}")

    def registrarProntuario(self, profissional, descricao):
        return super().registrarProntuario(profissional, descricao)

class Psicologo(FuncionarioSaude):
    def __init__(self, nome, registro):
        super().__init__(nome, registro)
    
    def requisitarExame(self, exame):
        print(f"Solicito encaminhamento para o médico psiquiatra para o exame {exame}")
    
    def registrarProntuario(self, profissional, descricao):
        return super().registrarProntuario(profissional, descricao)
    
    def atenderPaciente(self, nome):
        print(f"A psicóloga {funcionarios['Psicologa']} está realizando uma sessão de terapia com o paciente {nome}")
    
  


