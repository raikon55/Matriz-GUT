#!/bin/usr/env python3

import tkinter
from tkinter.messagebox import showinfo
from tkinter.ttk import Combobox

"""
AXIS padrão é 100, para deslocar para cima, substraia um valor e 
para baixo, adicione um valor.

Deslocar o AYIS para esquerda, substraia, e adicione para deslocar
para direita
"""
AXIS = 100
AYIS = 100

class Janela(tkinter.Frame):
    
    opcoesComboBox = list( range(1,6) )

    def __init__(self, master = None):
        tkinter.Frame.__init__(self, master)
        self.master = master

        self.pack(fill=tkinter.BOTH, expand=1)
        botaoSair = tkinter.Button(self, text="Sair", command=self.clickBotaoSair)
        botaoSalvar = tkinter.Button(self, text="Salvar", command=self.clickBotaoSalvar)
        botaoProximo = tkinter.Button(self, text="Proximo", command=self.clickBotaoProximo)

        self.setLabels()
        self.setCampoTexto()

        botaoSalvar.place(x=AXIS-50, y=AYIS+66)
        botaoProximo.place(x=AXIS+20, y=AYIS+66)
        botaoSair.place(x=AXIS+95, y=AYIS+66)

    def setCampoTexto(self):
        self.textoTarefa = tkinter.Entry(self)
        self.textoTarefa.place(x=AXIS+10, y=AYIS-60)

        self.textoGravidade = tkinter.Entry(self)
        self.textoGravidade.place(x=AXIS+10, y=AYIS-40)

        self.textoUrgencia = tkinter.Entry(self)
        self.textoUrgencia.place(x=AXIS+10, y=AYIS-20)

        self.textoTendencia = tkinter.Entry(self)
        self.textoTendencia.place(x=AXIS+10, y=AYIS)

    def setLabels(self):
        self.labelTendencia = tkinter.Label(self, text="Insira a tarefa que se deseja\ncalcular o G.U.T.")
        self.labelTendencia.place(x=AXIS-50, y=AYIS-100)

        self.labelTarefa = tkinter.Label(self, text="Tarefa")
        self.labelTarefa.place(x=AXIS-55, y=AYIS-60)

        self.labelGravidade = tkinter.Label(self, text="Gravidade")
        self.labelGravidade.place(x=AXIS-55, y=AYIS-40)

        self.labelUrgencia = tkinter.Label(self, text="Urgência")
        self.labelUrgencia.place(x=AXIS-55, y=AYIS-20)

        self.labelTendencia = tkinter.Label(self, text="Tendência")
        self.labelTendencia.place(x=AXIS-55, y=AYIS)

    def clickBotaoSair(self):
        root.destroy()

    def clickBotaoProximo(self):
        tarefa = str( self.textoTarefa.get() )
        gravidade = int( eval(self.textoGravidade.get()) )
        urgencia = int( eval(self.textoUrgencia.get()) )
        tendencia = int( eval(self.textoTendencia.get()) )

        insercao(resultList, gut(tarefa, gravidade, urgencia, tendencia))

        labelSalvo = tkinter.Label(self, text=f"{len(resultList)} entrada(s) salva(s)!")
        labelSalvo.place(x=AXIS, y=AYIS+20)
        
        self.textoTarefa.delete(0, "end")
        self.textoGravidade.delete(0, "end")
        self.textoUrgencia.delete(0, "end")
        self.textoTendencia.delete(0, "end")

    def clickBotaoSalvar(self):
        tempList = list()
        with open('matrixGut.txt', 'w+') as file:
            for i in range( len(resultList) ):
                file.write(f'Tarefa: {resultList[i][0]} -> peso: {resultList[i][1]}\n')
                tempList.append(f"Tarefa: {resultList[i][0]} -> peso: {resultList[i][1]}\n")
        self.popUpTasks(tempList)

    def popUpTasks(self, taskList):
        showinfo("Resultado da matriz", "\n".join(taskList))


def gut(label, gravidade, urgencia, tendencia):
    """
    Função para calcular G.U.T.
    Retorna uma tupla com o nome e o peso calculado
    """
    if gravidade > 5:
        gravidade = 5
    elif gravidade < 1:
        gravidade = 1

    if urgencia > 5:
        urgencia = 5
    elif urgencia < 1:
        urgencia = 1

    if tendencia > 5:
        tendencia = 5
    elif tendencia < 1:
        tendencia = 1

    resultado = gravidade * urgencia * tendencia
    return (label, resultado)

def insercao(lista, novoItem):
    """
    Insere em ordem decrescente em uma lista
    """
    if len(lista) == 0:
        lista.append(novoItem)
        return

    for i in range( len(lista) ):
        if novoItem not in lista and novoItem[1] >= lista[i][1]:
            lista.insert(i, novoItem)
        elif novoItem not in lista:
            lista.append(novoItem)

resultList = list()

root = tkinter.Tk()
app = Janela(root)
root.wm_title("Matriz G.U.T.")
root.geometry("290x200")
root.mainloop()