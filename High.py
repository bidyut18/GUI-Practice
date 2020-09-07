import tkinter as tk
from tkinter import filedialog, Text
import os


class FileOpener(tk.Tk):
    Apps = []
    if os.path.isfile('Textfile.txt'):
        with open('Textfile.txt') as f:
            tempapps = f.read()
            tempapps = tempapps.split(',')
            Apps = [x for x in tempapps if x.strip()]

    def __init__(self):
        super().__init__()
        self.canvas = tk.Canvas(self, height=500, width=500, bg="#1efca4")
        self.canvas.pack()
        self.frame = tk.Frame(self, bg="white")
        self.frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)
        self.btn1 = tk.Button(self,
                              text='Open file',
                              padx=10,
                              pady=5,
                              fg='White',
                              bg='#263D42',
                              command=self.addapp)
        self.btn1.pack(side='bottom')
        self.btnrun = tk.Button(self,
                                text='Run apps',
                                padx=10,
                                pady=5,
                                fg='White',
                                bg='#263D42',
                                command=self.runapp)
        self.btnrun.pack(side='bottom')

        for app in self.Apps:
            label = tk.Label(self.frame, text=app, bg='gray')
            label.pack()

    def addapp(self):
        for widget in self.frame.winfo_children():
            widget.destroy()
        filename = filedialog.askopenfilename(initialdir='/',
                                              title='Select File',
                                              filetypes=(('executables',
                                                          '.exe'), ('Images',
                                                                    '.jpg'),
                                                         ('all files', '*.*')))
        self.Apps.append(filename)
        for app in self.Apps:
            label = tk.Label(self.frame, text=app, bg='gray')
            label.pack()
        if len(filename) != 0:
            print(f'I am going to open {filename}')

    def runapp(self):
        for app in self.Apps:
            os.startfile(app)


if __name__ == "__main__":
    app = FileOpener()
    app.title('File Manager')
    app.resizable(False, False)
    app.attributes('-alpha', 0.9)
    app.mainloop()

with open('Textfile.txt', 'w') as f:
    for app in FileOpener.Apps:
        f.write(app + ',')