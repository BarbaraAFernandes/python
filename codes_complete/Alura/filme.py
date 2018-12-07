class Programa :
    def __init__(self, nome, ano) :
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    @property
    def nome(self) :
        return self._nome

    @nome.setter
    def nome(self, nome) :
        self._nome = nome

    def dar_likes(self) :
        self._likes += 1

    @property
    def likes(self) :
        return self._likes

    def __str__(self) :
        return f'{self._nome} - {self.ano} - {self._likes} min'


class Filme(Programa) :
    def __init__(self, nome, ano, duracao) :
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self) :
        return f'{self.nome} - {self.ano} - {self.duracao} min - {self.likes} likes'


class Serie(Programa) :
    def __init__(self, nome, ano, temporadas) :
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self) :
        return f'{self.nome} - {self.ano} - {self.temporadas} temporadas - {self.likes} likes'


class Playlist() :
    def __init__(self, nome, programas) :
        self.nome = nome
        self._programas = programas

    def __getitem__(self, item) :
        return self._programas[item]

    def __len__(self) :
        return len(self._programas)


if __name__ == '__main__' :
    vingadores = Filme('vingadores - guerra infinita', 2018, 160)
    atlanta = Serie('atlanta', 2018, 2)
    tmep = Filme('todo mundo em panico', 1999, 110)
    demolidor = Serie('demolidor', 2016, 3)
    tmep.dar_likes()
    tmep.dar_likes()
    tmep.dar_likes()
    tmep.dar_likes()
    demolidor.dar_likes()
    demolidor.dar_likes()
    demolidor.dar_likes()
    demolidor.dar_likes()
    demolidor.dar_likes()
    demolidor.dar_likes()
    vingadores.dar_likes()
    vingadores.dar_likes()
    vingadores.dar_likes()

    atlanta.dar_likes()
    atlanta.dar_likes()

    listinha = [atlanta, vingadores, tmep, demolidor]
    minha_playlist = Playlist('fim de semana', listinha)
    for programa in minha_playlist :
        print(programa)
