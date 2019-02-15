import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkinter import filedialog

import csproj_reader

class CSProjReaderGUI(object):
    def __init__(self):
        self.directory = '.'
        self.filename = 'result.csv'

    def run(self):
        win = tk.Tk()
        win.width = 300
        tk.Grid.rowconfigure(win, 0, weight=1)
        tk.Grid.columnconfigure(win, 0, weight=1)

        win.title('csproj.reader')

        dir_title_label = ttk.Label(win, text="working directory:")
        dir_title_label.grid(row=0, column=0, sticky=tk.W+tk.E)

        dir_label = ttk.Label(win, text="", anchor='w')
        dir_label.grid(row=0, column=1, sticky=tk.W+tk.E)

        def do_select_dir():
            self.directory = filedialog.askdirectory()
            dir_label.configure(text=self.directory)

        select_dir_button = ttk.Button(win, text="select directory", command=do_select_dir)
        select_dir_button.grid(row=0, column=2, sticky=tk.W+tk.E)

        file_title_label = ttk.Label(win, text="result file:")
        file_title_label.grid(row=1, column=0, sticky=tk.W+tk.E)

        file_label = ttk.Label(win,  text=self.filename)
        file_label.grid(row=1, column=1, sticky=tk.W+tk.E)

        def do_select_file():
            self.filename = filedialog.asksaveasfilename()
            file_label.configure(text=self.filename)

        select_file_button = ttk.Button(win, text="select file", command=do_select_file)
        select_file_button.grid(row=1, column=2, sticky=tk.W+tk.E)

        def do_process():
            result = csproj_reader.extract_from_directory(self.directory)
            for item in result:
                print(item)
            csproj_reader.write_to_csv(result, self.filename)
            messagebox.showinfo('Process', 'end')

        process_button = ttk.Button(win, text="process", command=do_process)
        process_button.grid(row=2, column=0, columnspan=3, sticky=tk.W+tk.E)

        win.mainloop()