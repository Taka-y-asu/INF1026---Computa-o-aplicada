class Ponto:
    x : float
    y : float
    def __init__(self, x : float , y : float): #Inicializa as variáveis, 
        self.x = x
        self.y = y
        
    def __repr__(self):
        return f'({self.x},{self.y})' #retorna o equivalente ao print
    
    def calcula_tamanho(self) -> float:
        return(self.x ** 2 + self.y ** 2) ** 0.5



def main():
    p1 = Ponto(1,1)
    tamanho = p1.calcula_tamanho()
    print(p1,tamanho)
    
if __name__ == "__main__":
    main()
    