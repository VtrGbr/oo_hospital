from hospital import Hospital

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
    print("0  - Sair")


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

# --- Execução principal ---
if __name__ == "__main__":
    hospital = Hospital()

    while True:
        menu()
        op = input("Escolha uma opção: ")

        if op == '0':
            print("Encerrando o sistema.")
            break

        elif op == '1':
            nome = input("Nome: ")
            cpf = input("CPF (ou Enter se não tiver): ") or None
            sus = input("Cartão SUS (ou Enter se não tiver): ") or None
            hospital.cadastrar_paciente(nome, cpf, sus)

        elif op == '2':
            nome = input("Nome do paciente: ")
            dia = input("Data da consulta (dd/mm): ")
            medico = input("Nome do médico: ")
            hospital.agendar_consulta(nome, dia, medico)

        elif op == '3':
            nome = input("Nome do paciente: ")
            profissional = input("Nome do profissional de saúde: ")
            descricao = input("Descrição do prontuário: ")
            hospital.registrar_prontuario(nome, profissional, descricao)

        elif op == '4':
            nome = input("Nome do paciente: ")
            hospital.faturar_paciente(nome)

        elif op == '5':
            estoque_menu(hospital)

        elif op == '6' or op == '7':
            emergencias_menu(hospital)
        elif op == '8':
            nome = input("Nome do paciente: ")
            exame = input("Exame a solicitar: ")
            hospital.solicitar_exame(nome, exame)

        elif op == '9':
            nome = input("Nome do paciente: ")
            hospital.alocar_leito(nome)

        elif op == '10':
            escalonamento_menu(hospital)


        else:
            print("Opção inválida.")
