from tkinter import *
from tkinter import filedialog, colorchooser
from PIL import ImageTk
from stegan import stegan
from proj_py.change_filetype import *
from proj_py.eng_watermark import *

import os

s = stegan()


class SteganGUI:
    def __init__(self, master):
        self.root = master
        self.root.config()
        self.root.geometry("800x800")
        self.root.title("A GUI of Steganography")

        words_hidden(self.root)

class words_hidden:
    def __init__(self, master):
        def change_words_show():
            self.words_hidden.destroy()
            words_show(self.root)

        def change_digital_watermark():
            self.words_hidden.destroy()
            digitalwatermark(self.root)

        self.root = master
        self.root.config()
        self.words_hidden = Frame(self.root)
        self.words_hidden.grid()
        go_words_show = Button(self.words_hidden, text="Show hidden words", command=change_words_show)
        go_words_show.grid(row=0)
        go_digital_watermark = Button(self.words_hidden, text="Digital Watermark", command=change_digital_watermark)
        go_digital_watermark.grid(row=0, column=1)

        def fileDialog():
            filename.set(filedialog.askopenfilename(initialdir="/", title="Select file",
                                                    filetypes=(
                                                        ("bmp, wav, png, flac files", "*.bmp *.wav *.png *.flac"),
                                                        ("all files", " *.* "))))
            self.file_name = Entry(self.words_hidden, textvariable=filename, width=40)
            self.file_name.grid(row=2, column=1)

        def hidden():
            s.setinput_password(input_password.get())
            s.setinput(self.input_con.get(1.0, "end-1c"))
            if filename.get().endswith('.bmp'):
                s.bmphidden(filename.get())

            elif filename.get().endswith('wav'):
                s.wavhidden(filename.get())

            elif filename.get().endswith('.png'):
                change(filename.get())
                changed_filename = os.path.splitext(filename.get())[0] + ".bmp"
                s.bmphidden(changed_filename)
                change("Save.bmp")
                os.remove("Save.bmp")
                os.remove(changed_filename)

            elif filename.get().endswith('.flac'):
                change(filename.get())
                changed_filename = os.path.splitext(filename.get())[0] + ".wav"
                s.wavhidden(changed_filename)
                change("Save.wav")
                os.remove("Save.wav")
                os.remove(changed_filename)

            self.file_name.delete(0, END)
            self.input_pass.delete(0, END)
            self.input_con.delete(1.0, END)

        def clear():
            self.file_name.delete(0, END)
            self.input_pass.delete(0, END)
            self.input_con.delete(1.0, END)

        self.top_title = Label(self.words_hidden, text="This is make hidden words GUI!")
        self.top_title.grid(row=1, column=1)

        self.file_browse = Label(self.words_hidden, text="File: ")
        self.file_browse.grid(row=2)

        self.file_name = Entry(self.words_hidden, width=40)
        self.file_name.grid(row=2, column=1)

        filename = StringVar()
        self.browse_button = Button(self.words_hidden, text="Browse", command=fileDialog)
        self.browse_button.grid(row=2, column=2)

        self.top_password = Label(self.words_hidden, text="Password: ")
        self.top_password.grid(row=3)

        input_password = StringVar()
        self.input_pass = Entry(self.words_hidden, textvariable=input_password, width=40)
        self.input_pass.grid(row=3, column=1)

        self.top_content = Label(self.words_hidden, text="Input content: ")
        self.top_content.grid(row=4)

        input_content = StringVar()
        self.input_con = Text(self.words_hidden, width=60, height=20)
        self.input_con.grid(row=4, column=1)

        self.ok_button = Button(self.words_hidden, text="OK", command=hidden)
        self.ok_button.grid(row=4, column=2)

        self.clear_button = Button(self.words_hidden, text="clear", command=clear)
        self.clear_button.grid(row=4, column=3)


class words_show:
    def __init__(self, master):
        def change_words_hidden():
            self.words_show.destroy()
            words_hidden(self.root)

        def change_digital_watermark():
            self.words_show.destroy()
            digitalwatermark(self.root)

        self.root = master
        self.root.config()
        self.words_show = Frame(self.root)
        self.words_show.grid()
        go_words_hidden = Button(self.words_show, text="Make hidden words", command=change_words_hidden)
        go_words_hidden.grid(row=0)
        go_digital_watermark = Button(self.words_show, text="Digital Watermark", command=change_digital_watermark)
        go_digital_watermark.grid(row=0, column=1)

        def fileDialog():
            filename.set(filedialog.askopenfilename(initialdir="/", title="Select file",
                                                    filetypes=(
                                                        ("bmp, wav, png, flac files", "*.bmp *.wav *.png *.flac"),
                                                        ("all files", " *.* "))))
            self.file_name = Entry(self.words_show, textvariable=filename, width=40)
            self.file_name.grid(row=2, column=1)

        def show():
            s.setpassword(input_password.get())
            if filename.get().endswith('.bmp'):
                s.bmpshow(filename.get())

            elif filename.get().endswith('.wav'):
                s.wavshow(filename.get())

            elif filename.get().endswith('.png'):
                change(filename.get())
                changed_filename = os.path.splitext(filename.get())[0] + ".bmp"
                s.bmpshow(changed_filename)
                os.remove(changed_filename)

            elif filename.get().endswith('.flac'):
                change(filename.get())
                changed_filename = os.path.splitext(filename.get())[0] + ".wav"
                s.wavshow(changed_filename)
                os.remove(changed_filename)

            self.get_con.configure(state=NORMAL)
            self.get_con.insert(1.0, s.content)
            self.get_con.configure(state=DISABLED)
            self.file_name.delete(0, END)
            self.input_pass.delete(0, END)

        def clear():
            self.file_name.delete(0, END)
            self.input_pass.delete(0, END)
            self.get_con.configure(state=NORMAL)
            self.get_con.delete(1.0, END)
            self.get_con.configure(state=DISABLED)

        self.top_title = Label(self.words_show, text="This is show hidden words GUI!")
        self.top_title.grid(row=1, column=1)

        self.file_browse = Label(self.words_show, text="File: ")
        self.file_browse.grid(row=2)

        self.file_name = Entry(self.words_show, width=40)
        self.file_name.grid(row=2, column=1)

        filename = StringVar()
        self.browse_button = Button(self.words_show, text="Browse", command=fileDialog)
        self.browse_button.grid(row=2, column=2)

        self.top_password = Label(self.words_show, text="Password: ")
        self.top_password.grid(row=3)

        input_password = StringVar()
        self.input_pass = Entry(self.words_show, textvariable=input_password, width=40)
        self.input_pass.grid(row=3, column=1)

        self.top_content = Label(self.words_show, text="Show hidden content: ")
        self.top_content.grid(row=4)

        self.get_con = Text(self.words_show, width=60, height=20)
        self.get_con.configure(state=DISABLED)
        self.get_con.grid(row=4, column=1)

        self.ok_button = Button(self.words_show, text="OK", command=show)
        self.ok_button.grid(row=3, column=2)

        self.clear_button = Button(self.words_show, text="clear", command=clear)
        self.clear_button.grid(row=3, column=3)


class digitalwatermark:
    def __init__(self, master):
        def change_words_hidden():
            self.water_mark.destroy()
            words_hidden(self.root)

        def change_words_show():
            self.water_mark.destroy()
            words_show(self.root)

        self.root = master
        self.root.config()
        self.water_mark = Frame(self.root)
        self.water_mark.grid()
        go_words_show = Button(self.water_mark, text="Show hidden words", command=change_words_show)
        go_words_show.grid(row=7)
        go_words_hidden = Button(self.water_mark, text="Make hidden words", command=change_words_hidden)
        go_words_hidden.grid(row=8)

        # Browse file
        self.filename = None

        def fileDialog():
            try:
                self.filename = StringVar()
                File = filedialog.askopenfilename(initialdir="/", title="Select file",
                                                  filetypes=(
                                                      ("bmp, png files", "*.bmp *.png"),
                                                      ("all file", " *.* ")
                                                  ))
                self.filename.set(File)
                self.file_name = Entry(self.water_mark, textvariable=self.filename, width=50)
                self.file_name.grid(row=6, column=0, padx=5, pady=5)

                self.original = Image.open(File)
                self.original = self.original.resize((500, 500))  # resize image
                self.img = ImageTk.PhotoImage(self.original)
                self.XY.create_image(0, 0, image=self.img, anchor="nw")  # add係左上
            except:
                print("Please select an image")

        self.pos = None

        def getlocation(image):
            self.pos = (image.x, image.y)

        self.rgb = None
        self.hx = None

        def colorpicker():
            (self.rgb, self.hx) = colorchooser.askcolor()

        # OK
        def print_all():
            water_mark(self.filename.get(), self.text.get(),
                       self.pos, self.clicked_type.get(),
                       self.clicked_size.get(), self.rgb,
                       self.clicked_bold.get()
            )

        # Show address
        self.file_name = Entry(self.water_mark, width=50)
        self.file_name.grid(row=6, column=0, padx=5, pady=5)

        self.browse_button = Button(self.water_mark, text="Browse", command=fileDialog)
        self.browse_button.grid(row=6, column=0, padx=15, pady=15, sticky=W)

        # textarea for watermark
        self.text_label = Label(self.water_mark, text="Watermark text")
        self.text_label.grid(row=0, column=2, padx=5, pady=5, sticky=W)

        self.text = StringVar()
        self.text_area = Entry(self.water_mark, width=30, textvariable=self.text)
        self.text_area.grid(row=1, column=2, padx=20, sticky=N)

        # drop down box (TextType)
        self.type_label = Label(self.water_mark, text="Text Type")
        self.type_label.grid(row=2, column=2, padx=5, pady=5, sticky=NW)
        options_type = [
            "1",
            "2",
            "3",
            "4",
            "5",
            "6",
            "7",
            "8",
            "9",
            "10"
        ]
        self.clicked_type = StringVar()
        self.clicked_type.set(options_type[0])
        self.drop_type = OptionMenu(self.water_mark, self.clicked_type, *options_type)
        self.drop_type.grid(row=2, column=2, padx=5, pady=5, sticky=W)

        # drop down box (TextSize)
        self.size_label = Label(self.water_mark, text="Text Size")
        self.size_label.grid(row=3, column=2, padx=5, pady=5, sticky=NW)
        options_size = [
            "1",
            "2",
            "3",
            "4",
            "5",
            "6",
            "7",
            "8",
            "9",
            "10"
        ]
        self.clicked_size = StringVar()
        self.clicked_size.set(options_size[0])
        self.drop_size = OptionMenu(self.water_mark, self.clicked_size, *options_size)
        self.drop_size.grid(row=3, column=2, padx=5, pady=5, sticky=W)

        # drop down box (Text Weight)
        self.weight_label = Label(self.water_mark, text="Text Weight")
        self.weight_label.grid(row=4, column=2, padx=5, pady=5, sticky=NW)
        options_bold = [
            "1",
            "2",
            "3",
            "4",
            "5",
            "6",
            "7",
            "8",
            "9",
            "10"
        ]
        self.clicked_bold = StringVar()
        self.clicked_bold.set(options_bold[0])
        self.drop_bold = OptionMenu(self.water_mark, self.clicked_bold, *options_bold)
        self.drop_bold.grid(row=4, column=2, padx=5, pady=5, sticky=W)

        # Determin the X, Y by clicking
        # setting up a tkinter window
        self.XY = Canvas(self.water_mark, width=500, height=500, bg='grey')
        self.XY.grid(row=0, column=0, rowspan=6, padx=15, pady=15)

        # MouseClick event
        self.XY.bind("<Button 1>", getlocation)

        # ColorPicker
        self.color_button = Button(self.water_mark, text="Pick a Color", command=colorpicker)
        self.color_button.grid(row=5, column=2, padx=5, pady=5, sticky=W)

        # Print all data button
        self.ok_button = Button(self.water_mark, text="OK", command=print_all)
        self.ok_button.grid(row=6, column=2, padx=15, pady=15, sticky=NSEW)


root = Tk()
SteganGUI(root)
root.mainloop()
