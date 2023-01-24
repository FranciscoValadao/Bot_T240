class Usuario:
    def __init__(self,nome,treinos):
        self.nome = nome
        self.treinos = treinos

    def get_msg(self):
        mess = "{} = {}/240".format(self.nome, self.treinos)
        return mess

    def set_treino(self):
        self.treinos += 1

    def set_desfaz(self):
        self.treinos -=1

    def get_treino(self):
        return self.treinos

