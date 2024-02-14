class Heap:
    def __init__(self):
        self.heap = []

    def post(self, nome, p):
        pass

    def get(self, nome, c):
        pass

    def delete(self, nome, c):
        pass

def main():
    entrada1 = input().split()
    f = int(entrada1[0])
    q = int(entrada1[1])
    heap = Heap(f, q)
    n = int(input())
    for i in range(n):
        entrada2 = input().split()
        if entrada2[0] == "CAD":
            nome = entrada2[1]
            p = entrada2[2]
            heap.post(nome, p)




if __name__ == "__main__":
    main()