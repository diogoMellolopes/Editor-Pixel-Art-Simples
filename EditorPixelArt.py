from tkinter import *

class PixelArt():
    def __init__(self, tamanhoGrid = 9):
        self.tamanhoGrid = tamanhoGrid

    def criarGrid(self):
        self.grid = [[" " for i in range(0, self.tamanhoGrid)] for j in range(0, self.tamanhoGrid)]

class Menu():
    def __init__(self, master = None, mudarCenario = None):
        fontePadrao = ("Courier New", "13")
        self.tamanhoGrid = 0
        self.mudarCenario = mudarCenario

        self.primeiroContainer = Frame(master)
        self.primeiroContainer.pack()
        Label(self.primeiroContainer, text = "Digite qual o tamanho da grid que deseja: ", font = fontePadrao, bg = "white").pack(side = LEFT)
        self.quantidade = Entry(self.primeiroContainer, font = fontePadrao, width = 15, validate = "key", validatecommand = (master.register(lambda texto: len(texto) <= 2), "%P"))
        self.quantidade.pack(side = LEFT)

        self.terceiroContainer = Frame(master)
        self.terceiroContainer.pack()
        Label(self.terceiroContainer, text = "Digite se quer ativar o grid: (s - sim / n - não): ", font = fontePadrao, bg = "white").pack(side = LEFT)
        self.grid = Entry(self.terceiroContainer, font = fontePadrao, width = 6, validate = "key", validatecommand = (master.register(lambda texto: len(texto) <= 1), "%P"))
        self.grid.pack(side = LEFT)

        self.segundoContainer = Frame(master)
        self.segundoContainer.pack()
        Button(self.segundoContainer, text = "Avançar", font = fontePadrao, width = 12, bg = "white", command = self.iniciarInterface).pack()

    def destruir(self):
        self.primeiroContainer.destroy()
        self.segundoContainer.destroy()
        self.terceiroContainer.destroy()

    def iniciarInterface(self):
        try:
            self.tamanhoGrid = int(self.quantidade.get())
        except ValueError:
            self.tamanhoGrid = 18
        if self.tamanhoGrid <= 0 or self.tamanhoGrid > 99:
            self.tamanhoGrid = 18
        self.gridAtivo = self.grid.get()
        if self.gridAtivo == "s" or self.gridAtivo == "S":
            self.gridAtivo = 1
        else:
            self.gridAtivo = 0
        self.mudarCenario("interface", self.tamanhoGrid, self.gridAtivo)

class Interface():
    def __init__(self, master = None, tamanhoGrid = 0, gridAtivo = 2, mudarCenario = None):
        self.tamanhoGrid = tamanhoGrid
        self.mudarCenario = mudarCenario
        self.gridAtivo = gridAtivo
        fontePadrao = ("Courier New", "13")
        self.interface = PixelArt(self.tamanhoGrid)
        self.interface.criarGrid()
        self.temp = ""
        contColuna = 1
        contLinha = 0

        self.primeiroContainer = Frame(master)
        self.primeiroContainer.pack()
        self.botoes = []
        for i in range(0, tamanhoGrid):
            for j in range(0, tamanhoGrid):
                if gridAtivo == 1:
                    Frame(self.primeiroContainer, width = 1, bg = "black", height = 28).grid(row = i + contLinha, column = 0, padx = 0, pady = 0, sticky = "nsew")
                coordenada = str(i) + str(j)
                botao = Button(self.primeiroContainer, text = str(self.interface.grid[i][j]), width = 2, height = 1, borderwidth = 0, relief = "flat", bg = "white", padx = 0, pady = 0)
                botao.grid(row = i + contLinha, column = j + contColuna, sticky = "nsew")
                botao.config(command = lambda b = botao, c = coordenada: self.atualizar(b, c))
                self.botoes.append(botao)
                self.botoes.append(coordenada)
                if gridAtivo == 1:
                    Frame(self.primeiroContainer, width = 0, bg = "black", height = 28, relief = "flat", padx = 0, pady = 0).grid(row = i + contLinha, column = j + contColuna + 1, sticky = "nsew")
                    Frame(self.primeiroContainer, height = 0, bg = "black", width = 28, relief = "flat", padx = 0, pady = 0).grid(row = i + contLinha + 1, column = j + contColuna, sticky = "nsew")
                    contColuna += 1
            if gridAtivo == 1:
                contLinha += 2
                contColuna = 1
        contLinha = 0

        self.segundocontainer = Frame(master)
        self.segundocontainer.pack()
        Label(self.segundocontainer, text = "Pinte com estas cores: ", font = fontePadrao, bg = "white").pack()

        self.terceiroContainer = Frame(master)
        self.terceiroContainer.pack()

        cores = ["white", "black", "blue", "green", "red", "yellow", "pink", "purple", "orange", "cyan", "silver", "gray", "#189BCC", "#01EE01", "#B22222", "gold", "#C71585", "#DA70D6", "#D2691E", "#8B4513"]
        for i, cor in enumerate(cores):
            escolhaBotao = Button(self.terceiroContainer, bg = cor, width = 2, height = 1)
            escolhaBotao.grid(row = i // 10, column = i % 10)
            escolhaBotao.config(command = lambda cor = escolhaBotao: self.escolha(cor))

    def atualizar(self, botao, coordenada):
        botao["bg"] = self.temp

    def escolha(self, cor):
        self.temp = cor["bg"]

class Aplicacao():
    def __init__(self, master):
        self.master = master
        self.cenarioAtual = None
        self.carregarCenario("menu")

    def carregarCenario(self, cenario, tamanhoGrid = 0, gridAtivo = ""):
        if self.cenarioAtual:
            self.cenarioAtual.destruir()
        if cenario == "menu":
            self.cenarioAtual = Menu(self.master, self.carregarCenario)
        elif cenario == "interface":
            self.cenarioAtual = Interface(self.master, tamanhoGrid, gridAtivo, self.carregarCenario)

if __name__ == "__main__":
    root = Tk()
    root.config(bg = "white")
    root.title("Editor de Pixel Art")
    app = Aplicacao(root)
    root.mainloop()