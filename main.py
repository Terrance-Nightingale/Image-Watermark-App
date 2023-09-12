from tkinter import *
from tkinter.filedialog import askopenfilename
from PIL import Image, ImageTk


def upload():
    filename = askopenfilename(title="Choose a file", filetypes=[(".png file", "*.png")])
    # my_label.config(text=input.get())
    image = Image.open(filename)
    canv_image = ImageTk.PhotoImage(image)


window = Tk()
window.title("Image Watermarker")
window.geometry("500x300")
window.config(padx=200, pady=200)

image = Image.open("./images/default_img.png")
image.resize((400, 300))
canv_image = ImageTk.PhotoImage(image)

my_label = Label(window, image=canv_image, width=500, height=300)
my_label.grid(column=0, row=0)
my_label["text"] = "New Text"
my_label.config(padx=50, pady=50)

input = Entry(width=10)
input.grid(column=4, row=2)

button = Button(text="Import file", command=upload)
button.grid(column=1, row=1)

new_button = Button(text="Add watermark")
new_button.grid(column=3, row=0)

window.mainloop()
