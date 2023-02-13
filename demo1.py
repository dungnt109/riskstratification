from tkinter import *

root = Tk()
root.title("Parent Window")
root.geometry("600x600")

def open_popup():
    pop = Toplevel(root)
    pop.title("Pop-up Window")
    pop.geometry("200x200")
    x = (root.winfo_screenwidth() - pop.winfo_reqwidth()) / 2
    y = (root.winfo_screenheight() - pop.winfo_reqheight()) / 2
    #pop.geometry("+%d+%d" % (x, y))

    pop.wm_transient(root)

btn = Button(root, text="Open Pop-up", command=open_popup)
btn.pack()

root.mainloop()