import tkinter as tk

def show_popup():
    pop_up = tk.Toplevel()
    pop_up.withdraw()
    pop_up.title("Pop-Up Window")
    width = 300
    height = 200
    screen_width = pop_up.winfo_screenwidth()
    screen_height = pop_up.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    pop_up.geometry("%dx%d+%d+%d" % (width, height, x, y))
    pop_up.deiconify()
    label = tk.Label(pop_up, text="This is a pop-up window.")
    label.pack(pady=10)
    close_button = tk.Button(pop_up, text="Close", command=pop_up.destroy)
    close_button.pack()

root = tk.Tk()
root.title("Main Window")
show_button = tk.Button(root, text="Show Pop-Up", command=show_popup)
show_button.pack(pady=10)
root.mainloop()
