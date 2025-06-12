import tkinter as tk
from tkinter import * 
from tkinter import ttk
from tkinter import filedialog
from generator import Generator



class UI(tk.Frame):

    def __init__(self):
        self.root = tk.Tk()
        super().__init__(self.root)
        self.mainframe = ttk.Frame(self.root, padding ="3 3 12 12")
        self.mainframe.grid(column=0, row = 0, sticky=("N", "W", "E", "S"))
        self.root.columnconfigure(0, weight = 1)
        self.root.rowconfigure(0,weight=1)

        self.words = ["Please generate words.", "You can assign wanted parameters in the fields to the right."]        
        self.filename = "Please select a file"
        
        self.input_frames()
        self.results_frame()

        for child in self.mainframe.winfo_children(): 
            child.grid_configure(padx=5, pady=5)



    def results_frame(self):

        # Parent frame for results view
        results_frame = ttk.Frame(self.mainframe, padding="3 3 12 12")
        results_frame.columnconfigure(0, weight=1)
        results_frame.rowconfigure(0,weight=1)


        # Textbox to contain generated words
        text = Text(results_frame)

        for word in self.words:
            text.insert(END, word+"\n")

        text.pack()
        
        results_frame.grid(column=2,row=1)


    def input_frames(self):

        # Parent frame for the input fields, parameters & run controls
        self.input_frame = ttk.Frame(self.mainframe,padding="3 3 12 12")
        self.input_frame.columnconfigure(0, weight=1)
        self.input_frame.rowconfigure(0,weight=1)

        # Call to create parameter panel
        self.parameter_panel_widget(self.input_frame)
        
        self.training_widget()

        #Call to create operating panel
        self.control_panel_widget(self.input_frame)
        
        self.set_grids(self.input_frame)

        self.input_frame.grid(column=1, row=1)




    def control_panel_widget(self,frame):
        control_frame = ttk.Frame(frame)
        control_frame.columnconfigure(0, weight=1)
        control_frame.rowconfigure(0, weight=1)

        ttk.Label(control_frame, text="Control panel widget").grid(column=0,row=0)

        ttk.Button(control_frame, text="Save results",command=self.save_output).grid(column=0,row=1)

        ttk.Button(control_frame, text="Run generation", command=self.run_generation).grid(column=1,row=1)

        self.set_grids(control_frame)
        #TODO: Add field to show currently trained on file

    
    
    def run_generation(self):
        #TODO: separate generation and training so user can generate multiple lists if wanted
        
        self.generator = Generator(self.filename, int(self.degrees.get()), int(self.word_length.get()))
        self.generator.train()

        self.words = self.generator.generate(int(self.n.get()))

        self.results_frame()


    def save_output(self):
        print("This will save the output")        


    def select_training_file(self):
        # TODO: need to separate input_frames() from training file selection to update the frame without losing parameters
        filename = filedialog.askopenfilename()

        self.filename = filename
        self.training_widget()
        

    def training_widget(self):
        training_frame = ttk.Frame(self.input_frame)
        training_frame.columnconfigure(0,weight=1)
        training_frame.rowconfigure(0,weight=1)

        ttk.Button(training_frame, text="Select training file",command=self.select_training_file).grid(column=0,row=1)
        
        self.label_text = StringVar()
        self.label_text.set(self.filename)

        ttk.Label(training_frame, textvariable=self.label_text).grid(column=0,row=2)

        self.set_grids(training_frame)
        training_frame.grid(column=0,row=1)


    def parameter_panel_widget(self,frame):

        # Create parent frame for parameter panel
        parameter_frame = ttk.Frame(frame)
        parameter_frame.columnconfigure(0, weight=1)
        parameter_frame.rowconfigure(0, weight=1)

        ttk.Label(parameter_frame, text="Parameter widget thing").grid()

        # Assign label and entry field to degree selection
        ttk.Label(parameter_frame, text="Degree: ").grid(column=0,row=1)
        self.degrees = StringVar()
        degree_entry = ttk.Entry(parameter_frame, width=5, textvariable=self.degrees)
        degree_entry.grid(column=1,row=1)

        # Assign label and entry field to word length selection
        ttk.Label(parameter_frame,text="Test").grid(column=0, row=2)
        self.word_length= StringVar()
        length_entry = ttk.Entry(parameter_frame, width=5, textvariable=self.word_length)
        length_entry.grid(column=1,row=2)

        # Assign label and entry field for word amount selection
        ttk.Label(parameter_frame, text="Words to generate:").grid(column=0,row=3)
        self.n = StringVar()
        n_entry = ttk.Entry(parameter_frame, width = 5, textvariable = self.n)
        n_entry.grid(column=1,row=3)

        #ttk.Button(parameter_frame, text="Select training file",command=self.select_training_file).grid(column=0,row=4)
        #ttk.Label(parameter_frame, text=self.filename).grid(column=1,row=4)
        

        # Populate the frames
        self.set_grids(parameter_frame)
        parameter_frame.grid(column=0, row=2)

    def set_grids(self,frame):
        # Function to run through widget children and packing them into the grid
        for child in frame.winfo_children():
            child.grid_configure(padx=2,pady=2)


    def run(self):
        self.mainloop()
        


app = UI()

app.run()