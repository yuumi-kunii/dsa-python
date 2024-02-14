class Grafo:
    def __init__(self, n):
        self.adj_list = [None] * n

    def criar_aresta(self, v1, v2):
        v1 = int(v1)
        v2 = int(v2)
        if self.adj_list[v1] is None:
            self.adj_list[v1] = [v2]
        else:
            self.adj_list[v1] = [v2] + self.adj_list[v1]
        if self.adj_list[v2] is None:
            self.adj_list[v2] = [v1]
        else:
            self.adj_list[v2] = [v1] + self.adj_list[v2]

    def print_list(self, v):
        lista = self.adj_list[v]
        if lista is not None:
            conc_list = " ".join(str(i) for i in lista)
            txt = "{}: {} ".format(v, conc_list)
            print(txt)
        else:
            txt = "{}: Lista Vazia".format(v)
            print(txt)

    def dfs(self, v, visitado, antecessor, caminho):
        visitado[v] = True
        if self.adj_list[v] is not None:
            caminho += [v]
            for u in self.adj_list[v]:
                if not visitado[u]:
                    antecessor[u] = v
                    self.dfs(u, visitado, antecessor, caminho)

    def busca_profundidade(self, n):
        visitado = [False] * n
        antecessor = [-1] * n
        caminho = []
        for v in range(0, n):
            if not visitado[v]:
                self.dfs(v, visitado, antecessor, caminho)
        caminho_format = ' '.join(str(i) for i in caminho)
        print(caminho_format, end=' ')


def main():
    n = int(input())
    g = Grafo(n)
    entrada = input().split(' ')
    g.criar_aresta(int(entrada[0]), int(entrada[1]))
    continua = int(entrada[2])
    while continua == 1:
        entrada2 = input().split(' ')
        g.criar_aresta(entrada2[0], entrada2[1])
        continua = int(entrada2[2])
    for v in range(n):
        g.print_list(v)
    print('')
    g.busca_profundidade(n)

if __name__ == '__main__':
    main()