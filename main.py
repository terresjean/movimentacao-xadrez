class Peca:
    def __init__(self, nome, cor):
        self.nome = nome
        self.cor = cor

    def movimentos_possiveis(self, posicao):
        return []

class Torre(Peca):
    def movimentos_possiveis(self, posicao):
        linha, coluna = posicao
        movimentos = []
        for i in range(8):
            if i != linha:
                movimentos.append((i, coluna))
            if i != coluna:
                movimentos.append((linha, i))
        return movimentos

class Bispo(Peca):
    def movimentos_possiveis(self, posicao):
        linha, coluna = posicao
        movimentos = []
        for i in range(1, 8):
            if linha + i < 8 and coluna + i < 8:
                movimentos.append((linha + i, coluna + i))
            if linha - i >= 0 and coluna - i >= 0:
                movimentos.append((linha - i, coluna - i))
            if linha + i < 8 and coluna - i >= 0:
                movimentos.append((linha + i, coluna - i))
            if linha - i >= 0 and coluna + i < 8:
                movimentos.append((linha - i, coluna + i))
        return movimentos

class Cavalo(Peca):
    def movimentos_possiveis(self, posicao):
        linha, coluna = posicao
        movimentos = []
        offsets = [(2,1),(2,-1),(-2,1),(-2,-1),(1,2),(1,-2),(-1,2),(-1,-2)]
        for dl, dc in offsets:
            nl, nc = linha + dl, coluna + dc
            if 0 <= nl < 8 and 0 <= nc < 8:
                movimentos.append((nl, nc))
        return movimentos

class Rei(Peca):
    def movimentos_possiveis(self, posicao):
        linha, coluna = posicao
        movimentos = []
        for dl in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if dl == 0 and dc == 0:
                    continue
                nl, nc = linha + dl, coluna + dc
                if 0 <= nl < 8 and 0 <= nc < 8:
                    movimentos.append((nl, nc))
        return movimentos

class Rainha(Peca):
    def movimentos_possiveis(self, posicao):
        return Torre("Torre", self.cor).movimentos_possiveis(posicao) + Bispo("Bispo", self.cor).movimentos_possiveis(posicao)

class Peao(Peca):
    def movimentos_possiveis(self, posicao):
        linha, coluna = posicao
        movimentos = []
        if self.cor == "branco":
            if linha > 0:
                movimentos.append((linha - 1, coluna))
        else:
            if linha < 7:
                movimentos.append((linha + 1, coluna))
        return movimentos

# Exemplo de uso
if __name__ == "__main__":
    cavalo = Cavalo("Cavalo", "branco")
    pos = (4, 4)
    print("Movimentos possíveis do Cavalo:")
    print(cavalo.movimentos_possiveis(pos))
