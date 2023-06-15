# Application to watermark images
#TODO 1: Imports
import tkinter
from tkinter import *
from tkinter import filedialog as fd
from PIL import Image,ImageDraw,ImageFont
from tkinter import messagebox

global filename
#TODO 2: Functions:
# Select file from the local disk
def select_file():
    global filename
    filename=fd.askopenfilename()
    label_2.configure(text=filename)
    watermark.focus_set()
    watermark.select_range(0,tkinter.END)

def mark():
    # get filepath
    global filename
    # open image in Image class
    im = Image.open(filename)
    width, height = im.size
    extension=im.format
    print(extension)
    # Create draw object
    draw = ImageDraw.Draw(im)
    text = watermark.get()
    # set font
    font = ImageFont.truetype('arial', 32)
    textwidth, textheight = draw.textsize(text, font)
    # calculate the x,y coordinates of the text
    margin = 10
    x = margin
    y = height - textheight - margin
    # draw watermark in the bottom left corner
    if bl.get()==1:
        draw.text((x, y), text, font=font,fill=(233,221,232,int(alpha_value.get())))
    # draw watermark in the top right corner
    if br.get()==1:
        x = width - textwidth - margin
        y = height - textheight - margin
        draw.text((x, y), text, font=font, fill=(233,221,232,int(alpha_value.get())))
    # draw watermark in the center
    if center.get()==1:
        x = width//2 - textwidth//2
        y = height//2 -textheight//2
        draw.text((x, y), text, font=font, fill=(233,221,232,int(alpha_value.get())))
    # draw watermark in the top left
    if tl.get()==1:
        x = margin
        y = margin
        draw.text((x, y), text, font=font, fill=(233,221,232,int(alpha_value.get())))
    # draw watermark in top right
    if tr.get()==1:
        x = width - textwidth - margin
        y = margin
        draw.text((x, y), text, font=font, fill=(233,221,232,int(alpha_value.get())))
    im.show()
    try:
        savefilename = fd.asksaveasfile(title=f"Save File As", filetypes=[("Image File",f".{extension}")], defaultextension=f".{extension}")
        im.save(savefilename)
    except KeyError:
        messagebox.showwarning("PyWtMrk","You have not saved the file!")
    except ValueError:
        messagebox.showwarning("PyWtMrk", "You have not saved the file!")
    else:
        messagebox.showinfo("PyWtMrk","File Saved Successfully!")
    finally:
        return
#TODO : Runtime

#GUI Design using tkinter

window=Tk()
s_width=window.winfo_screenwidth()
s_height=window.winfo_screenheight()
x1=s_width//2-750//2
y1=s_height//2-750//2
window.geometry('{}x{}+{}+{}'.format(750,750,x1,y1))
window.title("PyWtMrk")
window.configure(pady=10,padx=10,bg="skyblue")
canvas=Canvas(width=225,height=225,bg="skyblue",highlightthickness=0)
logo_img=PhotoImage(file='logo.png',height=200,width=200)
canvas.create_image(125,100,image=logo_img)
canvas.grid(column=1,row=1,padx=10,pady=10,columnspan=2)

title_label=Label(text="PyWtMrk",font=("Tahoma",30,"bold"),foreground="blue",justify="center",bg="skyblue")
title_label.grid(column=1,row=0,padx=10,pady=10,columnspan=2)

label_1=Label(text="Select the image file:",font=("Tahoma",14,"normal"),bg="skyblue")
label_1.grid(column=0,row=2,padx=10,pady=10)

file_select=Button(text="Select File",command=select_file,font=("Tahoma",12,"bold"),bg="grey")
file_select.grid(column=2,row=2,padx=10,pady=10)

label_2=Label(text="filepath",padx=10,pady=10,font=("Tahoma",8,"normal"),bg="skyblue")
label_2.grid(column=1,row=3,padx=10,pady=10,columnspan=2)

watermark=Entry(font=("Tahoma",14,"bold"),width=12,bg="white",)
watermark.insert(0,"Write your text here")
watermark.grid(column=0,row=4,padx=10,pady=10)

file_select=Button(text="Mark",command=mark,font=("Tahoma",12,"bold"),bg="grey")
file_select.grid(column=2,row=4,padx=10,pady=10)

#define checkbox variables
tr=IntVar()
tl=IntVar()
center=IntVar()
br=IntVar()
bl=IntVar()
top_right=Checkbutton(text="Top Right",variable=tr,justify="left").grid(column=0,row=5,padx=5,pady=5)
top_left=Checkbutton(text="Top Right",variable=tl,justify="left").grid(column=1,row=5,padx=5,pady=5)
botton_right=Checkbutton(text="Bottom Right",variable=br,justify="left").grid(column=2,row=5,padx=5,pady=5)
bottom_left=Checkbutton(text="Bottom Left",variable=bl,justify="left").grid(column=0,row=6,padx=5,pady=5)
center_=Checkbutton(text="Center",variable=center,justify="left").grid(column=1,row=6,padx=5,pady=5)


alpha_value=DoubleVar()
slider=Scale(label="Alpha Channel",from_=0, to=255,variable=alpha_value,orient="horizontal").grid(column=2,row=6,padx=5,pady=5)
title_label=Label(text="Created by Narendra Kashikar\nVisit narendrakashikar.life for more projects",font=("Tahoma",8,"bold"),foreground="blue",justify="center",bg="skyblue")
title_label.grid(column=1,row=8,padx=10,pady=10,columnspan=2)
window.mainloop()