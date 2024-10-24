THEME_COLOR = "#375362"
from tkinter import *
from PIL import Image
from PIL import ImageTk
from PIL import ImageDraw


class QuizInterface:

    def __init__(self):
        self.window = Tk()
        self.window.title("WaterMarker")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.canvas = Canvas(self.window, width=720, height=750, bg=THEME_COLOR, highlightthickness=0)
        self.canvas.grid(row=0, column=0)

        with Image.open("tsok.jpg") as im:
            draw = ImageDraw.Draw(im)
            pos = (im.size[0]/2, im.size[1]/2)
            amount = im.size[0]/20
            draw.text(pos, 'Created by Metskas', fill='darkblue', align='center',  font_size=amount, width=20)
            im.save('images/newpicture.jpg')

        img = ImageTk.PhotoImage(im)
        self.canvas.create_image(50, 50, anchor='center', image=img)

        self.window.mainloop()


quiz = QuizInterface()

