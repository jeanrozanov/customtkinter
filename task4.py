import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

root = ctk.CTk()
root.title("Задание №3")
root.geometry("500x500")
my_font = ctk.CTkFont(size=20)


def handle_switch_choice():
    if var_switch.get():
        ctk.set_appearance_mode("light")
        switch.configure(text="Светлая тема")
    else:
        ctk.set_appearance_mode("dark")
        switch.configure(text="Темная тема")


def handle_slider_1_choice(value):
    # изменение ползунка:
    if value == 0:
        label_1.configure(text="красный ползунок")
        slider_1.configure(button_color="red")
    if value == 1:
        label_1.configure(text="зеленый ползунок")
        slider_1.configure(button_color="green")
    if value == 2:
        label_1.configure(text="синий ползунок")
        slider_1.configure(button_color="blue")


var_slider_1 = ctk.DoubleVar()
slider_1 = ctk.CTkSlider(
    master=root,
    button_color="red",
    from_=0, to=2,
    variable=var_slider_1,
    orientation="horizontal",
    number_of_steps=2
)
slider_1.configure(command=handle_slider_1_choice)
slider_1.set(0)  # значение на старте
label_1 = ctk.CTkLabel(master=root, text="красный ползунок", font=my_font)

var_slider_1.get()

# Switch - переключатель (похоже на RadioButton, но только два состояния):
var_switch = ctk.BooleanVar()
switch = ctk.CTkSwitch(master=root, variable=var_switch, onvalue=True, offvalue=False)
switch.configure(text="Темная тема", font=my_font)
switch.configure(command=handle_switch_choice)
var_switch.set(True)

switch.pack(pady=100)
slider_1.pack(pady=(100, 10))  # отступ 100px сверху и 10px снизу
label_1.pack(pady=(10, 100))

root.mainloop()
