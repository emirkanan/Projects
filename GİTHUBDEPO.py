from tkinter import *
from tkinter import ttk
from tkinter import filedialog as fd
import csv

listkullanici=[]
listdepo=[]
listyildiz=[]

class Depo(Frame):
    
    def __init__(self,parent):
        Frame.__init__(self, parent)
        self.initUI(parent)
    def initUI(self,parent):
        global Depo

        # ------------Tuş Bölgesi------------------------

        self.baslik = Label(self, text='GitHub Depo Önerici', width=100, fg="white", bg='orange',font='Comic 19')
        self.baslik.grid(row=0, column=0, columnspan=11)

        self.bosbas = Label(self, text='', fg="white",width=1,height=2)
        self.bosbas.grid(row=1, column=0, sticky=EW)

        self.KVY = Button(self, text='Kullanıcı Verisi Yükle', width=10, height=2, bg='gainsboro', command=self.kullanicicagir)
        self.KVY.grid(row=1, column=1, pady=20, sticky=EW)

        self.bos1 = Button(self, text='', width=1, height=2, bg='grey37',state='disabled')
        self.bos1.grid(row=1, column=2, columnspan=3, pady=20, sticky=EW)

        self.DVY = Button(self, text='Depo Verisi Yükle', width=10, height=2, bg='gainsboro', command=self.depocagir)
        self.DVY.grid(row=1, column=5, pady=20, sticky=EW)

        self.bos2 = Button(self, text='', width=10, height=2, bg='grey37',state='disabled')
        self.bos2.grid(row=1, column=6, columnspan=3, pady=20, sticky=EW)
#https://stackoverflow.com/questions/16046743/how-to-change-tkinter-button-state-from-disabled-to-normal        

        self.YVY = Button(self, text='Yıldız Verisi Yükle', width=10, height=2, bg='gainsboro', command=self.vericagir)
        self.YVY.grid(row=1, column=9, pady=20, sticky=EW)

        self.bosson = Label(self, text='', fg="white",width=1, height=2)
        self.bosson.grid(row=1, column=10,sticky=EW)

        # -----------------------------------------

        self.depoonerLbl = Label(self, text='Şunun İçin Depo Öner :')
        self.depoonerLbl.grid(row=4, column=1, sticky=EW)

        self.tavsiyeLbl = Label(self, text='Tavsiyeler')
        self.tavsiyeLbl.grid(row=4, column=9, sticky=EW)

        # ------------------------------------------

        self.liste = Listbox(self, height=18, width=15)
        self.liste.grid(row=6, column=1, rowspan=3,sticky=EW)

        self.dilLbl= Label(self, text="Programlama Diline Göre Filtrele")
        self.dilLbl.grid(row=9, column=1, sticky=EW, pady=10)

        self.combo=ttk.Combobox(self, values=["Hepsi","-","C","C++","Dart","Go","HTML","Java", "JavaScript", "Julia"])
        self.combo.current(0)
        self.combo.grid(row=10, column=1)

        self.benzerlikLbl=Label(self, text="Benzerlik Algoritması")
        self.benzerlikLbl.grid(row=11, column=1,pady=10)

        self.check1 = Checkbutton(self, text='Pearson', onvalue=0, offvalue=0)
        self.check1.grid(row=12, column=1)
        #https://www.javatpoint.com/python-tkinter-checkbutton

        self.check2 = Checkbutton(self, text='Öklid', onvalue=0, offvalue=0)
        self.check2.grid(row=13, column=1)

        self.miktarLbl= Label(self, text="Tavsiye Miktarı")
        self.miktarLbl.grid(row=14, column=1, sticky=W)

        self.miktar=Entry(self, width=5)
        self.miktar.grid(row=14, column=1, sticky=E)

        # --------------------------------------------

        self.tavsiyeDepo = Button(self, text='Depo Tavsiye Et', height=2, bg='gainsboro')
        self.tavsiyeDepo.grid(row=7, column=2, sticky=S)

        self.tavsiyeKullanıcı = Button(self, text='GitHub Kullanıcısı Tavsiye Et', height=2, bg='gainsboro')
        self.tavsiyeKullanıcı.grid(row=8, column=2, sticky=N)

        # -------------------------------------------

        self.liste2=Listbox(self, height=27)
        self.liste2.grid(row=6, column=9,rowspan=9, sticky=EW)





        self.grid()
        pass

    def kullanicicagir(self):
        global listkullanici
        self.filename = fd.askopenfilename(initialdir="/İndirilenler", title="Select file", filetypes=(("All Files", "*.*"), ("Text files", "*.txt")))

        with open(self.filename) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                listkullanici.append(row[1].lower())
                #https://stackoverflow.com/questions/17329113/convert-list-to-lower-case
                #https://stackoverflow.com/questions/1801668/convert-a-python-list-with-strings-all-to-lowercase-or-uppercase
        listkullanici.sort()
        #https://www.w3schools.com/python/ref_list_sort.asp
        for kullanici in listkullanici:
            self.liste.insert(END,kullanici)
        # https://realpython.com/python-csv/ , https://www.youtube.com/watch?v=efSjcrp87OY , https://www.youtube.com/watch?v=0Vl0iwkXrQ8.




    def depocagir(self):
         
        global listdepo
        self.filename = fd.askopenfilename(initialdir="/İndirilenler", title="Select file", filetypes=(("All Files", "*.*"), ("Text files", "*.txt")))
        with open(self.filename) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                if row[3] not in listdepo:
                    listdepo.append(row[3])
        listdepo.sort()    

        self.combo['values'] = listdepo
        
        
        


    
             
    def vericagir(self):
        global listyildiz
        self.filename = fd.askopenfilename(initialdir="/İndirilenler", title="Select file", filetypes=(("All Files", "*.*"), ("Text files", "*.txt")))

        with open(self.filename) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter='\t')

            for row in csv_reader:
                listdepo.append(row)
  
def main():
    global pencere
    pencere = Tk()
    depo = Depo(pencere)
    pencere.title("GitHub Depo Önerici")
    pencere.mainloop()

main()
