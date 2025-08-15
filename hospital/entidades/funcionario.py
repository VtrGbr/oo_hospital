from abc import ABC, abstractmethod
from paciente import Paciente
paciente = Paciente()

class FuncionarioSaude(ABC):
    def __init__(self, nome, registro):
        self.nome = nome
        self.registro = registro

    @abstractmethod
    def requisitarExame(self,paciente,exame):
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
    def __init__(self, nome, registro, especialidade):
        super().__init__(nome, registro)
        self.especialidade = especialidade
    #O nome seria o do paciente
    def atenderPaciente(self, nome):
        print(f"Diagnosticando o paciente: {nome}")

    def requisitar_exame(self, paciente, exame):
        paciente.solicitar_exame(exame)

    def receitar_medicamento(self, paciente, receita):
        paciente.adicionar_receita(receita)

    def requisitarExame(self, exame):
        paciente.solicitar_exame(exame)

class Enfermeiro(FuncionarioSaude):
    def __init__(self, nome, registro):
        super().__init__(nome, registro)

    def requisitar_exame(self, exame):
        paciente.solicitar_exame(exame)
    
    def atenderPaciente(self, nome):
        print(f"Checando os sinais vitais do paciente {nome}")
    def registrarProntuario(self, profissional, descricao):
        paciente.adicionar_prontuario(profissional,descricao)
        
class Dentista(FuncionarioSaude):
    pass

class Psicologo(FuncionarioSaude):
    pass


