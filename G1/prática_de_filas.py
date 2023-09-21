class No:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None  # Referência para o primeiro elemento da fila
        self.rear = None   # Referência para o último elemento da fila
        self.size = 0      # Tamanho da fila

    def is_empty(self):
        return self.size == 0

    def enqueue(self, data):
        new_node = No(data)
        if self.is_empty():
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            print("A fila está vazia.")
            return None
        data = self.front.data
        if self.front == self.rear:
            self.front = self.rear = None
        else:
            self.front = self.front.next
        self.size -= 1
        return data

    def get_size(self):
        return self.size

if __name__ == "__main__":
    fila = Queue()

    while True:
        print("\nOperações na Fila Encadeada:")
        print("1 - Inserir item (enqueue)")
        print("2 - Remover item (dequeue)")
        print("3 - Tamanho da fila")
        print("4 - Sair")

        escolha = int(input("Escolha uma opção: "))

        if escolha == 1:
            item = input("Digite o item a ser inserido: ")
            fila.enqueue(item)
            print(f"{item} foi inserido na fila.")
        elif escolha == 2:
            item = fila.dequeue()
            if item is not None:
                print(f"{item} foi removido da fila.")
        elif escolha == 3:
            tamanho = fila.get_size()
            print(f"Tamanho da fila: {tamanho}")
        elif escolha == 4:
            break
        else:
            print("Opção inválida. Tente novamente.")
