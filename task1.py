from cProfile import label

import customtkinter as ctk


def handle_button_press():
    global root, entry
    text = entry.get()
    print(f"Текст, введенный в поле: {text}")
    entry.delete(0, 'end')

    entry._activate_placeholder()
    root.focus_set()


ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

root = ctk.CTk()
root.title("Задание №1")
root.geometry("500x500")
my_font = ctk.CTkFont(size=20)

label = ctk.CTkLabel(master=root)
label.configure(
    text="Привет, Аноним!",
    font=my_font,
    text_color='white'
)

entry = ctk.CTkEntry(master=root)
entry.configure(
    placeholder_text="Введи своё имя",  # данный текст должен подсказывать, что нужно ввести в поле
    justify="center",  # расположение текста и подсказки будет по центру поля
    font=my_font,
    width=250  # ширина виджета в пикселях
)

button = ctk.CTkButton(master=root, text="Готово", font=my_font, command=handle_button_press)

entry.pack(pady=100)
button.pack(pady=100)
label.pack(pady=100)


root.mainloop()
