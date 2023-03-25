from tkinter import *
import tkinter as tk
import os.path
from os import path
import json


masalar = {}
buttons = {}
kolonlar = {}
dosya = "masalar.json"
isim_entry = object
tel_entry = object

class Restorant(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.initUI(parent)
    


    def initUI(self, parent):
        global masalar, isim_entry, tel_entry
        
        
        self.parent = parent
        self.baslık= Label(self, text='Restoran Rezervasyon Sistemi', font="Normal 20", fg="white", bg="darkorange",width=72, height=1)
        self.baslık.pack(pady=10)
        self.pack()
        self.baslıkalan = Frame(self)
        self.baslıkalan.pack(fill=X, pady=3)
        self.masa = Label(self.baslıkalan, text="Masa: ")
        self.masa.pack(side=LEFT)
        self.masa_secimi = Label(self.baslıkalan, text="[Seçilmedi]")
        self.masa_secimi.pack(side=LEFT)
        self.musteri_ismi = Label(self.baslıkalan, text="Müşterinin İsmi:")
        self.musteri_ismi.pack(side=LEFT, padx=15)
        self.isim_giris = Entry(self.baslıkalan, textvariable=isim_entry)
        self.isim_giris.pack(side=LEFT)
        self.musteri_telefon = Label(self.baslıkalan, text="Müşterinin Telefon Numarası:")
        self.musteri_telefon.pack(side=LEFT,padx=15)
        self.musteri_telefon_giris = Entry(self.baslıkalan, textvariable=tel_entry)
        self.musteri_telefon_giris.pack(side=LEFT)
        self.kaydet = Button(self.baslıkalan, text="Reservasyonu Kaydet/Güncelle",bg="white", command = self.reserve )
        self.kaydet.pack(side=LEFT, padx=10)


        
        
        self.sil = Button(self.baslıkalan, text="Reservasyonu Sil",bg ="white", command = self.silme)
        self.sil.pack(side=LEFT, padx=15)
        # cerceve için frame
        self.cerceve=Frame(self, highlightbackground="black", highlightcolor="black", highlightthickness=2, bd= 0)
        self.cerceve.pack( pady= 20,side=LEFT, padx= 10)
         
        # kolon için frame
        for i in range(3):
            kolonlar[i] = Frame(self.cerceve,)
            kolonlar[i].pack( pady=15)
    
        # buttonlar
        j = 0

       
        for i in range(15):
            if i % 5 == 0:
                j = j + 1
            bcolor = "green"
            fcolor = "white"
            if masalar[str(i)]['mismi'] != '':
                bcolor = "red"
                fcolor = "black"
           
                
            buttons[i] = Button(kolonlar[j-1],text="Masa " + str(i+1), height=5, width=15, activebackground="red",
                                bg=bcolor,
                                fg=fcolor, activeforeground="white", command=lambda n = i+1 : self.editT(n))
            buttons[i].pack(side=LEFT,fill=X,padx=7)


        


        
        
        self.pack()

    def editT(self,n):
        global masalar, buttons,isim_entry,tel_entry
        self.masa_secimi.config(text=n)
        isim_entry.set(masalar[str(n-1)]['mismi'])
        tel_entry.set(masalar[str(n-1)]['tel'])
        

    def reserve(self):
        global masalar, buttons,isim_entry,tel_entry
        n = self.masa_secimi.cget("text")

        
        if isim_entry.get() == '' or tel_entry.get() == '':
            self.labellar = Label(self.baslıkalan, text="Eksik Bilgi" ,bg="orange", fg="white")
            self.labellar.after(2000, self.labellar.destroy)
            self.labellar.pack(side=LEFT)

        elif tel_entry.get().isdecimal() == FALSE:
            self.labellar = Label(self.baslıkalan, text="Tel.Num Yalnızca Rakam İçerebilir" ,bg="orange", fg="white")
            self.labellar.after(2000, self.labellar.destroy)
            self.labellar.pack(side=LEFT)

        else:
            self.labellar = Label(self.baslıkalan, text="Kaydedildi" ,bg="green", fg="white")
            self.labellar.after(2000, self.labellar.destroy)
            self.labellar.pack(side=LEFT)
            masalar[str(n-1)]['mismi'] = isim_entry.get()
            masalar[str(n-1)]['tel'] = tel_entry.get()
            self.kayıt()

    def kayıt(self):
        global masalar
        with open(dosya, 'w', encoding='utf-8') as f:
            json.dump(masalar, f, ensure_ascii=False, indent=4)
        self.yenilenme()

    def silme(self):
        global masalar,buttons,isim_entry,tel_entry
        n = self.masa_secimi.cget("text")
        if isim_entry.get() == '' or tel_entry.get() == '':
            self.labellar = Label(self.baslıkalan, text="Eksik Bilgi", bg="orange", fg="white")
            self.labellar.after(2000, self.labellar.destroy)
            self.labellar.pack(side=LEFT)
        else:
             self.labellar = Label(self.baslıkalan, text="Rezervasyon Silindi", bg="red", fg="white")
             self.labellar.after(2000, self.labellar.destroy)
             self.labellar.pack(side=LEFT)
             masalar[str(n - 1)]['mismi'] = ''
             masalar[str(n - 1)]['tel'] = ''
             isim_entry.set('')
             tel_entry.set('')
             self.kayıt()

    def yenilenme(self):
        global masalar
        for i in range(15):
            bcolor = "green"
            fcolor = "white"
            if masalar[str(i)]['mismi'] != '':
                bcolor = "red"
                fcolor = "black"
            buttons[i].config(bg=bcolor, fg=fcolor)
        
            
        

def main():
    global dosya, masalar, buttons, isim_entry, tel_entry
    
  



    try:
        with open(dosya, "r", encoding='utf-8') as f:
            fdata = f.read()
            masalar = json.loads(fdata)
    except:
        for i in range(15):
            masalar[i] = {"masa":i, "mismi":"", "tel":""}
        with open(dosya, 'w', encoding='utf-8') as f:
            json.dump(masalar, f, ensure_ascii=False, indent=4)
    finally:
        f.close()
          
    pencere = Tk()

    isim_entry = tk.StringVar()
    tel_entry = tk.StringVar()
    
    restorant = Restorant(pencere)
    pencere.title("Restoran Rezervasyon Sistemi")
    pencere.geometry("1250x500")
    pencere.resizable(FALSE, FALSE)

  
    
    pencere.mainloop()
main()
