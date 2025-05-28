class Palestrante:
    def __init__(self, id, nome, foto, curriculo):
        self.id = id
        self.nome = nome
        self.foto = foto
        self.curriculo = curriculo
        self.eventos = []

    def adicionar_evento(self, evento):
        self.eventos.append(evento)

class Evento:
    def __init__(self, id, nome, data, horario, banner, local, descricao, categoria):
        self.id = id
        self.nome = nome
        self.data = data
        self.horario = horario
        self.banner = banner
        self.local = local
        self.descricao = descricao
        self.categoria = categoria
        self.palestrantes = []

    def adicionar_palestrante(self, palestrante):
        self.palestrantes.append(palestrante)

class Categoria:
    def __init__(self, nome):
        self.nome = nome
        self.eventos = []

    def adicionar_evento(self, evento):
        self.eventos.append(evento)
