import customtkinter as ctk


ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

root = ctk.CTk()
root.title("Задание №1")
root.geometry("500x500")
my_font = ctk.CTkFont(size=20)


def handle_button_press():  # хендлер для кнопки - не должен принимать никаких аргументов
    # хендлер срабатывает при нажатии на кнопку, то есть это событийно-ориентированное программирование
    global button, cnt, flag_color, num1, num2, summa  # связываемся с глобальными переменными
    num1 = entry1.get()
    num2 = entry2.get()
    summa = int(num1) + int(num2)
    entry3.configure(state="normal")  # разблокируем поле
    entry3.delete(0, "end")  # удалим оттуда старую строчку
    entry3.insert(0, summa)  # вставим новую
    entry3.configure(state="readonly")  # снова заблокируем


label1 = ctk.CTkLabel(master=root)
label1.configure(
    text="+",
    font=my_font,
    text_color="white"
)

label2 = ctk.CTkLabel(master=root)
label2.configure(
    text="=",
    font=my_font,
    text_color="white"
)

entry1 = ctk.CTkEntry(master=root)
entry1.configure(
    justify="center",  # расположение текста и подсказки будет по центру поля
    font=my_font,
    width=250  # ширина виджета в пикселях
)

entry2 = ctk.CTkEntry(master=root)
entry2.configure(
    justify="center",
    font=my_font,
    width=250
)

entry3 = ctk.CTkEntry(master=root)
entry3.configure(
    justify="center",
    font=my_font,
    width=250
)
entry3.configure(state="readonly")  # заблокировали поле

button = ctk.CTkButton(master=root, text="Посчитать", font=my_font)

button.configure(command=handle_button_press)

cnt = 0  # счётчик числа нажатий на кнопку
flag_color = "white"

entry1.pack(pady=10)
label1.pack(pady=10)
entry2.pack(pady=30)
label2.pack(pady=10)
entry3.pack(pady=40)
button.pack(pady=0)


root.mainloop()
