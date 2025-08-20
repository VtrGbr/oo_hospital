from entidades.paciente import Paciente
from entidades.estoque import Estoque
from entidades.administrativo import SetorAdministrativo
from entidades.emergencia import EmergenciaManager

PRECO = 10.5
class Hospital:
    def __init__(self):
        self.pacientes = []
        self.funcionarios = [] #chamar a classe funcionario
        self.leitos = []
        self.escalonamento = {}
        self.estoque = Estoque()
        self.administrativo = SetorAdministrativo()
        self.emergencias = EmergenciaManager()

    def cadastrar_paciente(self, nome, cpf=None, cartao_sus=None):
        paciente = Paciente(nome, cpf, cartao_sus)
        self.pacientes.append(paciente)
        print(f"Paciente {nome} cadastrado.")

    def encontrar_paciente(self, nome):
        for p in self.pacientes:
            if p.nome.lower() == nome.lower():
                return p
        return None
    
    def listarPacientes(self):
        if not self.pacientes:
            print("Nenhum paciente cadastrado.")
            return  # Retorna para sair da função se não houver pacientes

        print("\n--- Lista de Pacientes ---")
        for i, paciente in enumerate(self.pacientes, 1):
            nome = paciente.nome
            cpf = paciente.cpf if paciente.cpf else "Não informado"
            cartao_sus = paciente.cartao_sus if paciente.cartao_sus else "Não informado"
            print(f"{i}: Nome: {nome}, CPF: {cpf}, Cartão SUS: {cartao_sus}")
            
    def mostrarPaciente(self, nome):
        paciente = self.encontrar_paciente(nome)
        if paciente:
            print(f"\n--- Detalhes do Paciente: {paciente.nome} ---")
            print(f"CPF: {paciente.cpf if paciente.cpf else 'Não informado'}")
            print(f"Cartão SUS: {paciente.cartao_sus if paciente.cartao_sus else 'Não informado'}")
            
            print("\n--- Prontuários ---")
            if paciente.prontuarios:
                for prontuario in paciente.prontuarios:
                    print(prontuario)
            else:
                print("Nenhum prontuário registrado.")

            print("\n--- Receitas ---")
            if paciente.receitas:
                for i, receita in enumerate(paciente.receitas, 1):
                    print(f"{i}: {receita}")
            else:
                print("Nenhuma receita registrada.")

            print("\n--- Exames Solicitados ---")
            if paciente.exames:
                for i, exame in enumerate(paciente.exames, 1):
                    print(f"{i}: {exame}")
            else:
                print("Nenhum exame solicitado.")

            print("\n--- Consultas Agendadas ---")
            if paciente.consultas:
                for i, (dia, medico) in enumerate(paciente.consultas, 1):
                    print(f"{i}: Dia {dia} com Dr(a). {medico}")
            else:
                print("Nenhuma consulta agendada.")
        else:
            print("Paciente não encontrado.")

    def agendar_consulta(self, nome, dia, profissional):
        paciente = self.encontrar_paciente(nome)
        if paciente:
            paciente.agendar_consulta(dia, profissional)
            print("Consulta agendada.")
        else:
            print("Paciente não encontrado.")

    def registrar_prontuario(self, nome, profissional, descricao):
        paciente = self.encontrar_paciente(nome)
        if paciente:
            paciente.adicionar_prontuario(profissional, descricao)
            print("Prontuário registrado.")
        else:
            print("Paciente não encontrado.")

    def faturar_paciente(self, nome):
        paciente = self.encontrar_paciente(nome)
        if paciente:
            total = len(paciente.consultas) * PRECO + len(paciente.exames) * PRECO
            print(f"Fatura para {paciente.nome}: R$ {total:.2f}")
        else:
            print("Paciente não encontrado.")

    def solicitar_exame(self, nome, exame):
        paciente = self.encontrar_paciente(nome)
        if paciente:
            paciente.solicitar_exame(exame)
            print("Exame solicitado.")
        else:
            print("Paciente não encontrado.")

    def alocar_leito(self, nome):
        paciente = self.encontrar_paciente(nome)
        if paciente:
            leito = f"Leito-{len(self.leitos)+1}"
            self.leitos.append((leito, paciente.nome))
            print(f"{paciente.nome} alocado no {leito}.")
        else:
            print("Paciente não encontrado.")

    def escalonar_funcionario(self, nome, turno):
        self.escalonamento[nome] = turno
        print(f"{nome} escalado para o turno {turno}.")

    def ver_escalonamento(self):
        if not self.escalonamento:
            print("Nenhum funcionário escalado.")
        else:
            for nome, turno in self.escalonamento.items():
                print(f"{nome}: {turno}")
