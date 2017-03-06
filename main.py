from tkinter import *
from PIL import Image, ImageDraw, ImageFont, ImageTk

master = Tk()

#
# Variables
#
canvas_width = StringVar()
canvas_height = StringVar()
canvas_color_R = IntVar()
canvas_color_G = IntVar()
canvas_color_B = IntVar()
canvas_opacity = IntVar()
text_color_R = IntVar()
text_color_G = IntVar()
text_color_B = IntVar()
text_opacity = IntVar()
text = StringVar()
image = None

#
# Labels
#
label_canvas = Label(master, text="CANVAS")
label_canvas_width = Label(master, text="width")
label_canvas_height = Label(master, text="height")
label_canvas_color_R = Label(master, text="color R")
label_canvas_color_G = Label(master, text="color G")
label_canvas_color_B = Label(master, text="color B")
label_canvas_opacity = Label(master, text="opacity")
label_text = Label(master, text="TEXT")
label_text_color_R = Label(master, text="color R")
label_text_color_G = Label(master, text="color G")
label_text_color_B = Label(master, text="color B")
label_text_opacity = Label(master, text="opacity")
label_text_content = Label(master, text="text")

#
# Validators
#

def int_validator(value):
    try:
        if value:
            v = int(value)
            return True
    except ValueError:
        return False
    return False


def canvas_width_validator(value):
    result = int_validator(value)
    if not result:
        canvas_width.set('')
    return result


def canvas_height_validator(value):
    result = int_validator(value)
    if not result:
        canvas_height.set('')
    return result


# https://stackoverflow.com/questions/4140437/interactively-validating-entry-widget-content-in-tkinter#4140988
vcmd_cwv = (master.register(canvas_width_validator), '%S')
vcmd_chv = (master.register(canvas_height_validator), '%S')

#
# Inputs
#
entry_canvas_width = Entry(master, textvariable=canvas_width, validatecommand=vcmd_cwv, validate='key')
entry_canvas_height = Entry(master, textvariable=canvas_height, validatecommand=vcmd_chv, validate='key')
entry_canvas_color_R = Scale(master, from_=0, to=255, orient=HORIZONTAL, showvalue=0, variable=canvas_color_R)
entry_canvas_color_G = Scale(master, from_=0, to=255, orient=HORIZONTAL, showvalue=0, variable=canvas_color_G)
entry_canvas_color_B = Scale(master, from_=0, to=255, orient=HORIZONTAL, showvalue=0, variable=canvas_color_B)
entry_canvas_opacity = Scale(master, from_=0, to=255, orient=HORIZONTAL, showvalue=0, variable=canvas_opacity)
entry_text_color_R = Scale(master, from_=0, to=255, orient=HORIZONTAL, showvalue=0, variable=text_color_R)
entry_text_color_G = Scale(master, from_=0, to=255, orient=HORIZONTAL, showvalue=0, variable=text_color_G)
entry_text_color_B = Scale(master, from_=0, to=255, orient=HORIZONTAL, showvalue=0, variable=text_color_B)
entry_text_opacity = Scale(master, from_=0, to=255, orient=HORIZONTAL, showvalue=0, variable=text_opacity)
entry_text = Entry(master, textvariable=text)

#
# Callbacks
#
def callback():
    try:
        canvas_x = int(canvas_width.get())
        canvas_y = int(canvas_height.get())
    except ValueError:
        return
    base = Image.new('RGBA', (canvas_x, canvas_y))

    # make a blank image for the text, initialized to transparent text color
    background_opacity = canvas_opacity.get()
    canvas_background = (canvas_color_R.get(), canvas_color_G.get(), canvas_color_B.get(), background_opacity)
    print(canvas_background)
    txt = Image.new('RGBA', base.size, canvas_background)

    # get a font
    fnt = ImageFont.truetype('FreeMono.ttf', 40)
    # get a drawing context
    d = ImageDraw.Draw(txt)

    # draw text, half opacity
    text_fill = (text_color_R.get(), text_color_G.get(), text_color_B.get(), text_opacity.get())
    print(text_fill)
    d.text((10,10), text.get(), font=fnt, fill=text_fill)

    out = Image.alpha_composite(base, txt)
    out.save('lena_out.png')

    global image
    image = ImageTk.PhotoImage(out)
    # canvas.config(width=canvas_width.get(), height=canvas_height.get())
    # canvas.create_image((0, 0), image=image)
    canvas.config(image=image)
    print('yahooo')

#
# Buttons
#

button = Button(text='hi!', command=callback)

#
# layout
#

label_canvas.grid()
label_canvas_width.grid(sticky=E+N)
label_canvas_height.grid(sticky=E+N)
label_canvas_color_R.grid(sticky=E+N)
label_canvas_color_G.grid(sticky=E+N)
label_canvas_color_B.grid(sticky=E+N)
label_canvas_opacity.grid(sticky=E+N)
label_text.grid()
label_text_color_R.grid(sticky=E+N)
label_text_color_G.grid(sticky=E+N)
label_text_color_B.grid(sticky=E+N)
label_text_opacity.grid(sticky=E+N)
label_text_content.grid(sticky=E+N)

entry_canvas_width.grid(row=1, column=1, sticky=N)
entry_canvas_height.grid(row=2, column=1, sticky=N)
entry_canvas_color_R.grid(row=3, column=1, sticky=N)
entry_canvas_color_G.grid(row=4, column=1, sticky=N)
entry_canvas_color_B.grid(row=5, column=1, sticky=N)
entry_canvas_opacity.grid(row=6, column=1, sticky=N)
entry_text_color_R.grid(row=8, column=1, sticky=N)
entry_text_color_G.grid(row=9, column=1, sticky=N)
entry_text_color_B.grid(row=10, column=1, sticky=N)
entry_text_opacity.grid(row=11, column=1, sticky=N)
entry_text.grid(row=12, column=1, sticky=E)

# canvas = Canvas(master, width=200, height=200)
canvas = Label(master)  #, width=200, height=200)
canvas.grid(row=0, column=2, columnspan=2, rowspan=10, sticky=W+E+N+S, padx=5,
            pady=5)
button.grid(row=12, column=3, rowspan=2)


master.mainloop()

#
# Init
#