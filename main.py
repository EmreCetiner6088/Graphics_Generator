import pandas as pd
import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt

root = tk.Tk()
root.geometry("800x600")
name_list = []
data_list = []
data_list_float = []
label = tk.Label(root, text="Hoşgeldin!")
label.grid(row=0, column=1)

texttitle = tk.Label(root, text="X")
texttitle.grid(row=2, column=0, pady=10)

textbox_name = tk.Text(root, font=('Ariel', 18), width=10, height=1)
textbox_name.grid(row=2, column=1, pady=10)

texttitle2 = tk.Label(root, text="Y")
texttitle2.grid(row=2, column=3, pady=10)

textbox_grade = tk.Text(root, font=('Ariel', 18), height=1, width=10)
textbox_grade.grid(row=2, column=4, pady=10)

columns = ("X", "Y")
tree = ttk.Treeview(root, columns=columns, show="headings")
tree.heading("X", text="X")
tree.heading("Y", text="Y")
tree.grid(row=7, column=0, columnspan=5, sticky='nsew', padx=10, pady=10)

def add_data():
    content = textbox_name.get("1.0", tk.END).strip()
    content2 = textbox_grade.get("1.0", tk.END).strip()
    try:
        global data_list_float, name_list, data_list
        data_list.append(content2)
        name_list.append(content)
        tree.insert("", "end", values=(content, content2))
        textbox_grade.delete("1.0", tk.END)
        textbox_name.delete("1.0", tk.END)
    except Exception as e:
        print("HATA: ", e)

def bar_plot():
    try:
        global data_list_float, name_list, data_list
        fig = plt.figure()
        ax = fig.add_axes([0.03, 0.03, 0.9, 0.9])
        data_list_float = [float(val) for val in data_list]
        ax.bar(name_list, data_list_float)
        ax.set_ylim(0, max(data_list_float) + 5)
        plt.show()
    except Exception as e:
        print("HATA: ", e)

def pie_plot():
    try:
        global data_list_float, name_list
        fig = plt.figure()
        ax = fig.add_axes([0.03, 0.03, 0.9, 0.9])
        data_list_float = [float(val) for val in data_list]
        ax.pie(data_list_float, labels=name_list, autopct='%1.1f%%')
        plt.show()
    except Exception as e:
        print("HATA: ", e)

def plot():
    try:
        global data_list_float
        data_list_float = [float(val) for val in data_list]
        plt.plot(name_list, data_list_float)
        plt.show()
    except Exception as e:
        print("HATA: ", e)

def restart():
    try:
        for item in tree.get_children():
            tree.delete(item)
        global data_list_float,data_list,name_list
        data_list = []
        name_list = []
        data_list_float = []
    except Exception as e:
        print("HATA: ", e)
    


button = tk.Button(root, text="Ekle", command=add_data)
button.grid(row=4, column=0)

button_plot = tk.Button(root, text="Koordinat Grafiği", command=plot)
button_plot.grid(row=4, column=1)

button_bar_plot = tk.Button(root, text="Bar Grafiği", command=bar_plot)
button_bar_plot.grid(row=4, column=2)

button_pie = tk.Button(root, text="Daire Grafiği", command=pie_plot)
button_pie.grid(row=4, column=4)

button_restart = tk.Button(root, text="Sıfırla", command=restart)
button_restart.grid(row=4, column=5)

root.mainloop()
