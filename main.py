from tkinter import *
from functools import partial
from tkinter.messagebox import showinfo

class Application():

    def __init__(self):
        self.fenetre = Tk()
        self.calcul = ""
        self.listeOptions = ('aide', 'basique', 'scientifique')

        self.calculP = StringVar()
        self.menuV = StringVar()
        w, h = 4, 5
        self.mat_but = [[0 for x in range(w)] for y in range(h)]
        self.l_lab = [[" ", " ", "C", "AC"], ["0", " ", "=", "+"], [ "1","2","3","-"], ["4","5","6","*"], ["7","8","9","/"]]

        self.frame0 = Frame(self.fenetre)
        self.frame0.pack()
        self.frame1 = Frame(self.fenetre)
        self.frame1.pack()
        self.frame2 = Frame(self.fenetre)
        self.frame2.pack()

        self.create_menu()

        self.create_interface()
        self.label = Label(self.frame2, textvariable=self.calculP)
        self.label.pack()
        self.fenetre.mainloop()

    def handle_button(self,i, j):
        print(i, j)
        if self.l_lab[i][j] == "C":
            if len(self.calcul) == 1:
                self.calcul = ""
            else:
                self.calcul = self.calcul[:1]
        elif self.l_lab[i][j] == "AC":
            self.calcul = ""
        elif self.l_lab[i][j] == "=":
            try:
                res = eval(self.calcul)
                self.calcul = str(res)
            except:
                self.calcul = ""
        elif self.l_lab[i][j] != " ":
            self.calcul+=self.l_lab[i][j]
        self.calculP.set(self.calcul)

    def aide(self):
        showinfo("Aide", "Aide inexistante")
    def create_menu(self):
        self.menu = Menu(self.fenetre)
        self.fenetre.config(menu = self.menu)
        self.menuFichier = Menu(self.menu,tearoff=0)
        self.menu.add_cascade(label="Fichier", menu=self.menuFichier)

        self.menuFichier.add_command(label="aide", command=self.aide)
        self.menuFichier.add_command(label="basique")
        self.menuFichier.add_command(label="scientifique")


    def create_interface(self):
        for i in range(5):
            for j in range(4):
                action = partial(self.handle_button, i, j)
                b = Button(self.frame1, text=self.l_lab[i][j], command=action)
                self.mat_but[i][j] = b
                self.mat_but[i][j].grid(row=i+1, column=j)



Application()