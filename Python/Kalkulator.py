import tkinter as tk

def okienko():
    root = tk.Tk()

    root.title("Kalkulator")
    root.geometry("460x460")

    return root

def ekran(root):

    ekran = [
        tk.Label(root, bg="#C0CBCB", width=60)
        for i in range(3)
    ]

    for i in range(len(ekran)):
        ekran[i].grid(row=i, columnspan=6, ipady=15, ipadx=1)

    return ekran

if __name__ == "__main__":
    root = okienko()
    root.mainloop()
 