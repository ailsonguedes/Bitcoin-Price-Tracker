import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import Widget
import PIL
from PIL import ImageTk
from PIL import Image

#Import librarys of bitcoin tracker
import requests
import json

color1 = "#586F7C" #Payne's Grey
color2 = "#F4F4F9" #Ghost White
color3 = "#B8DBD9" #Light Blue

# Create main window
mainScreen = Tk()
mainScreen.title("Monitorador de Bitcoin")
mainScreen.geometry("320x350")
mainScreen.resizable(width=False, height=False)
mainScreen.config(bg=color1)
mainScreen.iconbitmap("C:/Users/55759/OneDrive/Área de Trabalho/Python/WorkSpacePy/Bitcoin Price Tracker/Images/icon_bitcoin.ico")

#separete janela into 2 frames
ttk.Separator(mainScreen, orient=HORIZONTAL).grid(row=0, columnspan=1, ipadx=157)

upFrame = Frame(mainScreen, width=320, height=50, bg=color2, pady=0, padx=0, relief='flat')
upFrame.grid(row=1, column=0)

downFrame = Frame(mainScreen, width=320, height=300, bg=color1, pady=0, padx=0, relief='flat')
downFrame.grid(row=2, column=0, sticky=NW)

# func for tracking of datas

def info():
    ApiLink = "https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD%2CEUR%2CBRL%2CCNY"

    #HTTP requests
    response = requests.get(ApiLink)

    #converte data in dictionary
    data = response.json()

    # USD
    valUsd = float(data['USD'])
    valFormUsd = "$ {:,.3f}".format(valUsd)
    labelPriceUsd['text'] = valFormUsd

    # EUR
    valEur = float(data['EUR'])
    valFormEur = "€ {:,.3f}".format(valEur)
    labelPriceEuro['text'] = "Em Yuan é EUR:" + valFormEur

    # BRL
    valBrl= float(data['BRL'])
    valFormBrl = "R$ {:,.3f}".format(valBrl)
    labelPriceReal['text'] = "Em Yuan é BRL:" + valFormBrl

    # CNY
    valCny = float(data['CNY'])
    valFormCny = "¥ {:,.3f}".format(valCny)
    labelPriceYuan['text'] = "Em Yuan é CNY:" + valFormCny

    downFrame.after(1000, info)


#config upFrame
img = Image.open('C:/Users/55759/OneDrive/Área de Trabalho/Python/WorkSpacePy/Bitcoin Price Tracker/Images/bitImg.png')
img = img.resize((30,30), Image.ANTIALIAS)
img = ImageTk.PhotoImage(img)

labelIcon = Label(upFrame, image=img, compound=LEFT, bg=color2, relief=FLAT)
labelIcon.place(x=10, y=10)

labelName = Label(upFrame, text='Bitcoin Price Tracker', bg=color2, fg= color1, relief=FLAT, anchor='center', font=('Arial 20'))
labelName.place(x=50, y=5)

# config downFrame
labelPriceUsd = Label(downFrame, text='', bg=color1, fg= color3, relief=FLAT, anchor='center', font=('Arial 20'))
labelPriceUsd.place(x=80, y=50)

labelPriceEuro = Label(downFrame, text='', bg=color1, fg= color3, relief=FLAT, anchor='center', font=('Arial 12'))
labelPriceEuro.place(x=50, y=130)

labelPriceReal = Label(downFrame, text='', bg=color1, fg= color3, relief=FLAT, anchor='center', font=('Arial 12'))
labelPriceReal.place(x=50, y=160)

labelPriceYuan = Label(downFrame, text='', bg=color1, fg= color3, relief=FLAT, anchor='center', font=('Arial 12'))
labelPriceYuan.place(x=50, y=190)


info()

mainScreen.mainloop()