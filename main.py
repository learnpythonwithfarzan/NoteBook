from tkinter import *
from tkinter.font import *


master = Tk()
master.title('LearnPythonWithFarzan')

main_text_font = Font(family='slab serif', size=18)
toolbar_frame = Frame(master, bg='#231955', height=35)
toolbar_frame.pack(fill=X)

save_button = Button(master, text='Save')
save_button.config(height=1, width=2, bg='#1F4690', fg='#FFE5B4')
save_button.place(x=0, y=0)

load_button = Button(master, text='Load')
load_button.config(height=1, width=2, bg='#1F4690', fg='#FFE5B4')
load_button.place(x=48, y=0)

filename_Label = Label(master, text='File name')
filename_Label.config(height=2, bg='#1F4690', fg='#FFE5B4')
filename_Label.place(x=96, y=0)

main_text = Text(master, bg='#231955', fg='#FFE5B4', font=main_text_font, height=1000)
main_text.pack(fill=X)

master.geometry('300x300')
master.mainloop()
