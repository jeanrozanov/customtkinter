import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

root = ctk.CTk()
root.title("Задание №3")
root.geometry("500x500")
my_font = ctk.CTkFont(size=20)


def handle_button_press():  # хендлер для кнопки - не должен принимать никаких аргументов
    global button, cnt, flag_color, word  # связываемся с глобальными переменными
    if var_radiobuttons_1.get() == 1:
        entry1.configure(text_color='white')
    if var_radiobuttons_1.get() == 2:
        entry1.configure(text_color='red')
    if var_radiobuttons_1.get() == 3:
        entry1.configure(text_color='yellow')

    word = combobox.get()
    if var_checkbox_1:
        entry1.insert(0, word + '!')
    else:
        entry1.insert(0, word + '?')
    entry1.configure(state="normal")  # разблокируем поле
    entry1.delete(0, "end")  # удалим оттуда старую строчку
    entry1.insert(0, word)  # вставим новую
    entry1.configure(state="readonly")  # снова заблокируем


elems = ["Ты уходишь", "Элемент 2", "Элемент 3"]  # список элементов
combobox = ctk.CTkComboBox(master=root)
combobox.configure(
    font=my_font,
    justify="center",
    values=elems,  # указываем созданный ранее список элементов
    state="readonly",  # режим "только для чтения", чтобы пользователь не мог случайно стереть выбираемый элемент
    width=235
)
combobox.set("Выберите фразу:")  # значение элемента по умолчанию

# взаимодействие с ComboBox:


var_checkbox_1 = ctk.BooleanVar()  # первый флажок будет привязан к первой переменной
# она имеет тип bool, то есть может принимать всего два значения: True или False; это логично, потому что флажок тоже
# может принимать всего два состояния: активен или не активен; свяжем состояние "активен" с True, "не активен" - с False

checkbox_1 = ctk.CTkCheckBox(
    master=root,
    variable=var_checkbox_1,  # переменная, к которой привязываем флажок
    onvalue=True,  # значение переменной, когда флажок активен, мы решили, что это будет True
    offvalue=False  # значение переменной, когда флажок не активен, мы решили, что это будет False
)
checkbox_1.configure(text="Добавить в конец !", font=my_font)

var_checkbox_1.set(True)  # значение переменной по умолчанию, то есть по умолчанию первый флажок будет активен

var_checkbox_2 = ctk.BooleanVar()  # второй флажок будет привязан ко второй переменной
checkbox_2 = ctk.CTkCheckBox(master=root, variable=var_checkbox_2, onvalue=True, offvalue=False)
checkbox_2.configure(text="Добавить в конец ?", font=my_font)
var_checkbox_2.set(False)  # значение переменной по умолчанию, то есть по умолчанию второй флажок будет неактивен

# взаимодействие с CheckBox:
var_checkbox_1.get()  # True или False
var_checkbox_2.get()

var_radiobuttons_1 = ctk.IntVar()  # переключатели будут привязаны к одной переменной типа int, образуя связанную группу


radiobutton_1 = ctk.CTkRadioButton(
    master=root,
    variable=var_radiobuttons_1,  # привязываем переключатель к переменной
    value=1  # значение данного переключателя
)
# параметры variable и value обязательно указываем при создании, а не в .configure()
radiobutton_1.configure(text="Белый цвет текста", font=my_font)

radiobutton_2 = ctk.CTkRadioButton(master=root, variable=var_radiobuttons_1, value=2)
radiobutton_2.configure(text="Красный цвет текста", font=my_font)

radiobutton_3 = ctk.CTkRadioButton(master=root, variable=var_radiobuttons_1, value=3)
radiobutton_3.configure(text="Жёлтый цвет текста", font=my_font)

var_radiobuttons_1.set(1)  # значение переменной по умолчанию, то есть по умолчанию будет активен 1-ый переключатель

# взаимодействие с RadioButton:
var_radiobuttons_1.get()

entry1 = ctk.CTkEntry(master=root)
entry1.configure(
    justify="center",  # расположение текста и подсказки будет по центру поля
    font=my_font,
    width=250  # ширина виджета в пикселях
)

button = ctk.CTkButton(master=root, text="Выбрать", font=my_font)

button.configure(command=handle_button_press)

cnt = 0  # счётчик числа нажатий на кнопку
flag_color = "white"

entry1.pack(pady=10)
radiobutton_1.pack(pady=20)
radiobutton_2.pack(pady=20)
radiobutton_3.pack(pady=20)
combobox.pack(pady=20)
checkbox_1.pack(pady=20)
checkbox_2.pack(pady=20)
button.pack(pady=0)

root.mainloop()
