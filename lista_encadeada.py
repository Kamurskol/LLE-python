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

#criando o método para quesquisar contatos
    def pesquisar_contato(self, nome):
        atual = self.primeiro
        while atual:
#vai percorrer a lista procurando pelo nome fornecido
            if atual.nome == nome:
#se encontrar o contato, o retorna
                return atual
            atual = atual.proximo
#senão, retorna none
        return None

    #método de remoção de contato
    def remover_contato(self, nome):
        anterior = None
    #a var anterior é definida como none.
        atual = self.primeiro
    #ela será usada para rastrear o nó anterior ao nó atual
        while atual:
    #inicia-se um loop enquanto o nó atual não for nulo
            if atual.nome == nome:
                if anterior:
    #verifica-se se o nó atual não é o primeiro nó da lista (nulo).
                    anterior.proximo = atual.proximo
    #se não for, atualiza-se o ponteiro "próximo" do nó anterior para apontar para o próximo nó após o atual
                else:
    #se o nó atual for o primeiro da lista
                    self.primeiro = atual.proximo
    #atualiza-se o ponteiro para apontar para o próximo nó após o nó atual
                return True
    #após a remoção do contato, retorna-se true para indicar que a operação foi concluida com êxito.
            anterior = atual
    #atualiza-se a var "anterior" para que aponte para o nó atual
            atual = atual.proximo
    #se avança para o próximo nó da lista ao atualizar a var "atual"
        return False
    #caso o nome do contato não seja encontrado.

#criar a variável lista de contatos
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
