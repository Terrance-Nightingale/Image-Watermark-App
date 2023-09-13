from tkinter import *
from tkinter.filedialog import askopenfilename
from PIL import Image, ImageTk

BACKGROUND_COLOR = "#d8d8eb"
FONT = ("Ariel", 14, "bold")


def upload():
    filename = askopenfilename(title="Choose a file", filetypes=[(".png file", "*.png")])
    # my_label.config(text=input.get())
    image = Image.open(filename)
    # If image dimensions scale is less than 1, round it to 1. Else keep the scaling.
    resize_scale = int(image.width / 400)
    resized_width = int(image.width / resize_scale)
    resized_height = int(image.height / resize_scale)
    image = image.resize((resized_width, resized_height))
    canv_image = ImageTk.PhotoImage(image)


window = Tk()
window.title("Image Watermarking App")
window.minsize(width=600, height=600)
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)

image = Image.open("./images/default_img.png")
image = image.resize((400, 400))
canv_image = ImageTk.PhotoImage(image)

image_label = Label(window, image=canv_image, width=500, height=300, bg=BACKGROUND_COLOR)
image_label.grid(column=0, row=0, columnspan=2)
image_label.config(padx=50, pady=50)

wm_btn_img = Image.open("./images/water_button_icon.png")
wm_btn_img = wm_btn_img.resize((175, 75))
wm_btn_icon = ImageTk.PhotoImage(wm_btn_img)
wm_button = Button(image=wm_btn_icon, text="Add watermark", bg=BACKGROUND_COLOR, activebackground=BACKGROUND_COLOR,)
wm_button.config(highlightthickness=0, borderwidth=0)
wm_button.grid(column=0, row=1)

button = Button(text="Import file", command=upload, bg=BACKGROUND_COLOR,  activebackground=BACKGROUND_COLOR,)
button.grid(column=1, row=1)

wm_btn_label = Label(window, width=20, height=10, text="Add Watermark", bg=BACKGROUND_COLOR, font=FONT)
wm_btn_label.grid(column=0, row=2)

save_btn_label = Label(window, width=20, height=10, text="Save Image", bg=BACKGROUND_COLOR, font=FONT)
save_btn_label.grid(column=1, row=2)

window.mainloop()
