from hospital import Hospital
from entidades.exame import EXAMES_DISPONIVEIS
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

''' --- Funções para facilitar na main --- '''

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
            '''cadastroPaciente("Vitor Gabriel")
            cadastroPaciente("Davi Celestino")
            cadastroPaciente("João Tenório")
            cadastroPaciente("Humberto")'''     
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
    #nome = "Vitor Gabriel"
    paciente = hospital.encontrar_paciente(nome)
    if paciente:
        dia = input("Data da consulta (dd/mm): ")
        # Peça o tipo de profissional
        tipo_profissional = input("Tipo de profissional (Medico, Dentista, etc.): ")
        hospital.agendar_consulta(nome, dia, tipo_profissional)
    else:
        print("Paciente não encontrado.")
        resposta = input("Deseja cadastra-lo? ")
        if resposta.lower() == "sim":
            cadastroPaciente(nome)
            dia = input("Data da consulta (dd/mm): ")
            tipo_profissional = input("Tipo de profissional (Medico, Dentista, etc.): ")
            hospital.agendar_consulta(nome, dia, tipo_profissional)
        
#Função para prontuario
def prontuarioMedico():
    nome = input("Digite o nome do paciente: ")
    #nome = "Davi Celestino"
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
    nome_paciente = input("Nome do paciente: ")
    #nome_paciente = "João Tenório"
    paciente = hospital.encontrar_paciente(nome_paciente)

    if not paciente:
        print("Paciente não encontrado.")
        # Lógica opcional para cadastrar o paciente
        resposta = input("Deseja cadastrá-lo? (sim/nao) ")
        if resposta.lower() == "sim":
            cadastroPaciente(nome_paciente)
            solicitarExame() # Tenta novamente
        return

    # 1. Escolher o profissional
    print("\n--- Profissionais Disponíveis ---")
    for func in hospital.funcionarios:
        print(f"- {func.nome} ({func.__class__.__name__})")
    
    nome_profissional = input("Nome do profissional que está solicitando: ")
    #nome_profissional = "Aurora"

    # 2. Encontrar o objeto do profissional
    profissional_encontrado = None
    for func in hospital.funcionarios:
        if func.nome.lower() == nome_profissional.lower():
            profissional_encontrado = func
            break
    
    if not profissional_encontrado:
        print(f"Profissional '{nome_profissional}' não encontrado.")
        return

    # 3. Mostrar apenas os exames permitidos para esse profissional
    print(f"\n--- Exames que {profissional_encontrado.nome} pode solicitar ---")
    
    # Importa o dicionário de exames
    #from entidades.exame import EXAMES_DISPONIVEIS 
    
    # Verifica se o profissional tem exames permitidos
    if not profissional_encontrado.exames_permitidos:
        print("Este profissional não solicita exames.")
        return

    # Itera sobre a lista de exames permitidos do profissional
    for codigo_exame in profissional_encontrado.exames_permitidos:
        # Pega o nome completo do exame do dicionário principal
        exame_obj = EXAMES_DISPONIVEIS.get(codigo_exame)
        if exame_obj:
            print(f"- {codigo_exame}: {exame_obj.nome}")

    # 4. Solicitar o exame
    codigo_selecionado = input("Digite o código do exame a solicitar: ").lower()
    #codigo_selecionado = "limpeza"
    
    # Chama a função do hospital, que aplicará o polimorfismo
    hospital.solicitar_exame(nome_paciente, nome_profissional, codigo_selecionado)

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

'''def relatorios_menu(hospital):
    print("\n--- GERAÇÃO DE RELATÓRIOS ---")
    print("1 - Relatório de Paciente")
    print("2 - Relatório da Equipe de Saúde") # Texto da opção alterado
    print("3 - Relatório Geral do Hospital")
    print("0 - Voltar")
    op = input("Escolha: ")
    while op != '0':
        if op == '1':
            nome = input("Nome do paciente: ")
            hospital.gerar_pdf_paciente(nome)
        # --- CHAMADA MODIFICADA ---
        elif op == '2':
            # Não precisa mais pedir o nome, chama a função da equipe diretamente
            hospital.gerar_pdf_equipe()
        elif op == '3':
            hospital.gerar_pdf_hospital()
        else:
            print("Opção inválida.")
        
        print()
        op = input("Escolha: ")'''