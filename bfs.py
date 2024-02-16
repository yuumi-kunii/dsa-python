class Labirinto:
    def __init__(self, m, n):
        self.linhas = m
        self.colunas = n
        self.matriz = [[None] * self.colunas] * self.linhas

    def mov_valido(self, x, y, visitados):
        if self.linhas > x >= 0 and self.colunas > y >= 0 and self.matriz[x][y] != 1 and not visitados[x][y]:
            return True
        else:
            return False

    def bfs(self):
        linhas = self.linhas
        colunas = self.colunas
        visitados = [[False] * colunas for _ in range(linhas)]
        direcoes = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        fila = []
        for i in range(linhas):
            for j in range(colunas):
                if self.matriz[i][j] == 2:
                    fila = [(i, j, 0)]
                    visitados[i][j] = True
        while fila:
            linha, coluna, dist = fila[0]
            del fila[0]
            if self.matriz[linha][coluna] == 3:
                return dist
            for d_linha, d_coluna in direcoes:
                linha2, coluna2 = linha + d_linha, coluna + d_coluna
                if self.mov_valido(linha2, coluna2, visitados):
                    fila = fila + [(linha2, coluna2, dist + 1)]
                    visitados[linha2][coluna2] = True
        return "Labirinto Impossivel"


def main():
    entrada = input().split()
    linhas = int(entrada[0])
    colunas = int(entrada[1])
    l = Labirinto(linhas, colunas)
    for i in range(linhas):
        linha = input().split()
        linha_int = [int(item) for item in linha]
        l.matriz[i] = linha_int
    print(l.bfs())


if __name__ == '__main__':
    main()