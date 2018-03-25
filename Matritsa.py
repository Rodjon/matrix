import tkinter
from tkinter import *
from tkinter.messagebox import *

def matrix(): #Считает матрицу
    try:
        a11 = int(ent_a11.get())
        a12 = int(ent_a12.get())
        a13 = int(ent_a13.get())
        a21 = int(ent_a21.get())
        a22 = int(ent_a22.get())
        a23 = int(ent_a23.get())
        a31 = int(ent_a31.get())
        a32 = int(ent_a32.get())
        a33 = int(ent_a33.get())
        c = (a11*a22*a33)+(a12*a23*a31)+(a21*a32*a13)-(a13*a22*a31)-(a32*a23*a11)-(a21*a12*a33)
        # Кнопка вызова диалогового окна
        btn1 = Button(root, text="Определитель", command=lambda: showinfo("Определитель равен=", c))
        btn1.grid(row=4, column=0, sticky="ew")
        # Доделать. Обработчик ошибок
    except ValueError:
        notif("Ошибка")

root = Tk()
label1 = Label(root, text="Матрица")
label1.grid()

# Создаем фрейм
frame = Frame(root)
frame.grid()

#Здесь поля для заполнения матрицы
ent_a11 = Entry(frame, width=7, borderwidth=3)
ent_a11.grid(row=1,column=0)

ent_a12 = Entry(frame, width=7, borderwidth=3)
ent_a12.grid(row=1,column=1)

ent_a13 = Entry(frame, width=7, borderwidth=3)
ent_a13.grid(row=1,column=2)


ent_a21 = Entry(frame, width=7, borderwidth=3)
ent_a21.grid(row=2,column=0)

ent_a22 = Entry(frame, width=7, borderwidth=3)
ent_a22.grid(row=2,column=1)

ent_a23 = Entry(frame, width=7, borderwidth=3)
ent_a23.grid(row=2,column=2)

ent_a31 = Entry(frame, width=7, borderwidth=3)
ent_a31.grid(row=3,column=0)

ent_a32 = Entry(frame, width=7, borderwidth=3)
ent_a32.grid(row=3,column=1)

ent_a33 = Entry(frame, width=7, borderwidth=3)
ent_a33.grid(row=3,column=2)



#Кнопка Чтобы посчитать
button1 = Button(frame, text="Посчитать", command=matrix)
button1.grid()

root.mainloop()
