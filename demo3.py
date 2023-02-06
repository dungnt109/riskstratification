from tkinter import *
from tkinter import ttk

ws = Tk()
ws.title("Risk Stratification")
ws.geometry('1000x800')

var = IntVar()
var2 = IntVar()
var3 = IntVar()
    
question1  = Label(ws, text = "**High risk genetic subtype as defined by RNA-Sequencing d, pathogenic TP53 mutation, \nPAX5-altered (PAX5alt) with ikaros deletion (even if MRD negative tp#1)").grid(row=0, column=0, columnspan=5, sticky=W, padx=6, pady=6)

cold_bev = Radiobutton(ws, text="Yes", variable=var, value=1).grid(row=0, column=6)
hot_bev = Radiobutton(ws, text="No", variable=var, value=2).grid(row=0, column=7)

question2  = Label(ws, text = "**Infant ALL (< 1 years old) with CD10-ve/MLL-r").grid(row=3, columnspan=5,sticky=W, padx=6, pady=6)

Radiobutton(ws, text="Yes", variable=var2, value=1).grid(row=3, column=6)
Radiobutton(ws, text="No", variable=var2, value=2).grid(row=3, column=7)


question2  = Label(ws, text = "*MRD tp#1/D33≥ 1x 10^-2").grid(row=8, columnspan=5, sticky=W, padx=6, pady=6)

Radiobutton(ws, text="Yes", variable=var3, value=1).grid(row=8, column=6)
Radiobutton(ws, text="No", variable=var3, value=2).grid(row=8, column=7)

question3  = Label(ws, text = "**MRD tp#1b/w8 ≥ 1x 10^-3").grid(row=9, columnspan=5, sticky=W, padx=6, pady=6)

Radiobutton(ws, text="Yes", variable=var3, value=1).grid(row=9, column=6)
Radiobutton(ws, text="No", variable=var3, value=2).grid(row=9, column=7)

question4  = Label(ws, text = "**MRD at time point #2/w12 ≥ 1x 10^-4").grid(row=10, columnspan=5, sticky=W, padx=6, pady=6)

Radiobutton(ws, text="Yes", variable=var3, value=1).grid(row=10, column=6)
Radiobutton(ws, text="No", variable=var3, value=2).grid(row=10, column=7)

question5  = Label(ws, text = "**Bilateral testicular AL").grid(row=11, columnspan=5, sticky=W, padx=6, pady=6)

Radiobutton(ws, text="Yes", variable=var3, value=1).grid(row=11, column=6)
Radiobutton(ws, text="No", variable=var3, value=2).grid(row=11, column=7)

question6  = Label(ws, text = "**CNS+ beyond first 4 doses of IT MTX").grid(row=12, columnspan=5, sticky=W, padx=6, pady=6)

Radiobutton(ws, text="Yes", variable=var3, value=1).grid(row=12, column=6)
Radiobutton(ws, text="No", variable=var3, value=2).grid(row=12, column=7)

#separator = ttk.Separator(ws, orient=HORIZONTAL).grid (row=13,column =0, columnspan=5, sticky="ew")

#ttk.Separator(ws).place(x=0, y=26, relwidth=1)


ws.mainloop()
