import tkinter as tk
from tkinter import * 
from tkinter import ttk
from generator import Generator


test = Generator("testing/testing.txt", 3, 8)

test.train()

asd = test.generate(5)

#for word in asd:
#    print(word)

class UI(tk.Frame):

    def __init__(self):
        self.root = tk.Tk()
        super().__init__(self.root)
        self.mainframe = ttk.Frame(self.root, padding ="3 3 12 12")
        self.mainframe.grid(column=0, row = 0, sticky=("N", "W", "E", "S"))
        self.root.columnconfigure(0, weight = 1)
        self.root.rowconfigure(0,weight=1)

        self.words = ["Please generate words."]        


        self.test_widget()
        self.results_frame()
        for child in self.mainframe.winfo_children(): 
            child.grid_configure(padx=5, pady=5)



    def results_frame(self):

        results_frame = ttk.Frame(self.mainframe, padding="3 3 12 12")
        results_frame.columnconfigure(0, weight=1)
        results_frame.rowconfigure(0,weight=1)

        TEST = ["Word", "Word", "Word", "Word", "Word", "Word", "Word", "Word", "Ending word"]

        text = Text(results_frame)

        for word in self.words:
            text.insert(END, word+"\n")

        text.pack()
        
        results_frame.grid(column=2,row=1)


    def test_widget(self):

        test_frame = ttk.Frame(self.mainframe,padding="3 3 12 12")
        test_frame.columnconfigure(0, weight=1)
        test_frame.rowconfigure(0,weight=1)

        self.parameter_panel_widget(test_frame)
        self.control_panel_widget(test_frame)
        
        for child in test_frame.winfo_children():
            child.grid_configure(padx=5,pady=5)

        test_frame.grid(column=1, row=1)


    def control_panel_widget(self,frame):
        control_frame = ttk.Frame(frame)
        control_frame.columnconfigure(0, weight=1)
        control_frame.rowconfigure(0, weight=1)

        ttk.Label(control_frame, text="Control panel widget").grid(column=0,row=0)

        ttk.Button(control_frame, text="Save results",command=self.testing_function).grid(column=0,row=1)

        ttk.Button(control_frame, text="Run generation", command=self.testing_function).grid(column=1,row=1)

        self.set_grids(control_frame)

    def testing_function(self):
        self.generator = Generator("testing/testing.txt", int(self.degrees.get()), int(self.word_length.get()))
        self.generator.train()

        self.words = self.generator.generate(int(self.n.get()))

        self.results_frame()


        


    def parameter_panel_widget(self,frame):

        parameter_frame = ttk.Frame(frame)
        parameter_frame.columnconfigure(0, weight=1)
        parameter_frame.rowconfigure(0, weight=1)

        ttk.Label(parameter_frame, text="Parameter widget thing").grid()

        ttk.Label(parameter_frame, text="Degree: ").grid(column=0,row=1)
        self.degrees = StringVar()
        degree_entry = ttk.Entry(parameter_frame, width=5, textvariable=self.degrees)
        degree_entry.grid(column=1,row=1)


        ttk.Label(parameter_frame,text="Test").grid(column=0, row=2)
        self.word_length= StringVar()
        length_entry = ttk.Entry(parameter_frame, width=5, textvariable=self.word_length)
        length_entry.grid(column=1,row=2)

        ttk.Label(parameter_frame, text="Words to generate:").grid(column=0,row=3)
        self.n = StringVar()
        n_entry = ttk.Entry(parameter_frame, width = 5, textvariable = self.n)
        n_entry.grid(column=1,row=3)

        self.set_grids(parameter_frame)

    def set_grids(self,frame):

        for child in frame.winfo_children():
            child.grid_configure(padx=2,pady=2)


    def run(self):
        self.mainloop()
        


    def calculate(self, *args):
        try:
            value = float(self.feet.get())
            self.meters.set(int(0.3048 * value * 10000.0 + 0.5)/10000.0)
        except ValueError:
            pass

app = UI()

app.run()