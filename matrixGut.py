#!/bin/usr/env python3

import tkinter
from tkinter.messagebox import showinfo
from tkinter.ttk import Combobox

class Janela(tkinter.Frame):
    """
    AXIS padrão é 100, para deslocar para cima, substraia um valor e 
    para baixo, adicione um valor.

    Deslocar o AYIS para esquerda, substraia, e adicione para deslocar
    para direita
    """
    AXIS = 100
    AYIS = 100

    opcoesComboBox = list( range(1,6) )

    def __init__(self, master = None):
        tkinter.Frame.__init__(self, master)
        self.master = master

        self.pack(fill=tkinter.BOTH, expand=1)
        botaoSair = tkinter.Button(self, text="Sair", command=self.clickBotaoSair)
        botaoSalvar = tkinter.Button(self, text="Salvar", command=self.clickBotaoSalvar)
        botaoProximo = tkinter.Button(self, text="Proximo", command=self.clickBotaoProximo)

        self.setLabels()
        self.setCampos()

        botaoSalvar.place(x=self.AXIS-50, y=self.AYIS+66)
        botaoProximo.place(x=self.AXIS+20, y=self.AYIS+66)
        botaoSair.place(x=self.AXIS+95, y=self.AYIS+66)

    def setCampos(self):
        """
        Desenha os campos de entrada no Frame, e configura os 'comboboxes'(?)
        tornando-os apenas como leitura
        """
        self.textoTarefa = tkinter.Entry(self)
        self.textoTarefa.place(x=self.AXIS+10, y=self.AYIS-60)

        self.comboGravidade = Combobox(self, values=self.opcoesComboBox, state='readonly')
        self.comboGravidade.place(x=self.AXIS+10, y=self.AYIS-40)
        self.comboGravidade.current(0)

        self.comboUrgencia = Combobox(self, values=self.opcoesComboBox, state='readonly')
        self.comboUrgencia.place(x=self.AXIS+10, y=self.AYIS-20)
        self.comboUrgencia.current(0)

        self.comboTendencia = Combobox(self, values=self.opcoesComboBox, state='readonly')
        self.comboTendencia.place(x=self.AXIS+10, y=self.AYIS)
        self.comboTendencia.current(0)

    def setLabels(self):
        """
        Posiciona os labels no Frame
        """
        self.labelTendencia = tkinter.Label(self, 
            text="Insira a tarefa que se deseja\ncalcular o G.U.T.")
        self.labelTendencia.place(x=self.AXIS-50, y=self.AYIS-100)

        self.labelTarefa = tkinter.Label(self, text="Tarefa")
        self.labelTarefa.place(x=self.AXIS-55, y=self.AYIS-60)

        self.labelGravidade = tkinter.Label(self, text="Gravidade")
        self.labelGravidade.place(x=self.AXIS-55, y=self.AYIS-40)

        self.labelUrgencia = tkinter.Label(self, text="Urgência")
        self.labelUrgencia.place(x=self.AXIS-55, y=self.AYIS-20)

        self.labelTendencia = tkinter.Label(self, text="Tendência")
        self.labelTendencia.place(x=self.AXIS-55, y=self.AYIS)

    def clickBotaoSair(self):
        root.destroy()

    def clickBotaoProximo(self):
        tarefa = str( self.textoTarefa.get() )
        gravidade = int( eval(self.comboGravidade.get()) )
        urgencia = int( eval(self.comboUrgencia.get()) )
        tendencia = int( eval(self.comboTendencia.get()) )

        insercao(resultList, gut(tarefa, gravidade, urgencia, tendencia))

        labelSalvo = tkinter.Label(self, text=f"{len(resultList)} entrada(s) salva(s)!")
        labelSalvo.place(x=self.AXIS, y=self.AYIS+20)
        
        self.textoTarefa.delete(0, "end")

    def clickBotaoSalvar(self):
        tempList = list()
        with open('matrixGut.txt', 'w+') as file:
            for i in range( len(resultList) ):
                file.write(f'Tarefa: {resultList[i][0]} -> \
                    peso: {resultList[i][1]}\n')
                tempList.append(f"Tarefa: {resultList[i][0]} -> \
                    peso: {resultList[i][1]}\n")
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
root.iconphoto(False, tkinter.PhotoImage(file='matrix.png'))
root.mainloop()