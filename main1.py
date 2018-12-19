# -*- coding: ISO-8859-2 -*-
import matplotlib.pyplot as plt
import tkinter.ttk
from tkinter import *
from tkinter import messagebox

# Punkty od 0-5
#1 Inteligencja werbalna (lingwistyczna, językowa)
#2 Inteligencja matematyczno-logiczna
#3 Inteligencja wizualno-przestrzenna
#4 Inteligencja muzyczna (słuchowa, rytmiczna)
#5 Inteligencja ruchowa
#6 Inteligencja interpersonalna (społeczna)
#7 Inteligencja intrapersonalna (intuicyjna)
#8 Inteligencja przyrodnicza (środowiskowa)



def zbiory():
    try:
        
        lingwistyczna = [int(p5_input.get()) + int(p9_input.get())+ int(p19_input.get()) + int(p20_input.get())]    
        matematyczna = [int(p6_input.get()) + int(p11_input.get())+ int(p22_input.get()) + int(p28_input.get())]   
        wizualno = [int(p2_input.get()) + int(p12_input.get())+ int(p18_input.get()) + int(p24_input.get())]   
        muzyczna=[int(p4_input.get()) + int(p10_input.get())+ int(p17_input.get()) + int(p27_input.get())]   
        interpersonalna=[int(p3_input.get()) + int(p8_input.get())+ int(p13_input.get()) + int(p23_input.get())]   
        intrapersonalna=[int(p7_input.get()) + int(p15_input.get())+ int(p16_input.get()) + int(p26_input.get())]   
        kinestetyczna=[int(p1_input.get()) + int(p14_input.get())+ int(p21_input.get()) + int(p25_input.get())]
        #print('lingwistyczna' , lingwistyczna)
        #print('matematyczna' , matematyczna)
        #print('wizualno-przestrzenna' , wizualno)
        #print('muzyczna' , muzyczna)
        #print('interpersonalna' , interpersonalna)
        #print('intrapersonalna' , intrapersonalna)
        #print('kinestetyczna' , kinestetyczna)
        imie = imie_input.get()
        nazwisko = nazwisko_input.get()
        labels = 'Lingwistyczna', 'Matematyczno-logiczna', 'Wizualno-przestrzenna', 'Muzyczna','Interpersonalna','Intrapersonalna','Kinestetyczna'
        sizes = []
        sizes.extend([lingwistyczna,matematyczna,wizualno,muzyczna,interpersonalna,intrapersonalna,kinestetyczna])
        #print('sizes', sizes)    
        sizes2 = sorted(sizes)
        #print('sortet', sizes2)
        # explode = (0, 0, 0, 0,0,0,0.1)
        explode = (0, 0, 0, 0,0,0,0)
            
        fig1, ax1 = plt.subplots()
        fig1.suptitle('Graficzny rozkład typów inteligencji zgodnie z teorią Howarda Gardnera\n %s %s '%(imie, nazwisko), fontsize=12)     
        ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',startangle=90)
        ax1.axis('equal')   
        plt.show()
        
        
        
    except: print('blad')
        
        
def rysuj_wykres():
    labels = 'Lingwistyczna', 'Matematyczna', 'Wizualno-przestrzenna', 'Muzyczna','Interpersonalna','Intrapersonalna','Kinestetyczna'
    sizes = []
    sizes.extend([lingwistyczna,matematyczna,wizualno,muzyczna,interpersonalna,intrapersonalna,kinestetyczna])
    print('sizes', sizes)    
    sizes2 = sorted(sizes)
    print('sortet', sizes2)
    explode = (0, 0, 0, 0,0,0,0.1)
        
    fig1, ax1 = plt.subplots()
    fig1.suptitle('Graficzny rozkład typów inteligencji\n imię i nazwisko:', fontsize=12)        
    ax1.pie(sizes2, explode=explode, labels=labels, autopct='%1.1f%%',startangle=90)
    ax1.axis('equal')        
    plt.show()    

def close():
    result = messagebox.askyesno("Wyjście", "Zakończyć program?")
    if result == TRUE:
        root.destroy()     
    
def info():
    messagebox.showinfo('O programie','    Autor: Michał\n misial_82@interia.pl\n      --- 2019 ---')
def wyniki():
    root2 = Tk()
    root2.title('Interpretacja wyników testu')
    # 'Lingwistyczna', 'Matematyczna', 'Wizualno-przestrzenna', 'Muzyczna','Interpersonalna','Intrapersonalna','Kinestetyczna'
    
    info = Label(root2, text = 'TYP INTELIGENCJI  -  PRZYKŁADOWY KIERUNEK ROZWOJU\nlogiczno-matematyczna : matematyk, bankowiec, fizyk, chemik, lekarz, inżynier\ninterpersonalna : psychoterapeuta, nauczyciel, menadżer, lekarz, pielęgniarka\nmuzyczna : kompozytor, piosenkarz, aktor\nlingwistyczna : pisarz, dziennikarz, publicysta, prawnik, nauczyciel, tłumacz\nwizualno-przestrzenna : malarz, architekt, rzeźbiarz, pilot, przewodnik, projektant mody, chirurg, mechanik\nintrapersonalna : filozof, psychoterapeuta, teolog, powieściopisarz\nkinestetyczna : sportowiec, tancerz, choreograf, kierowca, wynalazca')
    info.grid(row=0,column=0)
    root.mainloop()
    
    
    
root = Tk()
root.title('Kwestionariusz wielorakiej inteligencji')
# MENU
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Informacje o wynikach",command=wyniki)
filemenu.add_command(label="O programie",command=info)
filemenu.add_command(label="Zakończ",command=close)
menubar.add_cascade(label="MENU", menu=filemenu)
root.config(menu=menubar)


# ------------------------ INT VAR -------------------
p1_input = IntVar()
p2_input = IntVar()
p3_input = IntVar()
p4_input = IntVar()
p5_input = IntVar()
p6_input = IntVar()
p7_input = IntVar()
p8_input = IntVar()
p9_input = IntVar()
p10_input = IntVar()
p11_input = IntVar()
p12_input = IntVar()
p13_input = IntVar()
p14_input = IntVar()
p15_input = IntVar()
p16_input = IntVar()
p17_input = IntVar()
p18_input = IntVar()
p19_input = IntVar()
p20_input = IntVar()
p21_input = IntVar()
p22_input = IntVar()
p23_input = IntVar()
p24_input = IntVar()
p25_input = IntVar()
p26_input = IntVar()
p27_input = IntVar()
p28_input = IntVar()
imie_input = StringVar()
nazwisko_input = StringVar()
# ------------------------ RAMKA 1 -----------------------
ramka1 = LabelFrame(root, text='Użyj cyfr od 0 do 5 aby określić stopień prawdziwości poszczególnych stwierdzeń',font=("Arial", 9,'bold'))
ramka1.grid(row=0, column=0,sticky=W)

p1 = Label(ramka1, text = '1. Posiadam uzdolnienia manualne')
p1.grid(row=0, column=0,sticky=W)
p2 = Label(ramka1, text = '2. Posiadam dobre wyczucie kierunku')
p2.grid(row=1, column=0,sticky=W)
p3 = Label(ramka1, text = '3. Posiadam naturalną umiejętność rozwiązywania sporów między przyjaciółmi')
p3.grid(row=2, column=0,sticky=W)
p4 = Label(ramka1, text = '4. Łatwo zapamiętuję słowa piosenek')
p4.grid(row=3, column=0,sticky=W)
p5 = Label(ramka1, text = '5. Potrafię wyjaśniać w prosty sposób trudne zagadnienia')
p5.grid(row=4, column=0,sticky=W)
p6 = Label(ramka1, text = '6. Robię wszystko krok po kroku')
p6.grid(row=5, column=0,sticky=W)
p7 = Label(ramka1, text = '7. Dobrze znam samego siebie i rozumiem, dlaczego postępuję tak, a nie inaczej')
p7.grid(row=6, column=0,sticky=W)
p8 = Label(ramka1, text = '8. Lubię czwiczenia grupowe i spotkania towarzyskie')
p8.grid(row=7, column=0,sticky=W)
p9 = Label(ramka1, text = '9. Dobrze uczę się, słuchając wykładów i wywodów innych ludzi')
p9.grid(row=8, column=0,sticky=W)
p10 = Label(ramka1, text = '10. Słuchając muzyki, doznaję zmian nastroju')
p10.grid(row=9, column=0,sticky=W)
p11 = Label(ramka1, text = '11. Lubię krzyżówki, łamigłówki i problemy logiczne')
p11.grid(row=10, column=0,sticky=W)
p12 = Label(ramka1, text = '12. Tablice, zestawienia i pomoce wizualne odgrywają dla mnie ważną rolę podczas uczenia się')
p12.grid(row=11, column=0,sticky=W)
p13 = Label(ramka1, text = '13. Jestem wrażliwy na nastroje i uczucia otaczających mnie ludzi')
p13.grid(row=12, column=0,sticky=W)
p14 = Label(ramka1, text = '14. Najlepiej uczę się, kiedy muszę wziąć się w garść i zrobić coś samemu')
p14.grid(row=13, column=0,sticky=W)
p15 = Label(ramka1, text = '15. Zanim zechcę się czegoś nauczyć, muszę zobaczyć, jaką będę miał z tego korzyść')
p15.grid(row=14, column=0,sticky=W)
p16 = Label(ramka1, text = '16. Podczas nauki i rozmyślań lubię spokój i samotność')
p16.grid(row=15, column=0,sticky=W)
p17 = Label(ramka1, text = '17. Potrafię usłyszeć poszczególne instrumenty w złożonych utworach muzycznych')
p17.grid(row=16, column=0,sticky=W)
p18 = Label(ramka1, text = '18. Łatwo przychodzi mi wywołanie w wyobraźni zapamiętanych i wymyślonych obrazów')
p18.grid(row=17, column=0,sticky=W)
p19 = Label(ramka1, text = '19. Posiadam bogaty język i potrafię się nim posługiwać')
p19.grid(row=18, column=0,sticky=W)
p20 = Label(ramka1, text = '20. Lubię robić notatki')
p20.grid(row=19, column=0,sticky=W)
p21 = Label(ramka1, text = '21. Posiadam dobre poczucie równowagi i lubię ruch fizyczny')
p21.grid(row=20, column=0,sticky=W)
p22 = Label(ramka1, text = '22. Potrafię dostrzegać strukturę przedmiotów i związki między różnymi rzeczami')
p22.grid(row=21, column=0,sticky=W)
p23 = Label(ramka1, text = '23. Potrafię pracować w zespole i korzystać z cudzych doświadczeń')
p23.grid(row=22, column=0,sticky=W)
p24 = Label(ramka1, text = '24. Jestem dobrym obserwatorem i często zauważam rzeczy uchodzące uwadze innych')
p24.grid(row=23, column=0,sticky=W)
p25 = Label(ramka1, text = '25. Często bywam niespokojny')
p25.grid(row=24, column=0,sticky=W)
p26 = Label(ramka1, text = '26. Lubię pracować lub uczyć się niezależnie od innych')
p26.grid(row=25, column=0,sticky=W)
p27 = Label(ramka1, text = '27. Lubię komponować muzykę')
p27.grid(row=26, column=0,sticky=W)
p28 = Label(ramka1, text = '28. Potrafię radzić sobie z liczbami i problemami matematycznymi')
p28.grid(row=27, column=0,sticky=W)
# ------------------------ INPUT`s -----------------------
p1_input = Entry(ramka1,font=("Arial", 10),width=5,textvariable=p1_input)
p1_input.grid(row=0,column=1,pady=2)
p2_input = Entry(ramka1,font=("Arial", 10),width=5,textvariable=p2_input)
p2_input.grid(row=1,column=1)
p3_input = Entry(ramka1,font=("Arial", 10),width=5,textvariable=p3_input)
p3_input.grid(row=2,column=1,pady=2)
p4_input = Entry(ramka1,font=("Arial", 10),width=5,textvariable=p4_input)
p4_input.grid(row=3,column=1,pady=2)
p5_input = Entry(ramka1,font=("Arial", 10),width=5,textvariable=p5_input)
p5_input.grid(row=4,column=1,pady=2)
p6_input = Entry(ramka1,font=("Arial", 10),width=5,textvariable=p6_input)
p6_input.grid(row=5,column=1,pady=2)
p7_input = Entry(ramka1,font=("Arial", 10),width=5,textvariable=p7_input)
p7_input.grid(row=6,column=1,pady=2)
p8_input = Entry(ramka1,font=("Arial", 10),width=5,textvariable=p8_input)
p8_input.grid(row=7,column=1,pady=2)
p9_input = Entry(ramka1,font=("Arial", 10),width=5,textvariable=p9_input)
p9_input.grid(row=8,column=1,pady=2)
p10_input = Entry(ramka1,font=("Arial", 10),width=5,textvariable=p10_input)
p10_input.grid(row=9,column=1,pady=2)
p11_input = Entry(ramka1,font=("Arial", 10),width=5,textvariable=p11_input)
p11_input.grid(row=10,column=1,pady=2)
p12_input = Entry(ramka1,font=("Arial", 10),width=5,textvariable=p12_input)
p12_input.grid(row=11,column=1,pady=2)
p13_input = Entry(ramka1,font=("Arial", 10),width=5,textvariable=p13_input)
p13_input.grid(row=12,column=1,pady=2)
p14_input = Entry(ramka1,font=("Arial", 10),width=5,textvariable=p14_input)
p14_input.grid(row=13,column=1,pady=2)
p15_input = Entry(ramka1,font=("Arial", 10),width=5,textvariable=p15_input)
p15_input.grid(row=14,column=1,pady=2)
p16_input = Entry(ramka1,font=("Arial", 10),width=5,textvariable=p16_input)
p16_input.grid(row=15,column=1,pady=2)
p17_input = Entry(ramka1,font=("Arial", 10),width=5,textvariable=p17_input)
p17_input.grid(row=16,column=1,pady=2)
p18_input = Entry(ramka1,font=("Arial", 10),width=5,textvariable=p18_input)
p18_input.grid(row=17,column=1,pady=2)
p19_input = Entry(ramka1,font=("Arial", 10),width=5,textvariable=p19_input)
p19_input.grid(row=18,column=1,pady=2)
p20_input = Entry(ramka1,font=("Arial", 10),width=5,textvariable=p20_input)
p20_input.grid(row=19,column=1,pady=2)
p21_input = Entry(ramka1,font=("Arial", 10),width=5,textvariable=p21_input)
p21_input.grid(row=20,column=1,pady=2)
p22_input = Entry(ramka1,font=("Arial", 10),width=5,textvariable=p22_input)
p22_input.grid(row=21,column=1,pady=2)
p23_input = Entry(ramka1,font=("Arial", 10),width=5,textvariable=p23_input)
p23_input.grid(row=22,column=1,pady=2)
p24_input = Entry(ramka1,font=("Arial", 10),width=5,textvariable=p24_input)
p24_input.grid(row=23,column=1,pady=2)
p25_input = Entry(ramka1,font=("Arial", 10),width=5,textvariable=p25_input)
p25_input.grid(row=24,column=1,pady=2)
p26_input = Entry(ramka1,font=("Arial", 10),width=5,textvariable=p26_input)
p26_input.grid(row=25,column=1,pady=2)
p27_input = Entry(ramka1,font=("Arial", 10),width=5,textvariable=p27_input)
p27_input.grid(row=26,column=1,pady=2)
p28_input = Entry(ramka1,font=("Arial", 10),width=5,textvariable=p28_input)
p28_input.grid(row=27,column=1,pady=2)
# ------------------------ RAMKA 2 -----------------------
ramka2 = LabelFrame(root,text='Dane ucznia',font=("Arial", 10,'bold'))
ramka2.grid(column=0,row=1,sticky=W)

imie_label = Label(ramka2,text = 'Imię')
imie_label.grid(column=0,row=0,pady=2,padx=2)
nazwisko_label = Label(ramka2,text='Nazwisko')
nazwisko_label.grid(column=0, row=1)

imie_input = Entry(ramka2,font=("Arial", 10),width=20,textvariable=imie_input)
imie_input.grid(column=1,row=0,pady=2,padx=2)
nazwisko_input = Entry(ramka2,font=("Arial", 10),width=20,textvariable=nazwisko_input)
nazwisko_input.grid(column=1,row=1,pady=2,padx=2)
# ------------------------ BUTTON OK -----------------------
ramka3 = Label(root)
ramka3.grid(column=0,row=1,sticky=E)
button_ok = Button(ramka3,text='Zapisz',font=("Arial", 10,'bold'),width=25,bg='green',command=zbiory)
button_ok.grid(column=0,row=0,sticky=E)


# --------------------- PODZIAŁ NA ZBIORY ---------------------------


root.geometry('505x760')
root.mainloop()
