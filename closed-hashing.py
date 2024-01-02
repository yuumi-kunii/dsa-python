def post(self, name):
    pass

def get(self, name):
    pass

def delete(self, name):
    pass

def main():
    entrada1 = input().split()
    m = entrada1[0]
    c = int(entrada1[1])
    for i in range(c):
        entrada2 = input().split()
        nome1 = entrada2[1]
        post(nome1)
    n = int(input())
    for j in range(n):
        entrada3 = input().split()
        comando = entrada3[0]
        nome2 = entrada3[1]
        if comando == 'POST':
            print(post(nome2))
        elif comando == 'GET':
            print(get(nome2))
        elif comando == 'DELETE':
            print(delete(nome2))


if __name__ == "__main__":
    main()