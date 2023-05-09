#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from tkinter import *

window = Tk()
window.title("Kalkulator GUI Dengan Python")
window.geometry('450x300')

# Membuat frame untuk input nilai
input_frame = Frame(window)
input_frame.pack(pady=10)

lbl = Label(input_frame, text="Masukkan Nilai Pertama:", anchor="e", width=20, font=("Arial", 12))
lbl.grid(column=0, row=0, padx=5, pady=5)

nilai1 = Entry(input_frame, width=20, font=("Arial", 12))
nilai1.grid(column=1, row=0, padx=5, pady=5)

lbl2 = Label(input_frame, text="Masukkan Nilai Kedua:", anchor="e", width=20, font=("Arial", 12))
lbl2.grid(column=0, row=1, padx=5, pady=5)

nilai2 = Entry(input_frame, width=20, font=("Arial", 12))
nilai2.grid(column=1, row=1, padx=5, pady=5)

# Membuat frame untuk output hasil
output_frame = Frame(window)
output_frame.pack(pady=10)

lbl3 = Label(output_frame, text="Hasil:", anchor="e", width=20, font=("Arial", 12))
lbl3.grid(column=0, row=0, padx=5, pady=5)

hasil = Label(output_frame, width=20, font=("Arial", 12))
hasil.grid(column=1, row=0, padx=5, pady=5)

#rumus
def tambah():
    hasil.configure(text=(float(nilai1.get())+float(nilai2.get())))
def kurang():
    hasil.configure(text=(float(nilai1.get())-float(nilai2.get())))
def kali():
    hasil.configure(text=(float(nilai1.get())*float(nilai2.get())))
def bagi():
    hasil.configure(text=(float(nilai1.get())/float(nilai2.get())))
def pangkat():
    hasil.configure(text=(float(nilai1.get())**float(nilai2.get())))
def mod():
    hasil.configure(text=(float(nilai1.get())%float(nilai2.get())))
def akar():
    hasil.configure(text=(float(nilai1.get())**(1/float(nilai2.get()))))

# Membuat tombol operasi
button_frame = Frame(window)
button_frame.pack(pady=10)

btn = Button(button_frame, text="Tambah", command=tambah, font=("Arial", 12), bg="blue", fg="white")
btn.grid(column=0, row=0, padx=5, pady=5)

btn = Button(button_frame, text="Kurang", command=kurang, font=("Arial", 12), bg="blue", fg="white")
btn.grid(column=1, row=0, padx=5, pady=5)

btn = Button(button_frame, text="Kali", command=kali, font=("Arial", 12), bg="blue", fg="white")
btn.grid(column=2, row=0, padx=5, pady=5)

btn = Button(button_frame, text="Bagi", command=bagi, font=("Arial", 12), bg="blue", fg="white")
btn.grid(column=0, row=1, padx=5, pady=5)

btn = Button(button_frame, text="Pangkat", command=pangkat, font=("Arial", 12), bg="blue", fg="white")
btn.grid(column=1, row=1, padx=5, pady=5)

btn = Button(button_frame, text="Mod", command=mod, font=("Arial", 12), bg="blue", fg="white")
btn.grid(column=2, row=1, padx=5, pady=5)

btn = Button(button_frame, text="Akar", command=akar , font=("Arial", 12), bg="blue", fg="white")
btn.grid(column=1, row=2, padx=5, pady=5)

window.configure(bg="#B0C4DE")

window.mainloop()


# In[ ]:




