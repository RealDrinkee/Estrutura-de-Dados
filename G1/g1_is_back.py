class Funcoes:
    def __init__(self):
        self.lista_do_caralho = {
            "tamanho": 0,
            "inicio": None,
            "fim": None,
            "posicao_lista": 0
        }

    def get_tamanho(self):
        return self.lista_do_caralho.get("tamanho")
    
    def get_init(self):
        return self.lista_do_caralho.get("inicio")
    
    def get_fim(self):
        return self.lista_do_caralho.get("fim")
    
    def get_posicao_lista(self):
        return self.lista_do_caralho.get("posicao_lista")
    
    def ler_posicao_lista(self):
        print("Posição da lista:", self.lista_do_caralho.get("posicao_lista"))
        return self.lista_do_caralho.get("posicao_lista")


    def inserir_valor_lista(self):
        valor = str(input("Digite um valor: "))
        posicao_lista = int(input("Digite a posição que deseja adicionar: "))
        if self.lista_do_caralho.get("inicio") is None:
            self.lista_do_caralho.post("inicio", valor)
            self.lista_do_caralho.post("fim", valor)
            self.lista_do_caralho.post("posicao_lista" + 1)
            posicao_lista += 1
        else:
            novo_node = valor
            novo_node.proximo = self.lista_do_caralho["inicio"]
            self.lista_do_caralho["inicio"] = novo_node   

f = Funcoes()
f.__init__()
f.inserir_valor_lista()
f.ler_posicao_lista()
