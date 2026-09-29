# -*- coding: utf-8 -*-
###########################################################################################
#########################################################################################
# Turma:
# Professor:
# Nome completo:
# Matrícula PUC-Rio:

###########################################################################################
###########################################################################################
'''
Questão 2 
Teste as classes construídas por você, executando o código que se encontra 
comentado na área de testes 

'''
from dataP1 import *
#Escreva aqui a classe Arquivo

class Arquivo:
    def __init__(self, nome_arq : str, autor : str, data_cria : Data, texto : str = "") -> None:
        self.nome_arq = nome_arq
        self.autor = autor
        self.data_cria = data_cria
        self.texto = texto
        self.data_ult_mod = data_cria
        
    def tamanho(self) -> int:
        return len(self.texto)
        
    def __str__(self) -> str:
        return f'Nome do arquivo: {self.nome_arq}.txt\nAutor: {self.autor}\nData de criação: {self.data_cria}\nTamanho do arquivo: {self.tamanho()}'

    def __repr__(self) -> str:
        return f'Nome do arquivo: {self.nome_arq}.txt\nAutor: {self.autor}\nData de criação: {self.data_cria}\nTamanho do arquivo: {self.tamanho()}'

    def __add__(self, arq_ext : 'Arquivo') -> 'Arquivo': # O tipo atribuído a instância se chama referência Antecipada, em que há uma "metalinguagem" do objeto antes que esse seja encerrado
       novo_nome = self.nome_arq + arq_ext.nome_arq
       novo_autor = "sistema"
       nova_data = Data()
       novo_txt = self.texto + "\n" + arq_ext.texto
       
       return (Arquivo(novo_nome, novo_autor, nova_data, novo_txt))    
    
    def substituiTexto(self, Texto : str, objdata : 'Data'):
        self.texto = Texto
        self.data_ult_mod = objdata
       
    def adicionaTexto(self, Texto : str, objdata : 'Data'):
        self.texto = self.texto + Texto # ou self.texto =+ Texto 
        self.data_ult_mod = objdata
        
    def exibeTexto(self):
        print(self.texto)
        
    def ultimaAlteracaoNaData(self, dataestipu : 'Data') -> bool:
        return self.data_ult_mod == dataestipu
    
#Escreva aqui a classe Pasta

class Pasta:
    def __init__(self, nome_pasta : str):
        self.nome_pasta = nome_pasta        
        self.lista_pastas = []
    
    def __str__(self) -> str:
        return f"Nome da pasta: {self.nome_pasta}\nQuantidade de arquivos na pasta:{len(self.lista_pastas)}"
    
    
    def __repr__(self) -> str:
        return f"Nome da pasta: {self.nome_pasta}\nQuantidade de arquivos na pasta:{len(self.lista_pastas)}"
            
    def incluiArquivo(self,arq_criado : 'Arquivo'):
        self.lista_pastas.append(arq_criado)
    
    def exibeArquivos(self) -> None:
        if len(self.lista_pastas) == 0:
            print("Pasta vazia")
        else:
            for elem in self.lista_pastas:
                print(elem)

    def alteradosNaData(self, data : 'Data') -> None:
        for arquivo in self.lista_pastas:
            if arquivo.ultimaAlteracaoNaData(data):
                print(arquivo)
        
        
        
    
    
#-------- Área de teste da questao 2 --------
print('\n------ Teste da Q2 ------')
'''Retire # das linhas abaixo'''
print("\n=====================================")
print("ARQUIVOS CRIADOS")
print("=====================================")

arq1=Arquivo('comprasFrutas','fifi',Data(12,4,2023),'abacate,pera,abacaxi,manga')
print(arq1)
print("Texto do arquivo: ")
arq1.exibeTexto()

'''Adicionando texto'''
dtAlteracao=Data(19,4,2023)
arq1.adicionaTexto(',banana,laranja',dtAlteracao)
print("\n")
print(arq1)
print("Texto do arquivo: ")
arq1.exibeTexto()

'''Teste da data da última alteração'''
if arq1.ultimaAlteracaoNaData(dtAlteracao):
    print("\n\n-->A última alteração do arquivo FOI em {}".format(dtAlteracao))
else:
    print("\n\n-->A última alteração do arquivo NÃO foi em {}}".format(dtAlteracao))

print("--------------------------------")
print("--------------------------------")

arq2=Arquivo('comprasBebidas','guga',Data(10,4,2023))
print(arq2)
print("Texto do arquivo: ")
arq2.exibeTexto()

'''Substituindo texto'''
arq2.substituiTexto('suco,água',Data(21,4,2023))
print("\n")
print(arq2)
print("Texto do arquivo: ")
arq2.exibeTexto()

print("--------------------------------")
print("--------------------------------")

'''Juntando dois arquivos'''
arq3=arq1+arq2
print(arq3)
print("Texto do arquivo: ")
arq3.exibeTexto()

'''Teste da data da última alteração'''
hoje=Data()
if arq2.ultimaAlteracaoNaData(hoje):
    print("\n\n-->A última alteração do arquivo FOI em {}".format(hoje))
else:
    print("\n\n-->A última alteração do arquivo NÃO foi em {}".format(hoje))



print("--------------------------------")
print("--------------------------------")

arq4=Arquivo('convBibi','bibi',Data(1,4,2023),'juca,keko,kaka,lilo,mano,mimi,dora,zeze')
print(arq4)
print("Texto do arquivo: ")
arq4.exibeTexto()

print("--------------------------------")
print("--------------------------------")

print("\n======================================")
print("PASTA CRIADA")
print("======================================")
pasta1=Pasta('festaNiver')
print(pasta1)
print("--------------------------------")
print("Arquivos da pasta")
pasta1.exibeArquivos()


print("\n======================================")
print("ARQUIVOS INCLUIDOS NAS PASTAS")
print("======================================")

'''Incluindo arquivos na pasta '''
pasta1.incluiArquivo(arq1)
pasta1.incluiArquivo(arq2)
pasta1.incluiArquivo(arq3)
pasta1.incluiArquivo(arq4)

'''Exibindo pasta atualizada'''
print(pasta1)
print("Arquivos da pasta")
pasta1.exibeArquivos()
print("--------------------------------")

'''Exibindo arquivos modificados em determinada data'''
print("Arquivos alterado hoje na pasta {}\n".format(pasta1))
pasta1.alteradosNaData(Data())


print('\n---- Fim do Teste da Q3 ----')             
