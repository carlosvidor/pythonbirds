class Pessoa:
    def __init__(self, *filhos, nome = None, idade=41):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'
if __name__ == '__main__':
    theo = Pessoa(nome='Théo')
    carlos = Pessoa(theo,nome='Carlos')

    print(Pessoa.cumprimentar(theo))
    print(id(theo))
    print(theo.cumprimentar())
    print(theo.nome)
    print(theo.idade)
    for filho in carlos.filhos:
        print(filho.nome)

