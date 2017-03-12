import itertools
import sys

try:
    import tkinter as tk
except ImportError:
    print("tkinter not found.\nOn debian-like distributions install with:\napt install python3-tk")
    sys.exit(0)
import matplotlib.font_manager
import tkinter.font
from PIL import Image, ImageDraw, ImageFont, ImageTk


master = tk.Tk()


#
# Variables
#
canvas_width = tk.StringVar()
canvas_height = tk.StringVar()
canvas_color_R = tk.IntVar()
canvas_color_G = tk.IntVar()
canvas_color_B = tk.IntVar()
canvas_opacity = tk.IntVar()
text_color_R = tk.IntVar()
text_color_G = tk.IntVar()
text_color_B = tk.IntVar()
text_opacity = tk.IntVar()
text_size = tk.IntVar()
text = tk.StringVar()
image = None

#
# Labels
#
label_canvas = tk.Label(master, text="CANVAS")
label_canvas_width = tk.Label(master, text="width")
label_canvas_height = tk.Label(master, text="height")
label_canvas_color_R = tk.Label(master, text="color R")
label_canvas_color_G = tk.Label(master, text="color G")
label_canvas_color_B = tk.Label(master, text="color B")
label_canvas_opacity = tk.Label(master, text="opacity")
label_text = tk.Label(master, text="TEXT")
label_text_color_R = tk.Label(master, text="color R")
label_text_color_G = tk.Label(master, text="color G")
label_text_color_B = tk.Label(master, text="color B")
label_text_opacity = tk.Label(master, text="opacity")
label_text_size = tk.Label(master, text="size")
label_text_font = tk.Label(master, text="font")
label_text_content = tk.Label(master, text="text")

#
# Inputs
#
entry_canvas_width = tk.Scale(master, from_=320, to=1900, orient=tk.HORIZONTAL, variable=canvas_width)
entry_canvas_height = tk.Scale(master, from_=160, to=720, orient=tk.HORIZONTAL, variable=canvas_height)
entry_canvas_color_R = tk.Scale(master, from_=0, to=255, orient=tk.HORIZONTAL, showvalue=0, variable=canvas_color_R)
entry_canvas_color_G = tk.Scale(master, from_=0, to=255, orient=tk.HORIZONTAL, showvalue=0, variable=canvas_color_G)
entry_canvas_color_B = tk.Scale(master, from_=0, to=255, orient=tk.HORIZONTAL, showvalue=0, variable=canvas_color_B)
entry_canvas_opacity = tk.Scale(master, from_=0, to=255, orient=tk.HORIZONTAL, showvalue=0, variable=canvas_opacity)
entry_text_color_R = tk.Scale(master, from_=0, to=255, orient=tk.HORIZONTAL, showvalue=0, variable=text_color_R)
entry_text_color_G = tk.Scale(master, from_=0, to=255, orient=tk.HORIZONTAL, showvalue=0, variable=text_color_G)
entry_text_color_B = tk.Scale(master, from_=0, to=255, orient=tk.HORIZONTAL, showvalue=0, variable=text_color_B)
entry_text_opacity = tk.Scale(master, from_=0, to=255, orient=tk.HORIZONTAL, showvalue=0, variable=text_opacity)
entry_text_size = tk.Scale(master, from_=10, to=100, orient=tk.HORIZONTAL, showvalue=0, variable=text_size)
# Why `exportselection`
# https://bytes.com/topic/python/answers/20254-tkinter-listbox-looses-selection-tab
entry_text_font = tk.Listbox(master, exportselection=0)
entry_text = tk.Entry(master, textvariable=text)

_family_set = matplotlib.font_manager.findSystemFonts()
_family_set.sort()
family_set = [f.split('/')[-1].split('.')[0] for f in _family_set]
for name in family_set:
    entry_text_font.insert(tk.END, name)
entry_text_font.selection_set(0)

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
    txt = Image.new('RGBA', base.size, canvas_background)

    # get a font
    font = _family_set[entry_text_font.curselection()[0]]
    fnt = ImageFont.truetype(font=font, size=text_size.get())
    # get a drawing context
    d = ImageDraw.Draw(txt)

    # draw text, half opacity
    text_fill = (text_color_R.get(), text_color_G.get(), text_color_B.get(), text_opacity.get())
    d.text((10,10), text.get(), font=fnt, fill=text_fill)

    out = Image.alpha_composite(base, txt)
    out.save('lena_out.png')

    # keeping a reference to the image is required
    global image
    image = ImageTk.PhotoImage(out)
    canvas.config(image=image)


def crazy(*args):
    callback()

#
# Bindings
#
canvas_width.trace("w", crazy)
canvas_height.trace("w", crazy)
canvas_color_R.trace("w", crazy)
canvas_color_G.trace("w", crazy)
canvas_color_B.trace("w", crazy)
canvas_opacity.trace("w", crazy)
text_color_R.trace("w", crazy)
text_color_G.trace("w", crazy)
text_color_B.trace("w", crazy)
text_opacity.trace("w", crazy)
text_size.trace("w", crazy)
text.trace("w", crazy)
master.bind("<Button-1>", crazy)
master.bind("<Key>", crazy)

#
# Buttons
#
button = tk.Button(text='Tengo hambre!', command=callback)

#
# layout
#
label_canvas.grid()
label_canvas_width.grid(sticky=tk.E+tk.N)
label_canvas_height.grid(sticky=tk.E+tk.N)
label_canvas_color_R.grid(sticky=tk.E+tk.N)
label_canvas_color_G.grid(sticky=tk.E+tk.N)
label_canvas_color_B.grid(sticky=tk.E+tk.N)
label_canvas_opacity.grid(sticky=tk.E+tk.N)
label_text.grid()
label_text_color_R.grid(sticky=tk.E+tk.N)
label_text_color_G.grid(sticky=tk.E+tk.N)
label_text_color_B.grid(sticky=tk.E+tk.N)
label_text_opacity.grid(sticky=tk.E+tk.N)
label_text_size.grid(sticky=tk.E+tk.N)
label_text_font.grid(sticky=tk.E+tk.N)
label_text_content.grid(sticky=tk.E+tk.N)

ROW = itertools.count(start=1)

entry_canvas_width.grid(row=next(ROW), column=1, sticky=tk.N)
entry_canvas_height.grid(row=next(ROW), column=1, sticky=tk.N)
entry_canvas_color_R.grid(row=next(ROW), column=1, sticky=tk.N)
entry_canvas_color_G.grid(row=next(ROW), column=1, sticky=tk.N)
entry_canvas_color_B.grid(row=next(ROW), column=1, sticky=tk.N)
entry_canvas_opacity.grid(row=next(ROW), column=1, sticky=tk.N)
next(ROW)
entry_text_color_R.grid(row=next(ROW), column=1, sticky=tk.N)
entry_text_color_G.grid(row=next(ROW), column=1, sticky=tk.N)
entry_text_color_B.grid(row=next(ROW), column=1, sticky=tk.N)
entry_text_opacity.grid(row=next(ROW), column=1, sticky=tk.N)
entry_text_size.grid(row=next(ROW), column=1, sticky=tk.N)
entry_text_font.grid(row=next(ROW), column=1, sticky=tk.N)
LAST_ROW = next(ROW)
entry_text.grid(row=LAST_ROW, column=1, sticky=tk.E)

# A label works better than a `Canvas`. Canvas doesn't support transparency.
canvas = tk.Label(master)
canvas.grid(row=0, column=2, columnspan=2, rowspan=10, sticky=tk.W+tk.E+tk.N+tk.S, padx=5, pady=5)
button.grid(row=LAST_ROW, column=3, rowspan=2)

#
# Init
#
master.mainloop()
