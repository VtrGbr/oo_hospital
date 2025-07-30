Hospital Management Software
Sistema de gestão hospitalar desenvolvido em Python com Programação Orientada a Objetos (POO), permitindo o gerenciamento completo de pacientes, consultas, receitas, exames, leitos, estoque, equipe médica e emergências.

-- Projetando o software --
    Possíveis objetos a serem usados:
        - FuncionariosSaude -> Estarão contidos os(as) médicos(as) e enfermeiros(as)
        - Médico
        - Enfermeiro
        - Paciente
        - Prontuário médico
        - Setor administrativo --> Responsável por receber queixas contra os funcionáriosSaude, organizar o faturamento do hospital e do paciente

    Possíveis atributos de cada objeto:
        - FuncionariosSaude:
            1. Nome
            2. Profissão (médico ou enfermeiro)
            3. Registro profissional ( medico - CRM; Enfermeiros - COREN)
            /*A classe FucnioraiosSaude será uma classe pai para enfermeiros e médicos*/
        
        -Médico: Vai herdar "FuncionariosSaude"
            1.Especialidade
        
        -Enfermeiro:
            --Por enquanto enfermeiro não terá nenhum atributo particular dele. Pois ainda estou pensando no cenário do enfermeiro
        
        - Paciente:
            1. Nome
            2. Cartão do SUS
            3. CPF ( Caso o paciente não possua cartão do sus)
            4. Histórico médico

        -Prontuário médico:
            1.Profissional da sáude que realizou o prontuário
            2. Informações contidas no prontuário

            obs: analisando com mais atenção, creio que seja melhor que "prontuário médico" passe a ser um atributo ou classe do paciente

        -Setor administrativo:
            1.Queixas (bool)

    Possíveis métodos de cada objeto:
        -FuncionarioSaude:
            1. adicionar funcionario;
            2. Remover funcionario;
            3. Turno dos funcionario;
            4. Atualizar informações do funcionário
        -Médico:
            1. Requisitar exames;
            2. Receitar medicação;
        -Enfermeiro:
            -- Ainda não sei o que um enfermeiro pode fazer, irei pesquisar e implementar as funções específicas para o enfermeiro
        -Paciente:
            1. Adicionar paciente
            2. Remover paciente
            3. Agendar consulta
            4. Atualizar informações do paciente
        -Setor administrativo:
            1. Registrar queixa(se houver)
            2. Faturamento do hospital
            3. Faturamento do paciente
            


                   

Funcionalidades:
1 - Cadastro de pacientes

2 - Agendamento, cancelamento e remarcação de consultas

3 - Registro médico (prontuário do paciente)

4 - Prescrição de medicamentos

5 - Solicitação de exames laboratoriais

6 - Gerenciamento de leitos e internações

7 - Controle de estoque de materiais hospitalares

8 - Escalonamento de turnos da equipe

9 - Gerenciamento de casos de emergência (com prioridade)

10 - Faturamento automático por atendimentos

-- Esta funcionalidade está planejada para ser implementada futuramente
Relatórios em PDF: Gerar um pdf com as informações do paciente
