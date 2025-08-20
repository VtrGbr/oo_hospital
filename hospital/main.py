from hospital import Hospital

hospital = Hospital()
def menu():
    print("\n--- SISTEMA DE GESTÃO HOSPITALAR ---")
    print("1  - Cadastrar paciente")
    print("2  - Agendar consulta")
    print("3  - Registrar prontuário")
    print("4  - Gerar fatura")
    print("5  - Gerenciar estoque")
    print("6  - Registrar emergência")
    print("7  - Ver emergências")
    print("8  - Solicitar exame")
    print("9  - Alocar leito")
    print("10 - Escalonamento de funcionários")
    print("11 - Queixas")
    print("0  - Sair")

''' Funções para facilitar na main'''
def estoque_menu(hospital):
    print("\n--- ESTOQUE ---")
    print("1 - Adicionar item")
    print("2 - Ver estoque")
    print("0 - Voltar")
    op = input("Escolha: ")
    while op != '0':
        if op == '1':
            item = input("Item: ")
            qtd = int(input("Quantidade: "))
            hospital.estoque.adicionar_item(item, qtd)
        elif op == '2':
            hospital.estoque.mostrar_estoque()
        else:
            print("Opção inválida.")
        print()
        op = input("Escolha: ")

def emergencias_menu(hospital):
    print("\n--- EMERGÊNCIAS ---")
    print("1 - Registrar emergência")
    print("2 - Ver emergências")
    print("0 - Voltar")
    op = input("Escolha: ")
    while op != '0':
        if op == '1':
            nome = input("Nome do paciente: ")
            prioridade = input("Prioridade (alta/média/baixa): ").lower()
            hospital.emergencias.registrar_emergencia(nome, prioridade)
        elif op == '2':
            hospital.emergencias.ver_emergencias()
        else:
            print("Opção inválida.")
        print()
        op = input("Escolha: ")
        
def escalonamento_menu(hospital):
    print("\n--- ESCALONAMENTO ---")
    print("1 - Escalar funcionário")
    print("2 - Ver escalonamento")
    print("0 - Voltar")
    op = input("Escolha: ")
    while op != '0':
        if op == '1':
            nome = input("Nome do funcionário: ")
            turno = input("Turno (manhã/tarde/noite): ")
            hospital.escalonar_funcionario(nome, turno)
        elif op == '2':
            hospital.ver_escalonamento()
        else:
            print("Opção inválida.")
        op = input("Escolha: ")



#funcao para cadastro
def cadastroPaciente(nome):
    cpf = input("CPF (ou Enter se não tiver): ") or None
    sus = input("Cartão SUS (ou Enter se não tiver): ") or None
    hospital.cadastrar_paciente(nome, cpf, sus)
#Função mais robusta para cadastrar e ver os pacientes
def cadastro():
    print("\n--- Cadastro ---")
    print("1 - Cadastrar paciente")
    print("2 - Ver pacientes cadastrados")
    print("3 - Dados de um paciente")
    print("0 - Voltar")
    op = input("Escolha: ")
    while op != '0':
        if op == '1':
            nome = input("Digite o nome do paciente: ")
            cadastroPaciente(nome)
        elif op == '2':

            hospital.listarPacientes()
        elif op == '3':
            nome = input("Digite o nome do paciente: ")
            hospital.mostrarPaciente(nome)
        else:
            print("Opção inválida.")
        op = input("Escolha: ")

#Funcao para agendamento
def agendarConsulta():
    nome = input("Nome do paciente: ")
    paciente = hospital.encontrar_paciente(nome)
    if paciente:
        dia = input("Data da consulta (dd/mm): ")
        medico = input("Nome do médico: ")
        hospital.agendar_consulta(nome, dia, medico)
    else:
        print("Paciente não encotrado.")
        resposta = input("Deseja cadastra-lo? ")
        if resposta.lower() == "sim":
            cadastroPaciente(nome)
            dia = input("Data da consulta (dd/mm): ")
            medico = input("Nome do médico: ")
            hospital.agendar_consulta(nome, dia, medico)
        
#Função para prontuario
def prontuarioMedico():
    nome = input("Nome do paciente: ")
    paciente = hospital.encontrar_paciente(nome)
    if paciente:
        profissional = input("Nome do profissional de saúde: ")
        descricao = input("Descrição do prontuário: ")
        hospital.registrar_prontuario(nome, profissional, descricao)
    else:
        print("Paciente não encontrado")
        resposta = input("Deseja cadastrá-lo? ")
        if resposta.lower() == "sim":
            cadastroPaciente(nome)
            profissional = input("Nome do profissional de saúde: ")
            descricao = input("Descrição do prontuário: ")
            hospital.registrar_prontuario(nome, profissional, descricao)

#Solicitação de exame
def solicitarExame():
    nome = input("Nome do paciente: ")
    paciente = hospital.encontrar_paciente(nome)

    if paciente:
        exame = input("Exame a solicitar: ")
        hospital.solicitar_exame(nome, exame)
    else:
        print("Paciente não encontrado")
        resposta = input("Deseja cadastrá-lo? ")
        if resposta.lower() == "sim":
            cadastroPaciente(nome)
            exame = input("Exame a solicitar: ")
            hospital.solicitar_exame(nome, exame)

def queixa():
    print("\n--- Registro de queixas ---")
    print("1 - Registrar queixa")
    print("2 - Ver queixa")
    print("0 - Voltar")
    op = input("Escolha: ")
    while op != '0':
        if op == '1':
            print("Registre uma queixa: ")
            funcionario = input("Digite o nome do funcionário: ")
            descricao = input("Descreva o ocorrido")
            hospital.administrativo.registrar_queixa(funcionario,descricao)
        elif op == '2':
            hospital.administrativo.exibir_queixas()
        else: 
            print("Opcao inválida!")
        print()
        op = input("Escolha: ")

# --- Execução principal ---
if __name__ == "__main__":
    #hospital = Hospital()
    while True:
        menu()
        op = input("Escolha uma opção: ")

        if op == '0':
            print("Encerrando o sistema.")
            break

        elif op == '1':
            cadastro()

        elif op == '2':
            agendarConsulta()

        elif op == '3':
            prontuarioMedico()

        elif op == '4':
            nome = input("Nome do paciente: ")
            hospital.faturar_paciente(nome)

        elif op == '5':
            estoque_menu(hospital)

        elif op == '6' or op == '7':
            emergencias_menu(hospital)
        elif op == '8':
            solicitarExame()

        elif op == '9':
            nome = input("Nome do paciente: ")
            hospital.alocar_leito(nome)

        elif op == '10':
            escalonamento_menu(hospital)
        elif op == '11':
            queixa()
        else:
            print("Opção inválida.")
           
