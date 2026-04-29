import customtkinter as ctk


ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

root = ctk.CTk()
root.title("Название приложения")
root.geometry("900x500")
my_font = ctk.CTkFont(family="Roboto", size=40)

btn_1 = ctk.CTkButton(master=root, text="Вернуться", font=my_font)
btn_2 = ctk.CTkButton(master=root, text="Добавить", font=my_font)
text_1 = ctk.CTkLabel(master=root, text="Суть:", font=my_font)
text_2 = ctk.CTkLabel(master=root, text="Категория товара", font=my_font)
text_3 = ctk.CTkLabel(master=root, text='Добавьте товар', font=my_font)
entry_1 = ctk.CTkEntry(master=root)
entry_1.configure(placeholder_text="Название", font=my_font)
entry_2 = ctk.CTkEntry(master=root)
entry_2.configure(placeholder_text='Цена', font=my_font)
elements = ['Еда', 'Транспорт', 'Одежда', 'Быт.товары', 'Лекарства', 'Крупные траты']
combobox = ctk.CTkComboBox(master=root)
combobox.configure(font=my_font, values=elements, state="readonly")

rows, columns = 5, 3
for i in range(rows):
    root.rowconfigure(index=i, weight=1)
for i in range(columns):
    root.columnconfigure(index=i, weight=1)
btn_1.grid(row=2, column=0)
btn_2.grid(row=3, column=0)
text_1.grid(row=0, column=0, rowspan=2)
text_2.grid(row=1, column=0)
text_3.grid(row=0, columnspan=3)
entry_1.grid(row=1, column=1, padx=(200, 0))
entry_2.grid(row=1, column=2)
combobox.grid(row=2, column=1)

btn_1.configure(width=200, height=50)
btn_2.configure(width=200, height=50)
text_1.configure(width=200, height=50)
entry_1.configure(width=200, height=50)
combobox.configure(width=340, height=50)

root.mainloop()
