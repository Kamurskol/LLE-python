#criando a classse contatos
class Contato:
#adicionando os atributos ao construtor _init_
    def __init__(self, nome, telefone, email):
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.proximo = None

#criando a lista que irá conter os contatos
class ListaContatos:
    def __init__(self):
#o None significa que a lista está vazia
        self.primeiro = None

#metodo que irá adicionar contatos à lista
    def adicionar_contato(self, nome, telefone, email):
        novo_contato = Contato(nome, telefone, email)
        if not self.primeiro:
#se a lista estiver vazia, o novo contato será o primeiro
            self.primeiro = novo_contato
        else:
#senão, percorre-se a lista até o último contato
            atual = self.primeiro
            while atual.proximo:

#o novo contato é adicionado como o próximo do último
                atual = atual.proximo
            atual.proximo = novo_contato


    def pesquisar_contato(self, nome):
        atual = self.primeiro
        while atual:
            if atual.nome == nome:
                return atual
            atual = atual.proximo
        return None

    def remover_contato(self, nome):
        anterior = None
        atual = self.primeiro
        while atual:
            if atual.nome == nome:
                if anterior:
                    anterior.proximo = atual.proximo
                else:
                    self.primeiro = atual.proximo
                return True
            anterior = atual
            atual = atual.proximo
        return False

#criar a lista de contatos
lista_contatos = ListaContatos()

#adicionar contatos
lista_contatos.adicionar_contato("João", "123456789", "joao@email.com")
lista_contatos.adicionar_contato("Maria", "987654321", "maria@eemail.com")

#pesquisar contato
contato = lista_contatos.pesquisar_contato("João")
if contato:
    print("Contato encontrado:", contato.nome, contato.telefone, contato.email)
else:
    print("Contato não encontrado.")

#remover contato
removido = lista_contatos.remover_contato("Maria")
if removido:
    print("Contato removido com sucesso.")
else:
    print("Contato não encontrado.")

#pesquisar o contato removido
contato = lista_contatos.pesquisar_contato("Maria")
if contato:
    print("Contato encontrado:", contato.nome, contato.telefone, contato.email)
else:
    print("Contato não encontrado.")
