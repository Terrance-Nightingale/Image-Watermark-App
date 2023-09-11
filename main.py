from tkinter import *
from tkinter.filedialog import askopenfilename

# image = placeholder_image
# this is initial setup

def upload():
    filename = askopenfilename(title="Choose a file", filetypes=[(".png file", "*.png"), (".jpg file", "*.jpg")])
    my_label.config(text=input.get())
    image = PhotoImage(file=filename)


window = Tk()
window.title("Image Watermarker")
window.minsize(width=500, height=300)
window.config(padx=200, pady=200)

canvas = Canvas(width=850, height=576, highlightthickness=0)
current_card = canvas.create_image(425, 288, image=image)

my_label = Label(text="I am a Label", font=("Arial", 24, "bold"))
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
