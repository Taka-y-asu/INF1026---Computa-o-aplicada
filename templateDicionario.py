# -*- coding: utf-8 -*-
"""
###############################################################################
###############################################################################
# Turma:
# Professor:
# Nome completo:
# Matrícula PUC-Rio:
###############################################################################
###############################################################################
"""

# QUESTÃO 1a: Dicionário do Imposto de Renda.

#-----------Escreva a seguir a funcao exibeTotalRecebidoPorUmCPF ------




def exibeTotalRecebidoPorUmCPF(dici : dict, cpf : str) -> None:
    quant = 0.0
    for recebedores in dici.values():
        for recebedor,valor in recebedores.items():
            if recebedor == cpf:
                quant += valor
    print(f"{cpf} recebeu no total R${quant:.2f}")

###################################################################
###################################################################

# QUESTÃO 1b: Dicionário dos tipos (fontes) de energia.

#-----------Escreva a seguir a funcao cria_dic_por_vantagem ------

'''
Considere um dicionário como o dic_energia disponibilizado na área de testes.
É um dicionário de dicionários com as informações 
sobre os diferentes tipos de energia. 
Obs: as informações não são confiáveis (obtidas com a ajuda do chatgpt) 
O dicionário externo tem: 
    CHAVE: tipo de energia 
    VALOR: dicionário interno com informações importantes sobre o tipo (fonte) de energia 
    E obrigatoriamente as CHAVEs de todos os dicionários internos são: 
        tecnologia        => tecnologia ou método usado para gerar energia a partir dessa fonte,  
        
        capacidade      => capacidade máxima ou potencial de geração desse tipo de energia, expressa em kW,  
        
        geracao            => atual quantidade de energia gerada desse tipo, expressa em kW,    
        
        eficiencia         => quão eficiente é a conversão dessa fonte de energia em energia utilizável, expressa 
        como percentagem entre 0 e 1 
        
        custo_por_kw => custo para gerar um kW desse tipo de energia (em uma determinada moeda) 
        
        vantagens         => lista de vantagens ou benefícios desse tipo de energia 
        
Exemplo de um elemento do dic_energia: 
    "solar": {"tecnologia": "Fotovoltaica", "capacidade": 1000, "geracao": 800, "eficiencia": 0.8, "custo_por_kw": 0.12, 
                    "vantagens": ["renovavel", "limpa", "baixos custos operacionais"]} 
Escreva uma função, denominada cria_dic_por_vantagem, que: 
  - receba um dicionário por energia como o descrito 
  - construa e retorne um dicionário por Vantagem (ou benefício), em que cada item é: 
CHAVE: a vantagem (benefício) 
VALOR: lista dos tipos de energia que apresentam essa vantagem. 
Por exemplo, para o dicionário dic_energia fornecido na área de testes, a função retornaria o seguinte dicionário: 
  {'renovavel': ['solar', 'eolica', 'hidreletrica', 'geotermica', 'biomassa'], 'limpa': ['solar'],  
   'baixos custos operacionais': ['solar'], 'sem emissões': ['eolica'], 'recurso abundante': ['eolica'],  
   'baixas emissoes': ['hidreletrica', 'geotermica', 'nuclear'], 'longa vida util': ['hidreletrica'],  
   'confiavel': ['geotermica', 'nuclear'], 'alta densidade energetica': ['nuclear'], 'utilizacao de residuos': ['biomassa']}  
'''


def cria_dic_por_vantagem(dic : dict) -> dict:
    dic_vant = {}
    for tipo,valores in dic.items():
        for nome_atr,características in valores.items():
            if nome_atr == 'vantagens':
                for res in características:
                    if res not in dic_vant:
                        dic_vant[res] = [tipo]
                    else:
                        dic_vant[res].append(tipo)
    return dic_vant
            



###################################################################
#                        BLOCO PRINCIPAL
###################################################################
#------------------------------------------------------------------
# -----------------  Area de Teste da questão 1a -------------------

dPorPagador= {'34534522-00': { '67167776-73':3200, '75167776-23':1500,'27197776-78':2200, '58587776-73':3200,
                               '55455324-26':2500, '34167716-32':1000 },
              '75167776-23': {'27197776-78':1500, '58587776-73':1100,'34167716-32':5000, '67167776-73':2400},
              '58587776-73': {'55455324-26':1200, '67167776-73':1000, '34167716-32':2000},
              '34167716-32': {'55455324-26':3000, '75167776-23':1800, '27197776-78':1650},
              '98167716-38': {'62345324-26':1000, '34567776-23':1300, '67167776-73':5000,'27197776-78':650},
              '373537522-00': {'67167776-73':2200, '75167776-23':500,'23237676-78':2100}        
             }


print('\n---------- Teste da questão 1a ----------')
# Tire os # das linhas a seguir
  
print('---Teste com CPF 67167776-73 ---' )
exibeTotalRecebidoPorUmCPF(dPorPagador,'67167776-73')

print('---Teste com CPF 99167776-74 ---' )
exibeTotalRecebidoPorUmCPF(dPorPagador,'99167776-74')

print('---Teste com CPF 55455324-26 ---' )
exibeTotalRecebidoPorUmCPF(dPorPagador,'55455324-26')



###################################################################
#------------------------------------------------------------------
# -----------------  Area de Teste da questão 1b -------------------

dic_energia = {
    "solar": {
        "tecnologia": "Fotovoltaica", "capacidade": 1000,  "geracao": 800,
        "eficiencia": 0.8, "custo_por_kw": 0.12,
        "vantagens": ["renovavel", "limpa", "baixos custos operacionais"]
    },
    "eolica": {
        "tecnologia": "Turbina de vento", "capacidade": 2000, "geracao": 1500,
        "eficiencia": 0.85,  "custo_por_kw": 0.10,
        "vantagens": ["renovavel", "sem emissões", "recurso abundante"]
    },
    "hidreletrica": {
        "tecnologia": "Turbina hidraulica", "capacidade": 3000, "geracao": 2500,
        "eficiencia": 0.75, "custo_por_kw": 0.07,
        "vantagens": ["renovavel", "baixas emissoes", "longa vida util"]
    },
    "geotermica": {
        "tecnologia": "Ciclo binário ou outro", "capacidade": 500, "geracao": 400,
        "eficiencia": 0.9, "custo_por_kw": 0.15,
        "vantagens": ["renovavel", "baixas emissoes", "confiavel"]
    },
    "nuclear": {
        "tecnologia": "Reator nuclear", "capacidade": 4000, "geracao": 3500,
        "eficiencia": 0.95, "custo_por_kw": 0.14,
        "vantagens": ["alta densidade energetica", "baixas emissoes", "confiavel"]
    },
    "biomassa": {
        "tecnologia": "Combustao", "capacidade": 800, "geracao": 600,
        "eficiencia": 0.82, "custo_por_kw": 0.11,
        "vantagens": ["renovavel", "utilizacao de residuos"]
    }
}

print('\n---------- Teste da questão 1b ----------')
# Tire os # das  linhas a seguir
dPorVant= cria_dic_por_vantagem(dic_energia)
print(dPorVant)




