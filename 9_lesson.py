import tkinter as tk
from tkinter import messagebox


def show_text():
    text = entry.get()
    if text:
        messagebox.showinfo('Введенный текст', text)
    else:
        messagebox.showwarning('Ошибка', 'Поле ввода пустое')


def clear_text():
    entry.delete(0, tk.END)


my_tk = tk.Tk()

my_tk.geometry('300x150')

entry = tk.Entry(my_tk)
entry.pack()

button = tk.Button(my_tk, text='Показать текст', command=show_text)
button.pack()

clear = tk.Button(my_tk, text='Очистить', command=clear_text)
clear.pack()

my_tk.mainloop()
