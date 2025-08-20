class Exame():
    def __init__(self,nome):
        self.nome = nome

# Exames que podem ser solicitados
EXAMES_DISPONIVEIS = {
    # Médico
    "hemograma": Exame("Hemograma Completo"),
    "raio-x": Exame("Raio-X de Tórax"),
    "urina": Exame("Exame de Urina"),
    # Dentista
    "radiografia_dentaria": Exame("Radiografia Dentária"),
    "limpeza": Exame("Limpeza e Profilaxia"),
    # Enfermeiro
    "glicemia": Exame("Teste de Glicemia Capilar"),
    "pressao": Exame("Aferição de Pressão Arterial"),
    # Psicólogo (não solicita exames, mas encaminha)
    "encaminhamento_psiquiatra": Exame("Encaminhamento para Psiquiatra")
}