class Node:
    def __init__(self, name):
        self.name = name
        self.next = None


class Hashtable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def hash_function(self, name):
        soma = 0
        i = 1
        for letter in name:
            soma += (ord(letter) * i)
            i += 1
        result = (soma * 17) % self.size
        return result

    def post(self, name):
        index = self.hash_function(name)
        if self.get(name) == '404 - NOT FOUND':
            node = Node(name)
            node.next = self.table[index]
            self.table[index] = node

    def get(self, name):
        index = self.hash_function(name)
        cur = self.table[index]
        pos = 1
        while cur is not None:
            if cur.name == name:
                return "{} {}".format(index, pos)
            else:
                cur = cur.next
                pos += 1
        return "404 - NOT FOUND"

    def delete(self, name):
        index = self.hash_function(name)
        cur = self.table[index]
        prev = None
        while cur is not None:
            if cur.name == name:
                if prev is not None:
                    prev.next = cur.next
                else:
                    self.table[index] = cur.next
                print('DELETADO')
            prev = cur
            cur = cur.next



def main():
    entrada1 = input().split()
    m = int(entrada1[0])
    hash = Hashtable(m)
    c = int(entrada1[1])
    for i in range(c):
        entrada2 = input().split()
        nome1 = entrada2[1]
        hash.post(nome1)
    n = int(input())
    for j in range(n):
        entrada3 = input().split()
        comando = entrada3[0]
        nome2 = entrada3[1]
        if comando == 'POST':
            hash.post(nome2)
        elif comando == 'GET':
            print(hash.get(nome2))
        elif comando == 'DELETE':
            hash.delete(nome2)


if __name__ == "__main__":
    main()