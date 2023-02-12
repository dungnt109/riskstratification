from tkinter import *
from tkinter import ttk

ws = Tk()
ws.title("Risk Stratification")
ws.geometry('1000x800')

var1 = IntVar()
label1  = Label(ws, text = "**High risk genetic subtype as defined by RNA-Sequencing d, pathogenic TP53 mutation, \nPAX5-altered (PAX5alt) with ikaros deletion (even if MRD negative tp#1)").grid(row=0, column=0, columnspan=5, sticky=W, padx=6, pady=6)
leftbutton1 = Radiobutton(ws, text="Yes", variable=var1, value=1).grid(row=0, column=6)
rightbutton1 = Radiobutton(ws, text="No", variable=var1, value=2).grid(row=0, column=7)

var2 = IntVar()
label2  = Label(ws, text = "**Infant ALL (< 1 years old) with CD10-ve and/or MLL-r e").grid(row=1, column=0, columnspan=5, sticky=W, padx=6, pady=6)
leftbutton2 = Radiobutton(ws, text="Yes", variable=var2, value=1).grid(row=1, column=6)
rightbutton2 = Radiobutton(ws, text="No", variable=var2, value=2).grid(row=1, column=7)

var3 = IntVar()
label3  = Label(ws, text = "*MRD tp#1/D33≥ 1x 10-2").grid(row=2, column=0, columnspan=5, sticky=W, padx=6, pady=6)
leftbutton3 = Radiobutton(ws, text="Yes", variable=var3, value=1).grid(row=2, column=6)
rightbutton3 = Radiobutton(ws, text="No", variable=var3, value=2).grid(row=2, column=7)

var4 = IntVar()
label4  = Label(ws, text = "**MRD tp#1b/w8 ≥ 1x 10-3").grid(row=3, column=0, columnspan=5, sticky=W, padx=6, pady=6)
leftbutton4 = Radiobutton(ws, text="Yes", variable=var4, value=1).grid(row=3, column=6)
rightbutton4 = Radiobutton(ws, text="No", variable=var4, value=2).grid(row=3, column=7)

var5 = IntVar()
label5  = Label(ws, text = "**MRD at time point #2/w12 ≥ 1x 10-4").grid(row=4, column=0, columnspan=5, sticky=W, padx=6, pady=6)
leftbutton5 = Radiobutton(ws, text="Yes", variable=var5, value=1).grid(row=4, column=6)
rightbutton5 = Radiobutton(ws, text="No", variable=var5, value=2).grid(row=4, column=7)

var6 = IntVar()
label6  = Label(ws, text = "**Bilateral testicular ALL").grid(row=5, column=0, columnspan=5, sticky=W, padx=6, pady=6)
leftbutton6 = Radiobutton(ws, text="Yes", variable=var6, value=1).grid(row=5, column=6)
rightbutton6 = Radiobutton(ws, text="No", variable=var6, value=2).grid(row=5, column=7)

var7 = IntVar()
label7  = Label(ws, text = "**CNS+ beyond first 4 doses of IT MTX").grid(row=6, column=0, columnspan=5, sticky=W, padx=6, pady=6)
leftbutton7 = Radiobutton(ws, text="Yes", variable=var7, value=1).grid(row=6, column=6)
rightbutton7 = Radiobutton(ws, text="No", variable=var7, value=2).grid(row=6, column=7)

row = 7
separator = ttk.Separator(ws, orient="horizontal")
separator.grid(row=7,column =0, columnspan=100, sticky="ew")

row = row + 1
var8 = IntVar()
label8  = Label(ws, text = "NCI HR (age younger than 1 year OR ≥ 10 years; or WBC ≥50,000/uL)").grid(row=row, column=0, columnspan=5, sticky=W, padx=6, pady=6)
leftbutton8 = Radiobutton(ws, text="Yes", variable=var8, value=1).grid(row=row, column=6)
rightbutton8 = Radiobutton(ws, text="No", variable=var8, value=2).grid(row=row, column=7)

row = row + 1
var9 = IntVar()
label9  = Label(ws, text = "*Ikaros deletion in the absence of any HR criteria").grid(row=row, column=0, columnspan=5, sticky=W, padx=6, pady=6)
leftbutton9 = Radiobutton(ws, text="Yes", variable=var9, value=1).grid(row=row, column=6)
rightbutton9 = Radiobutton(ws, text="No", variable=var9, value=2).grid(row=row, column=7)

row = row + 1
var10 = IntVar()
label10  = Label(ws, text = "MRD tp #1 ≥1x10-4 to <1x10-2 & MRD tp#1b < 1x10-3 & MRD tp#2 negative").grid(row=row, column=0, columnspan=5, sticky=W, padx=6, pady=6)
leftbutton10 = Radiobutton(ws, text="Yes", variable=var10, value=1).grid(row=row, column=6)
rightbutton10 = Radiobutton(ws, text="No", variable=var10, value=2).grid(row=row, column=7)

row = row + 1
var11 = IntVar()
label11  = Label(ws, text = "CNS2, CNS2-TT with blast, CNS3").grid(row=row, column=0, columnspan=5, sticky=W, padx=6, pady=6)
leftbutton11 = Radiobutton(ws, text="Yes", variable=var11, value=1).grid(row=row, column=6)
rightbutton11 = Radiobutton(ws, text="No", variable=var11, value=2).grid(row=row, column=7)

row = row + 1
var12 = IntVar()
label12  = Label(ws, text = "Unilateral testicular ALL").grid(row=row, column=0, columnspan=5, sticky=W, padx=6, pady=6)
leftbutton12 = Radiobutton(ws, text="Yes", variable=var12, value=1).grid(row=row, column=6)
rightbutton12 = Radiobutton(ws, text="No", variable=var12, value=2).grid(row=row, column=7)

row = row + 1
var13 = IntVar()
label13  = Label(ws, text = "No sensitive PCR or flow MRD markerc").grid(row=row, column=0, columnspan=5, sticky=W, padx=6, pady=6)
leftbutton13 = Radiobutton(ws, text="Yes", variable=var13, value=1).grid(row=row, column=6)
rightbutton13 = Radiobutton(ws, text="No", variable=var13, value=2).grid(row=row, column=7)


separator = ttk.Separator(ws, orient="horizontal")
separator.grid (row=13,column =0, columnspan=100, sticky="ew")

row=14 
var14 = IntVar()
label14  = Label(ws, text = "NCI standard risk (Age between 1 - < 10 years and WBC < 50,000/uL)").grid(row=row, column=0, columnspan=5, sticky=W, padx=6, pady=6)
leftbutton14 = Radiobutton(ws, text="Yes", variable=var14, value=1).grid(row=row, column=6)
rightbutton14 = Radiobutton(ws, text="No", variable=var14, value=2).grid(row=row, column=7)

row = row + 1
var15 = IntVar()
label15  = Label(ws, text = "CNS 1, CNS 2-TT without blast (Traumatic tap without blasts can be in SR)").grid(row=row, column=0, columnspan=5, sticky=W, padx=6, pady=6)
leftbutton15 = Radiobutton(ws, text="Yes", variable=var15, value=1).grid(row=row, column=6)
rightbutton15 = Radiobutton(ws, text="No", variable=var15, value=2).grid(row=row, column=7)

row = row + 1
var16 = IntVar()
label16  = Label(ws, text = "No testicular ALL").grid(row=row, column=0, columnspan=5, sticky=W, padx=6, pady=6)
leftbutton16 = Radiobutton(ws, text="Yes", variable=var16, value=1).grid(row=row, column=6)
rightbutton16 = Radiobutton(ws, text="No", variable=var16, value=2).grid(row=row, column=7)

row = row + 1
var17 = IntVar()
label17  = Label(ws, text = "No high risk criteria").grid(row=row, column=0, columnspan=5, sticky=W, padx=6, pady=6)
leftbutton17 = Radiobutton(ws, text="Yes", variable=var17, value=1).grid(row=row, column=6)
rightbutton17 = Radiobutton(ws, text="No", variable=var17, value=2).grid(row=row, column=7)

row = row + 1
var18 = IntVar()
label18  = Label(ws, text = "MRD tp#1 ≤1x 10-4 and tp#1b negative a").grid(row=row, column=0, columnspan=5, sticky=W, padx=6, pady=6)
leftbutton18 = Radiobutton(ws, text="Yes", variable=var18, value=1).grid(row=row, column=6)
rightbutton18 = Radiobutton(ws, text="No", variable=var18, value=2).grid(row=row, column=7)

row = row + 1
var19 = IntVar()
label19  = Label(ws, text = "text19").grid(row=row, column=0, columnspan=5, sticky=W, padx=6, pady=6)
leftbutton19 = Radiobutton(ws, text="Yes", variable=var19, value=1).grid(row=row, column=6)
rightbutton19 = Radiobutton(ws, text="No", variable=var19, value=2).grid(row=row, column=7)

row = row + 1
var20 = IntVar()
label20  = Label(ws, text = "text20").grid(row=row, column=0, columnspan=5, sticky=W, padx=6, pady=6)
leftbutton20 = Radiobutton(ws, text="Yes", variable=var20, value=1).grid(row=row, column=6)
rightbutton20 = Radiobutton(ws, text="No", variable=var20, value=2).grid(row=row, column=7)

row = row + 1
var21 = IntVar()
label21  = Label(ws, text = "text21").grid(row=row, column=0, columnspan=5, sticky=W, padx=6, pady=6)
leftbutton21 = Radiobutton(ws, text="Yes", variable=var21, value=1).grid(row=row, column=6)
rightbutton21 = Radiobutton(ws, text="No", variable=var21, value=2).grid(row=row, column=7)

row = row + 1
var22 = IntVar()
label22  = Label(ws, text = "text22").grid(row=row, column=0, columnspan=5, sticky=W, padx=6, pady=6)
leftbutton22 = Radiobutton(ws, text="Yes", variable=var22, value=1).grid(row=row, column=6)
rightbutton22 = Radiobutton(ws, text="No", variable=var22, value=2).grid(row=row, column=7)

row = row + 1
var23 = IntVar()
label23  = Label(ws, text = "text23").grid(row=row, column=0, columnspan=5, sticky=W, padx=6, pady=6)
leftbutton23 = Radiobutton(ws, text="Yes", variable=var23, value=1).grid(row=row, column=6)
rightbutton23 = Radiobutton(ws, text="No", variable=var23, value=2).grid(row=row, column=7)

row = row + 1
var24 = IntVar()
label24  = Label(ws, text = "text24").grid(row=row, column=0, columnspan=5, sticky=W, padx=6, pady=6)
leftbutton24 = Radiobutton(ws, text="Yes", variable=var24, value=1).grid(row=row, column=6)
rightbutton24 = Radiobutton(ws, text="No", variable=var24, value=2).grid(row=row, column=7)

row = row + 1
var25 = IntVar()
label25  = Label(ws, text = "text25").grid(row=row, column=0, columnspan=5, sticky=W, padx=6, pady=6)
leftbutton25 = Radiobutton(ws, text="Yes", variable=var25, value=1).grid(row=row, column=6)
rightbutton25 = Radiobutton(ws, text="No", variable=var25, value=2).grid(row=row, column=7)

row = row + 1
var26 = IntVar()
label26  = Label(ws, text = "text26").grid(row=row, column=0, columnspan=5, sticky=W, padx=6, pady=6)
leftbutton26 = Radiobutton(ws, text="Yes", variable=var26, value=1).grid(row=row, column=6)
rightbutton26 = Radiobutton(ws, text="No", variable=var26, value=2).grid(row=row, column=7)

row = row + 1
var27 = IntVar()
label27  = Label(ws, text = "text27").grid(row=row, column=0, columnspan=5, sticky=W, padx=6, pady=6)
leftbutton27 = Radiobutton(ws, text="Yes", variable=var27, value=1).grid(row=row, column=6)
rightbutton27 = Radiobutton(ws, text="No", variable=var27, value=2).grid(row=row, column=7)



#separator = ttk.Separator(ws, orient=HORIZONTAL).grid (row=13,column =0, columnspan=5, sticky="ew")

#ttk.Separator(ws).place(x=0, y=26, relwidth=1)

def close_window():
    root.quit()

root = ws
root.protocol("WM_DELETE_WINDOW", close_window)


ws.mainloop()
