from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename
from PIL import Image, ImageTk, ImageDraw, ImageFont

BG_COLOR = "#d8d8eb"
FONT = ("Ariel", 14, "bold")
WM_TEXT = ""


def upload():
    global image
    global canv_image

    filename = askopenfilename(title="Choose a file", filetypes=[(".png file", "*.png")])
    try:
        image = Image.open(filename)
    except AttributeError:
        return
    # If image dimensions scale is less than 1, round it to 1. Else keep the scaling.
    resize_scale = image.width / 375
    if resize_scale < 0.5:
        resize_scale = 1
    resized_width = int(image.width / resize_scale)
    resized_height = int(image.height / resize_scale)
    image = image.resize((resized_width, resized_height))

    canv_image = ImageTk.PhotoImage(image)
    image_label.config(image=canv_image)


def save():
    save_file = asksaveasfilename(title="Save file", filetypes=[(".png file", "*.png")])
    if save_file:
        wm_image = image
        wm_image.save(save_file)


def watermark():
    global image, canv_image

    image = image.rotate(-45, expand=1)
    draw = ImageDraw.Draw(image)
    wm_text = wm_entry.get()
    font = ImageFont.truetype('arial.ttf', 30)
    width, height = image.size
    x = width / 6
    y = height / 4
    for _ in range(0, 5):
        draw.text((x, y), wm_text, font=font, fill=(0, 0, 0, 0))
        x += 60
        y += 80
    image = image.rotate(45, expand=1)
    canv_image = ImageTk.PhotoImage(image)
    image_label.config(image=canv_image)


window = Tk()
window.title("Image Watermarking App")
window.minsize(width=600, height=600)
window.config(padx=50, pady=20, bg=BG_COLOR)

frame = Frame(window, relief=SOLID, borderwidth=2)
frame.grid(column=0, row=0, columnspan=3)

image = Image.open("./images/default_img.png")
image = image.resize((375, 375))
canv_image = ImageTk.PhotoImage(image)

image_title = Label(frame, text="Add a Watermark to Your Image Here 🢃", font=("Ariel", 20, "bold"))
image_title.pack()
image_title.config(bg="white", padx=5, pady=5)

image_label = Label(window, image=canv_image, width=500, height=300, bg=BG_COLOR)
image_label.grid(column=0, row=1, columnspan=3)

wm_btn_img = Image.open("./images/water_button_icon.png")
wm_btn_img = wm_btn_img.resize((175, 75))
wm_btn_icon = ImageTk.PhotoImage(wm_btn_img)
wm_button = Button(image=wm_btn_icon, command=watermark, bg=BG_COLOR, activebackground=BG_COLOR,
                   text="Add watermark", font=FONT, compound="center")
wm_button.config(highlightthickness=0, borderwidth=0)
wm_button.grid(column=0, row=2)

import_btn_img = Image.open("./images/import_button_icon.png")
import_btn_img = import_btn_img.resize((175, 75))
import_btn_icon = ImageTk.PhotoImage(import_btn_img)
import_button = Button(image=import_btn_icon, command=upload, bg=BG_COLOR, activebackground=BG_COLOR,
                       text="Import Image", font=FONT, compound="center")
import_button.config(highlightthickness=0, borderwidth=0)
import_button.grid(column=1, row=2)

save_btn_img = Image.open("./images/save_button_icon.png")
save_btn_img = save_btn_img.resize((175, 75))
save_btn_img = ImageTk.PhotoImage(save_btn_img)
save_button = Button(image=save_btn_img, command=save, bg=BG_COLOR, activebackground=BG_COLOR,
                     text="Save Image", font=FONT, compound="center")
save_button.config(highlightthickness=0, borderwidth=0)
save_button.grid(column=2, row=2)

wm_entry_label = Label(text="Your Watermark Text Here:", font=("Ariel", 10, "bold"), bg=BG_COLOR)
wm_entry_label.grid(column=0, row=3)
wm_entry_label.config(pady=20)

wm_entry = Entry(width=50)
wm_entry.grid(column=1, row=3, columnspan=2, sticky="EW")
wm_entry.insert(END, "Placeholder Text ©")
wm_entry.focus()

window.mainloop()
