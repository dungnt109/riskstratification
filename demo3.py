from tkinter import *
from tkinter import ttk
import tkinter as tk

ws = Tk()
ws.title("Risk Stratification")
ws.geometry('1000x800')

highArray = []
intermediateArray = []
standardArray = []

def clicked():
    for element in highArray: 

    	if element.get() == 1: 

    		show_popup("Risk Stratification: High Risk")
    		return  


    for element in intermediateArray: 

    	if element.get() == 1: 

    		show_popup("Risk Stratification: Intermediate Risk")
    		return 

    flag = True

    for element in standardArray: 

    	if element.get() != 1: 

    		flag = False 

    if flag: 

    		show_popup("Risk Stratification: Standard Risk")
    		return  



 
font = ("Arial", 15)


var1 = IntVar()
label1  = Label(ws, font=font, text = "**High risk genetic subtype as defined by RNA-Sequencing d, pathogenic TP53 mutation, \nPAX5-altered (PAX5alt) with ikaros deletion (even if MRD negative tp#1)").grid(row=0, column=0, columnspan=5, sticky=W, padx=6, pady=6)
leftbutton1 = Radiobutton(ws, font=font, text="Yes", variable=var1, value=1, command=clicked).grid(row=0, column=6)
rightbutton1 = Radiobutton(ws, font=font, text="No", variable=var1, value=2, command=clicked).grid(row=0, column=7)

var2 = IntVar()
label2  = Label(ws, font=font, text = "**Infant ALL (< 1 years old) with CD10-ve and/or MLL-r e").grid(row=1, column=0, columnspan=5, sticky=W, padx=6, pady=6)
leftbutton2 = Radiobutton(ws, font=font, text="Yes", variable=var2, value=1, command=clicked).grid(row=1, column=6)
rightbutton2 = Radiobutton(ws, font=font, text="No", variable=var2, value=2, command=clicked).grid(row=1, column=7)

var3 = IntVar()
label3  = Label(ws, font=font,  text = "*MRD tp#1/D33≥ 1x 10-2").grid(row=2, column=0, columnspan=5, sticky=W, padx=6, pady=6)
leftbutton3 = Radiobutton(ws, font=font, text="Yes", variable=var3, value=1, command=clicked).grid(row=2, column=6)
rightbutton3 = Radiobutton(ws, font=font, text="No", variable=var3, value=2, command=clicked).grid(row=2, column=7)

var4 = IntVar()
label4  = Label(ws, font=font, text = "**MRD tp#1b/w8 ≥ 1x 10-3").grid(row=3, column=0, columnspan=5, sticky=W, padx=6, pady=6)
leftbutton4 = Radiobutton(ws, font=font, text="Yes", variable=var4, value=1, command=clicked).grid(row=3, column=6)
rightbutton4 = Radiobutton(ws, font=font, text="No", variable=var4, value=2, command=clicked).grid(row=3, column=7)

var5 = IntVar()
label5  = Label(ws, font=font, text = "**MRD at time point #2/w12 ≥ 1x 10-4").grid(row=4, column=0, columnspan=5, sticky=W, padx=6, pady=6)
leftbutton5 = Radiobutton(ws, font=font, text="Yes", variable=var5, value=1, command=clicked).grid(row=4, column=6)
rightbutton5 = Radiobutton(ws, font=font, text="No", variable=var5, value=2, command=clicked).grid(row=4, column=7)

var6 = IntVar()
label6  = Label(ws, font=font, text = "**Bilateral testicular ALL").grid(row=5, column=0, columnspan=5, sticky=W, padx=6, pady=6)
leftbutton6 = Radiobutton(ws, font=font, text="Yes", variable=var6, value=1, command=clicked).grid(row=5, column=6)
rightbutton6 = Radiobutton(ws, font=font, text="No", variable=var6, value=2, command=clicked).grid(row=5, column=7)

var7 = IntVar()
label7  = Label(ws, font=font, text = "**CNS+ beyond first 4 doses of IT MTX").grid(row=6, column=0, columnspan=5, sticky=W, padx=6, pady=6)
leftbutton7 = Radiobutton(ws, font=font, text="Yes", variable=var7, value=1, command=clicked).grid(row=6, column=6)
rightbutton7 = Radiobutton(ws, font=font, text="No", variable=var7, value=2, command=clicked).grid(row=6, column=7)

highArray = [var1, var2, var3, var4, var5, var6, var7]

row = 7
separator = ttk.Separator(ws, orient="horizontal")
separator.grid(row=7,column =0, columnspan=100, sticky="ew")

row = row + 1
var8 = IntVar()
label8  = Label(ws, font=font, text = "NCI HR (age younger than 1 year OR ≥ 10 years; or WBC ≥50,000/uL)").grid(row=row, column=0, columnspan=5, sticky=W, padx=6, pady=6)
leftbutton8 = Radiobutton(ws, font=font, text="Yes", variable=var8, value=1, command=clicked).grid(row=row, column=6)
rightbutton8 = Radiobutton(ws, font=font, text="No", variable=var8, value=2, command=clicked).grid(row=row, column=7)

row = row + 1
var9 = IntVar()
label9  = Label(ws, font=font, text = "*Ikaros deletion in the absence of any HR criteria").grid(row=row, column=0, columnspan=5, sticky=W, padx=6, pady=6)
leftbutton9 = Radiobutton(ws, font=font, text="Yes", variable=var9, value=1, command=clicked).grid(row=row, column=6)
rightbutton9 = Radiobutton(ws, font=font, text="No", variable=var9, value=2, command=clicked).grid(row=row, column=7)

row = row + 1
var10 = IntVar()
label10  = Label(ws, font=font, text = "MRD tp #1 ≥1x10-4 to <1x10-2 & MRD tp#1b < 1x10-3 & MRD tp#2 negative").grid(row=row, column=0, columnspan=5, sticky=W, padx=6, pady=6)
leftbutton10 = Radiobutton(ws, font=font, text="Yes", variable=var10, value=1, command=clicked).grid(row=row, column=6)
rightbutton10 = Radiobutton(ws, font=font, text="No", variable=var10, value=2, command=clicked).grid(row=row, column=7)

row = row + 1
var11 = IntVar()
label11  = Label(ws, font=font, text = "CNS2, CNS2-TT with blast, CNS3").grid(row=row, column=0, columnspan=5, sticky=W, padx=6, pady=6)
leftbutton11 = Radiobutton(ws, font=font, text="Yes", variable=var11, value=1, command=clicked).grid(row=row, column=6)
rightbutton11 = Radiobutton(ws, font=font, text="No", variable=var11, value=2, command=clicked).grid(row=row, column=7)

row = row + 1
var12 = IntVar()
label12  = Label(ws, font=font, text = "Unilateral testicular ALL").grid(row=row, column=0, columnspan=5, sticky=W, padx=6, pady=6)
leftbutton12 = Radiobutton(ws, font=font, text="Yes", variable=var12, value=1, command=clicked).grid(row=row, column=6)
rightbutton12 = Radiobutton(ws, font=font, text="No", variable=var12, value=2, command=clicked).grid(row=row, column=7)

row = row + 1
var13 = IntVar()
label13  = Label(ws, font=font, text = "No sensitive PCR or flow MRD markerc").grid(row=row, column=0, columnspan=5, sticky=W, padx=6, pady=6)
leftbutton13 = Radiobutton(ws, font=font, text="Yes", variable=var13, value=1, command=clicked).grid(row=row, column=6)
rightbutton13 = Radiobutton(ws, font=font, text="No", variable=var13, value=2, command=clicked).grid(row=row, column=7)


intermediateArray = [var8, var9, var10, var11, var12, var13]

row = row + 1
separator = ttk.Separator(ws, orient="horizontal")
separator.grid (row=row,column =0, columnspan=100, sticky="ew")

row = row + 1
var14 = IntVar()
label14  = Label(ws, font=font, text = "NCI standard risk (Age between 1 - < 10 years and WBC < 50,000/uL)").grid(row=row, column=0, columnspan=5, sticky=W, padx=6, pady=6)
leftbutton14 = Radiobutton(ws, font=font, text="Yes", variable=var14, value=1, command=clicked).grid(row=row, column=6)
rightbutton14 = Radiobutton(ws, font=font, text="No", variable=var14, value=2, command=clicked).grid(row=row, column=7)

row = row + 1
var15 = IntVar()
label15  = Label(ws, font=font, text = "CNS 1, CNS 2-TT without blast (Traumatic tap without blasts can be in SR)").grid(row=row, column=0, columnspan=5, sticky=W, padx=6, pady=6)
leftbutton15 = Radiobutton(ws, font=font, text="Yes", variable=var15, value=1, command=clicked).grid(row=row, column=6)
rightbutton15 = Radiobutton(ws, font=font, text="No", variable=var15, value=2, command=clicked).grid(row=row, column=7)

row = row + 1
var16 = IntVar()
label16  = Label(ws, font=font, text = "No testicular ALL").grid(row=row, column=0, columnspan=5, sticky=W, padx=6, pady=6)
leftbutton16 = Radiobutton(ws, font=font, text="Yes", variable=var16, value=1, command=clicked).grid(row=row, column=6)
rightbutton16 = Radiobutton(ws, font=font, text="No", variable=var16, value=2, command=clicked).grid(row=row, column=7)

row = row + 1
var17 = IntVar()
label17  = Label(ws, font=font, text = "No high risk criteria").grid(row=row, column=0, columnspan=5, sticky=W, padx=6, pady=6)
leftbutton17 = Radiobutton(ws, font=font, text="Yes", variable=var17, value=1, command=clicked).grid(row=row, column=6)
rightbutton17 = Radiobutton(ws, font=font, text="No", variable=var17, value=2, command=clicked).grid(row=row, column=7)

row = row + 1
var18 = IntVar()
label18  = Label(ws, font=font, text = "MRD tp#1 ≤1x 10-4 and tp#1b negative a").grid(row=row, column=0, columnspan=5, sticky=W, padx=6, pady=6)
leftbutton18 = Radiobutton(ws, font=font, text="Yes", variable=var18, value=1, command=clicked).grid(row=row, column=6)
rightbutton18 = Radiobutton(ws, font=font, text="No", variable=var18, value=2, command=clicked).grid(row=row, column=7)


standardArray = [var14, var15, var16, var17, var18]






#separator = ttk.Separator(ws, orient=HORIZONTAL).grid (row=13,column =0, columnspan=5, sticky="ew")

#ttk.Separator(ws).place(x=0, y=26, relwidth=1)

def close_window():
    root.quit()


def show_popup(message):
    pop_up = tk.Toplevel(root)
    pop_up.withdraw()
    pop_up.title("Risk Stratification")
    width = 600
    height = 400
    screen_width = pop_up.winfo_screenwidth()
    screen_height = pop_up.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    pop_up.geometry("%dx%d" % (width, height))
    pop_up.deiconify()
    label = tk.Label(pop_up, text=message, font=("Arial", 18))
    label.place(relx=0.5, rely=0.5, anchor=CENTER)
    close_button = tk.Button(pop_up, text="Close", command=pop_up.destroy)
    close_button.pack(side="bottom", padx=10, pady=10)

    pop_up.wm_transient(root)

root = ws
root.protocol("WM_DELETE_WINDOW", close_window)


ws.mainloop()
