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


# 2 задание:

import customtkinter as ctk


ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

root = ctk.CTk()
root.title("Название приложения")
root.geometry("1100x800")
my_font = ctk.CTkFont(family="Roboto", size=30)

elements_1 = []
combobox_1 = ctk.CTkComboBox(master=root)
combobox_1.configure(font=my_font, values=elements_1, state="readonly")

elements_2 = []
combobox_2 = ctk.CTkComboBox(master=root)
combobox_2.configure(font=my_font, values=elements_2, state="readonly")

elements_3 = []
combobox_3 = ctk.CTkComboBox(master=root)
combobox_3.configure(font=my_font, values=elements_3, state="readonly")

textbox_1 = ctk.CTkTextbox(master=root)
textbox_1.configure(font=my_font, height=250, width=600, state="disabled")

textbox_2 = ctk.CTkTextbox(master=root)
textbox_2.configure(font=my_font, height=100, width=1500, state="disabled")

button = ctk.CTkButton(master=root)
button.configure(text="Готово", font=my_font, text_color="white", fg_color="#00BFFF", hover_color="#00759E")

rows, columns = 5, 3
for i in range(rows):
    root.rowconfigure(index=i, weight=1)
for i in range(columns):
    root.columnconfigure(index=i, weight=1)

combobox_1.grid(row=0, column=0)
combobox_2.grid(row=1, column=0)
combobox_3.grid(row=2, column=0)
textbox_1.grid(row=0, column=1)
textbox_2.grid(row=3, column=0, columnspan=2)
button.grid(row=1, column=1)


combobox_1.configure(width=400, height=50)
combobox_2.configure(width=400, height=50)
combobox_3.configure(width=400, height=50)
button.configure(width=600)
textbox_2.configure(height=200)
root.mainloop()
