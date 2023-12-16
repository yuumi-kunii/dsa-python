class HashTable:
    def __init__(self, size):
        self.size = size
        self.hash_table = [None] * size
        self.deleted = object()

    def hash_function(self, key):
        return key % self.size

    def insert(self, key):
        index = self.hash_function(key)
        while index < self.size:
            if self.hash_table[index] is None or self.hash_table[index] is self.deleted:
                self.hash_table[index] = key
                break
            else:
                index += 1

    def search(self, key):
        index = self.hash_function(key)
        while index < self.size:
            if self.hash_table[index] == key:
                return index
            elif self.hash_table[index] is None:
                return None
            else:
                index += 1

    def delete(self, key):
        index = self.hash_function(key)
        while index < self.size:
            if self.hash_table[index] == key:
                self.hash_table[index] = self.deleted
                break
            else:
                index += 1


def print_open_hash_table(table):
    for i, item in enumerate(table):
        print(f"Posição {i}: {item}")

keys = [10, 22, 31, 4, 15, 28, 17, 88, 59]
open_hash_table = HashTable(11)
for key in keys:
    open_hash_table.insert(key)

print("\nTabela de Hash com Endereçamento Aberto (Antes da Exclusão):")
print_open_hash_table(open_hash_table.hash_table)

open_hash_table.delete(22)

print("\nTabela de Hash com Endereçamento Aberto (Após a Exclusão do 22):")
print_open_hash_table(open_hash_table.hash_table)