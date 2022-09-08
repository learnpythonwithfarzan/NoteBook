from tkinter import *
from tkinter.font import *


def save_window():
    def save():
        file_name = file_name_entry.get()
        file_ext = file_extension_entry.get()
        full_name = file_name + '.' + file_ext
        get_main_text = main_text.get(1.0, END)
        create_write_file = open(full_name, 'w')
        create_write_file.write(get_main_text)
        create_write_file.close()
        filename_Label.config(text=full_name)
        save_as_window.destroy()

    save_as_window = Tk()
    save_as_window.title('Save File')
    save_as_window.config(bg='#231955', padx=0)

    file_name_label = Label(save_as_window, text='File Name: ', bg='#1F4690', fg='#FFE5B4', width=9, height=1)
    file_name_label.config(font=main_text_font, padx=0)
    file_name_label.grid(row=0, column=0)

    file_extension_label = Label(save_as_window, text='File Ext: ', bg='#1F4690', fg='#FFE5B4', width=9, height=1)
    file_extension_label.config(font=main_text_font, padx=0)
    file_extension_label.grid(row=0, column=1)

    file_name_entry = Entry(save_as_window, bg='#231955', fg='#FFE5B4', width=9)
    file_name_entry.config(font=main_text_font)
    file_name_entry.grid(row=1, column=0)

    file_extension_entry = Entry(save_as_window, bg='#231955', fg='#FFE5B4', width=9)
    file_extension_entry.config(font=main_text_font)
    file_extension_entry.grid(row=1, column=1)

    save_file_button = Button(save_as_window, text='Save', bg='#1F4690', fg='#FFE5B4', height=1)
    save_file_button.config(font=main_text_font, padx=0, command=save)
    save_file_button.grid(row=2, column=0, columnspan=2, sticky=E + W)

    save_as_window.resizable(False, False)
    save_as_window.geometry('200x100')
    save_as_window.mainloop()


def load_window():
    def load():
        try:
            read = open(file_entry.get(), 'r')
        except:
            error_label.config(text='can\'t find file with this name')
        else:
            file_information = read.read()
            main_text.delete(1.0, END)
            main_text.insert(1.0, file_information)
            filename_Label.config(text=file_entry.get())
            load_file_window.destroy()

    load_file_window = Tk()
    load_file_window.title('Load File')

    load_file_frame = Frame(load_file_window, bg='#231955', width=200, height=100)
    load_file_frame.place(x=0, y=0)
    file_label = Label(load_file_window, text='File Name: ', bg='#1F4690', fg='#FFE5B4', width=9, height=1)
    file_label.config(font=main_text_font, padx=0)
    file_label.pack(anchor=CENTER)

    file_entry = Entry(load_file_window, bg='#231955', fg='#FFE5B4', width=9)
    file_entry.config(font=main_text_font)
    file_entry.pack(anchor=CENTER)

    load_file_button = Button(load_file_window, text='Load', bg='#1F4690', fg='#FFE5B4', height=1)
    load_file_button.config(font=main_text_font, padx=0, command=load)
    load_file_button.pack(anchor=CENTER)

    error_label = Label(load_file_window, text='', bg='#1F4690', fg='#FFE5B4', height=1)
    error_label.pack(anchor=CENTER)

    load_file_window.resizable(False, False)
    load_file_window.geometry('200x100')
    load_file_window.mainloop()


master = Tk()
master.title('LearnPythonWithFarzan')

main_text_font = Font(family='slab serif', size=18)
toolbar_frame = Frame(master, bg='#231955', height=35)
toolbar_frame.pack(fill=X)

save_button = Button(master, text='Save', command=save_window)
save_button.config(height=1, width=2, bg='#1F4690', fg='#FFE5B4')
save_button.place(x=0, y=0)

load_button = Button(master, text='Load', command=load_window)
load_button.config(height=1, width=2, bg='#1F4690', fg='#FFE5B4')
load_button.place(x=48, y=0)

filename_Label = Label(master, text='')
filename_Label.config(height=2, bg='#1F4690', fg='#FFE5B4')
filename_Label.place(x=96, y=0)

main_text = Text(master, bg='#231955', fg='#FFE5B4', font=main_text_font, height=1000)
main_text.pack(fill=X)

master.geometry('300x300')
master.mainloop()
