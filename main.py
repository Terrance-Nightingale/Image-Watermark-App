from tkinter import *
from tkinter.filedialog import askopenfilename
from PIL import Image, ImageTk

BACKGROUND_COLOR = "#d8d8eb"
FONT = ("Ariel", 14, "bold")


def upload():
    filename = askopenfilename(title="Choose a file", filetypes=[(".png file", "*.png")])
    image = Image.open(filename)

    # If image dimensions scale is less than 1, round it to 1. Else keep the scaling.
    resize_scale = int(image.width / 400)
    if resize_scale < 1:
        resize_scale = 1
    resized_width = int(image.width / resize_scale)
    resized_height = int(image.height / resize_scale)
    image = image.resize((resized_width, resized_height))

    canv_image = ImageTk.PhotoImage(image)
    image_label.config(image=canv_image)
    image_label.image=canv_image


window = Tk()
window.title("Image Watermarking App")
window.minsize(width=600, height=600)
window.config(padx=50, pady=20, bg=BACKGROUND_COLOR)

frame = Frame(window, relief=SOLID, borderwidth=2)
frame.grid(column=0, row=0, columnspan=3)

image = Image.open("./images/default_img.png")
image = image.resize((400, 400))
canv_image = ImageTk.PhotoImage(image)

image_title = Label(frame, text="Your Image Here 🢃", font=FONT)
image_title.pack()
image_title.config(bg="white")

image_label = Label(window, image=canv_image, width=500, height=300, bg=BACKGROUND_COLOR)
image_label.grid(column=0, row=1, columnspan=3)

wm_btn_img = Image.open("./images/water_button_icon.png")
wm_btn_img = wm_btn_img.resize((175, 75))
wm_btn_icon = ImageTk.PhotoImage(wm_btn_img)
wm_button = Button(image=wm_btn_icon, command=upload, bg=BACKGROUND_COLOR, activebackground=BACKGROUND_COLOR,
                   text="Add watermark",font=FONT, compound="center")
wm_button.config(highlightthickness=0, borderwidth=0)
wm_button.grid(column=0, row=2)

import_btn_img = Image.open("./images/import_button_icon.png")
import_btn_img = import_btn_img.resize((175, 75))
import_btn_icon = ImageTk.PhotoImage(import_btn_img)
import_button = Button(image=import_btn_icon, command=upload, bg=BACKGROUND_COLOR, activebackground=BACKGROUND_COLOR,
                       text="Import Image", font=FONT, compound="center")
import_button.config(highlightthickness=0, borderwidth=0)
import_button.grid(column=1, row=2)

save_btn_img = Image.open("./images/save_button_icon.png")
save_btn_img = save_btn_img.resize((175, 75))
save_btn_img = ImageTk.PhotoImage(save_btn_img)
save_button = Button(image=save_btn_img, command=upload, bg=BACKGROUND_COLOR, activebackground=BACKGROUND_COLOR,
                     text="Save Image",font=FONT, compound="center")
save_button.config(highlightthickness=0, borderwidth=0)
save_button.grid(column=2, row=2)

window.mainloop()
