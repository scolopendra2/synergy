import random
import tkinter as tk

definitions = {
    'While': 'Цикл "while" используется для выполнения блока кода, пока условие истинно.',
    'For': 'Цикл "for" используется для итерации по элементам последовательности (например, списку или строке).',
    'If': 'Условие "if" позволяет выполнить определенный блок кода, если условие истинно.',
    'Function': 'Функция - это блок кода, который можно вызывать с определенными аргументами.',
    'List': 'Список - это упорядоченная коллекция элементов, которая может содержать разные типы данных.'
}


def show_random_definition():
    random_key = random.choice(list(definitions.keys()))
    definition_text.delete('1.0', tk.END)
    definition_text.insert(tk.END, definitions[random_key])


my_tk = tk.Tk()
my_tk.title('Определения Python')
my_tk.configure(bg='#00FFFF')

title = tk.Label(my_tk, text='Определения Python', font=('Arial', 16), bg='#00FFFF')
title.pack(pady=10)

definition_text = tk.Text(my_tk, height=5, width=50)
definition_text.pack()

show_definition = tk.Button(my_tk, text='Показать определение', command=show_random_definition)
show_definition.pack(pady=10)

my_tk.mainloop()
