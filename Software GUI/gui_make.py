import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk
from tkinter import filedialog

# windows
window = ttk.Window()
#window.geometry('800x400')
window.title("DABANA")
window.iconbitmap('D:/Start Ups/Dabana/Code/Sample/icon.ico')

# windows size
window.minsize(700,340)
window_width = 800
window_height = 400
# windows attribute
window.attributes('-alpha', 1)
display_width = window.winfo_screenwidth()
display_height = window.winfo_screenheight()
left = int((display_width/2) - (window_width/2))
top = int((display_height/2) - (window_height/2))
window.geometry(f'{window_width}x{window_height}+{left}+{top}')


def openFileCompress():
    filepath = filedialog.askdirectory(initialdir="C:\\", title="Choose Your Folder")
    print(filepath)


def openFileDeCompress1():
    filepath = filedialog.askopenfilename(initialdir="C:\\", title="Choose Your Folder", filetypes= (("zip files","*.zip"),("all files","*.*")))
    print(filepath)


def openFileDeCompress2():
    filepath = filedialog.askopenfilename(initialdir="C:\\", title="Choose Your Zip File", filetypes= (("zip files","*.zip"),("all files","*.*")))
    print(filepath)


menu_frame = ttk.Frame(master=window)
button_home = ttk.Button(master=menu_frame, text = 'Home', width=25)
button_use = ttk.Button(master=menu_frame, text = 'How to Use', width=25)
button_pricing = ttk.Button(master=menu_frame, text = 'Pricing', width=25)
button_home.pack(side='left', pady=10)
button_use.pack(side='left', pady=10)
button_pricing.pack(side='left', pady=10)
menu_frame.pack()


option_frame = ttk.Frame(master=window)
button_compress = ttk.Button(master=option_frame, text = 'Compress', width=50, command=openFileCompress)

decompress_option_frame = ttk.Frame(master=option_frame)
button_decompress1 = ttk.Button(master=decompress_option_frame, text = 'Decompress Folder', width=23, command=openFileDeCompress1)
button_decompress2 = ttk.Button(master=decompress_option_frame, text = 'Decompress Zip File', width=23, command=openFileDeCompress2)
button_compress.pack(pady=30)
button_decompress1.pack(pady=30, side='left')
button_decompress2.pack(pady=30, side='left')
decompress_option_frame.pack()
option_frame.pack()


button_exit = ttk.Button(master=window, text='Exit', command=window.quit)
button_exit.pack()


disclaimer_label = ttk.Label(master=window, text="By uploading files you agree to our Term of Services.", font='Calibri 8')
disclaimer_label.pack(pady=20)


window.mainloop()
