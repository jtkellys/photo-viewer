from tkinter import *
from PIL import ImageTk, Image


root = Tk()
root.title("Random Stuff")

my_img1 = ImageTk.PhotoImage(Image.open("venv/images/..."))
my_img2 = ImageTk.PhotoImage(Image.open("venv/images/...."))
my_img3 = ImageTk.PhotoImage(Image.open("venv/images/....."))

image_list = [my_img1, my_img2, my_img3]

x = 0

my_label = Label(root, image=image_list[x])
my_label.grid(row=2, column=0, columnspan=3)

image_list = image_list * 99


def forward(image_number):
    global my_label
    global button_forward
    global button_back
    global x
    my_label.grid_forget()
    x += 1
    my_label = Label(image=image_list[x])
    my_label.grid(row=2, column=0, columnspan=3)
    return


def back():
    global my_label
    global button_forward
    global button_back
    global x
    my_label.grid_forget()
    x -= 1
    my_label = Label(image=image_list[x])
    my_label.grid(row=2, column=0, columnspan=3)
    return


button_back = Button(root, text="<<", command=lambda: back())
button_exit = Button(root, text="Exit Program", command=root.quit)
button_forward = Button(root, text=">>", command=lambda: forward(2))

button_back.grid(row=1, column=0)
button_exit.grid(row=1, column=1)
button_forward.grid(row=1, column=2)

root.mainloop()
