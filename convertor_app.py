from tkinter import messagebox
import convertor
import tkinter as tk
from tkinter import ttk



class convertor_app(tk.Tk):
    def __init__(self) :
        tk.Tk.__init__(self)
        self.title("Convertor Currency")
        self.geometry("750x500")
        self.resizable(width=0, height=0)
        self.config(background="#49A")
        self.value = tk.IntVar()
        self.entry_value = tk.IntVar(0)
        self.monnaie = tk.StringVar()
        self.monnaie2 = tk.StringVar()
        self.add_monnaie = tk.StringVar()
        self.add_hide_icon = tk.StringVar()
        self.add_hide_icon.set('+')
        self.list_init()
        self.affichage()

    def destroy(self) -> None:
        for cur in self.currency_liste :
            convertor.del_data(cur)
        convertor.saved_back_currency(self.currency_liste)
        return super().destroy()
  

    def list_init(self):
        back_up = convertor.back_up_currency()
        if back_up == [] :
            self.currency_liste = ['EUR','USD']
        else :
            self.currency_liste = back_up
        for cur in self.currency_liste:
            url = convertor.url_currency(cur)
            convertor.save_data(url,cur)

    def affichage(self):
        tk.Label(self,text='Convertir sa monnaie',bg="#49A",fg='white',font=('Arial',35)).pack(fill=tk.X,anchor=tk.N,ipady=20)

        self.frame = tk.Frame(self)
        self.frame.pack(fill=tk.X,ipady=40,pady=50)

        self.frame_center = tk.Frame(self.frame)
        self.frame_center.pack(expand=tk.YES)

        tk.Entry(self.frame_center,width=15,textvariable= self.entry_value,justify=tk.CENTER,font=('Courrier',15)).grid(row=0,column=0,padx=10,pady=5)
        
        self.currency_liste_combo = ttk.Combobox(self.frame_center,state='readonly',textvariable=self.monnaie)
        self.currency_liste_combo['values'] = self.currency_liste
        self.currency_liste_combo.current(0)
        self.currency_liste_combo.grid(row=0,column=1,padx=10,pady=5)

        tk.Label(self.frame_center,textvariable=self.value,width=15,font=('Courrier',15)).grid(row=2,column=0,padx=10,pady=5)

        tk.Button(self.frame_center,textvariable=self.add_hide_icon,font=('Arial',9),width=5,command=lambda : self.display_add()).grid(row=0,column=2,padx=10,pady=5)

        self.currency_liste_combo2 = ttk.Combobox(self.frame_center, state='readonly',textvariable=self.monnaie2,postcommand=self.list_combox2)
        self.currency_liste_combo2.grid(row=2,column=1,padx=10,pady=5)
        self.list_combox2()
        self.currency_liste_combo2.current(0)

        tk.Button(self,text="Convertir",font=('Arial',15),command=lambda : self.convertion()).pack(pady=10)


    def list_combox2(self):
        currency = self.monnaie.get()
        self.currency_liste2 = [value for value in self.currency_liste if value != currency]
        self.currency_liste_combo2['values'] = self.currency_liste2


    def convertion(self):
        devise1 = self.monnaie.get()
        devise2 = self.monnaie2.get()
        if devise1 != devise2 :
            rate = convertor.rate_value(devise1,devise2)
            change = round(int(self.entry_value.get()) * rate,2)
            self.value.set(change)
    
    def display_add(self):
        if self.add_hide_icon.get() == '+':
            self.add_hide_icon.set('-')
            self.info = tk.Label(self.frame_center,text=" Ecrivez votre devise, exemple : XAF, JPY",font=('Arial italic',10))
            self.info.grid(row=1,column=0,padx=10,pady=5)
            self.add_entry = tk.Entry(self.frame_center,width=7,textvariable= self.add_monnaie,justify=tk.CENTER,font=('Courrier',10))
            self.add_entry.grid(row=1,column=1,padx=10,pady=5)
            self.add_button = tk.Button(self.frame_center, text='ajouter',font=('Courrier',10),command=lambda : self.add())
            self.add_button.grid(row=1,column=2,padx=10,pady=5)
        else :
            self.add_hide_icon.set('+')
            self.add_entry.grid_remove()
            self.info.grid_remove()
            self.add_button.grid_remove()
    
    def add(self):
        devise = self.add_monnaie.get().upper()
        if len(devise) == 3 :
            url = convertor.url_currency(devise)
            status = convertor.save_data(url,devise)

            if status == 'ok': 
                self.currency_liste.append(devise)
                self.currency_liste_combo['values'] = self.currency_liste
                self.display_add()
            
            else:
                messagebox.showinfo("devise","veuillez entrer une devise valide sous la forme 'EUR','XAF','USD'")
       


if __name__ == "__main__":
    app = convertor_app()
    app.mainloop()