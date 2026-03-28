import customtkinter as ctk


ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

root = ctk.CTk()
root.title("Задание №1")
root.geometry("500x500")
my_font = ctk.CTkFont(size=20)
name = None
def handle_button_press():  # хендлер для кнопки - не должен принимать никаких аргументов
    # хендлер срабатывает при нажатии на кнопку, то есть это событийно-ориентированное программирование
    global button, cnt, flag_color, name  # связываемся с глобальными переменными
    name = entry.get()
    entry.delete(0, 'end')
    label.configure(text=f"Привет, {name}!")


entry = ctk.CTkEntry(master=root)
entry.configure(
    placeholder_text="Введи своё имя",  # данный текст должен подсказывать, что нужно ввести в поле
    justify="center",  # расположение текста и подсказки будет по центру поля
    font=my_font,
    width=250  # ширина виджета в пикселях
)

label = ctk.CTkLabel(master=root)
label.configure(
    text= f"Привет, Аноним!",
    font=my_font,
    text_color='white'
)


button = ctk.CTkButton(master=root, text="Готово", font=my_font)

button.configure(command=handle_button_press)

cnt = 0  # счётчик числа нажатий на кнопку
flag_color = "white"

label.pack(pady=70)
entry.pack(pady=60)
button.pack(pady=40)


root.mainloop()
