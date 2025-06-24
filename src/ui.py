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

        # Set default value in results window to instructions on how to use.
        self.words = ["Please generate words.", "Select you training file first, any UTF-8 .txt file will do.",
                        "You can assign wanted parameters in the fields to the right.",
                        "Please press train to populate the trie.", "Press run generation to create new words."]        
        self.filename = "Please select a file"

        self.degrees = StringVar()
        self.degrees.set(2) # Default Markov chain degree

        self.word_length = StringVar()
        self.word_length.set(8) # Default word length to generate

        self.n = StringVar()
        self.n.set(15) # Default amount of words to generate
        
        # Create separate frames for input (left side) and
        # results (right side)
        self.input_frames()
        self.results_frame()

        # set_grids() is a class method to use grid.configure
        # for all children of the frame.
        self.set_grids(self.mainframe)


    # UI structure functions
    def results_frame(self):
        '''
            Widget contains the right hand side of the UI, i.e. the results panel.
        '''
        # Parent frame for results view
        results_frame = ttk.Frame(self.mainframe, padding="3 3 12 12")
        results_frame.columnconfigure(0, weight=1)
        results_frame.rowconfigure(0,weight=1)

        # Textbox to contain generated words
        text = Text(results_frame)

        for word in self.words:
            text.insert(END, word+"\n")

        text.pack() # Pack the words into the textbox
        
        results_frame.grid(column=2,row=1)


    def input_frames(self):
        '''
            Contains the control widgets for generation, i.e. the left hand side of the UI.
        '''
        # Parent frame for the input fields, parameters & run controls
        self.input_frame = ttk.Frame(self.mainframe,padding="3 3 12 12")
        self.input_frame.columnconfigure(0, weight=1)
        self.input_frame.rowconfigure(0,weight=1)
        
        #Call to create training operations widget
        self.training_widget()

        # Call to create parameter panel
        self.parameter_panel_widget(self.input_frame)

        #Call to create operating panel
        self.control_panel_widget(self.input_frame)
        
        self.set_grids(self.input_frame)

        self.input_frame.grid(column=1, row=1)


    # Input frame widgets
    def training_widget(self):
        '''
            Widget to contain training file selection.
        '''
        # Separating the widget from parameter selection allows the UI
        # to refresh without resetting the parameter input fields.

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
        '''
            Widget contains parameter panel. Used to take user input.
        '''
        # Create parent frame for parameter panel
        parameter_frame = ttk.Frame(frame)
        parameter_frame.columnconfigure(0, weight=1)
        parameter_frame.rowconfigure(0, weight=1)

        # Assign label and entry field to degree selection
        ttk.Label(parameter_frame, text="Markov chain degree: ").grid(column=0,row=1)
        degree_entry = ttk.Entry(parameter_frame, width=5, textvariable=self.degrees)
        degree_entry.grid(column=1,row=1)

        # Assign label and entry field to word length selection
        ttk.Label(parameter_frame,text="Word length").grid(column=0, row=2)
        length_entry = ttk.Entry(parameter_frame, width=5, textvariable=self.word_length)
        length_entry.grid(column=1,row=2)

        # Assign label and entry field for word amount selection
        ttk.Label(parameter_frame, text="Word amount to generate:").grid(column=0,row=3)
        n_entry = ttk.Entry(parameter_frame, width = 5, textvariable = self.n)
        n_entry.grid(column=1,row=3)

        ttk.Button(parameter_frame, text="Train", command=self.train).grid(column=0, row=4)

        # Populate the frames
        self.set_grids(parameter_frame)
        parameter_frame.grid(column=0, row=2)
    
    
    def control_panel_widget(self,frame):
        '''
            Widget for operating saving and running word generation.
        '''
        control_frame = ttk.Frame(frame)
        control_frame.columnconfigure(0, weight=1)
        control_frame.rowconfigure(0, weight=1)

        ttk.Button(control_frame, text="Save results",command=self.save_output).grid(column=0,row=1)

        ttk.Button(control_frame, text="Run generation", command=self.run_generation).grid(column=1,row=1)

        self.set_grids(control_frame)


    # I/O functions for the UI.
    def save_output(self):
        '''
            Saves generated output to a file in the users system.
        '''
        save_file = filedialog.asksaveasfilename(defaultextension=".txt")

        if save_file == None:
            return
        
        words_to_write = "\n".join(self.words)

        with open(save_file,"w") as file:
            file.write(words_to_write)


    def select_training_file(self):
        '''
            Function to select a file to train on.
        '''
        filename = filedialog.askopenfilename()
        if filename == None:
            return
        
        self.filename = filename
        self.training_widget()


    #Functions to call on underlying app logic.
    def train(self):
        '''
            Calls on Generator class method train() to populate the trie structure.
        '''
        self.generator = Generator(self.filename, int(self.degrees.get()), int(self.word_length.get()))
        self.generator.train()
    

    def run_generation(self):
        '''
            Calls on Generator method generate() to create random words.
        '''
        self.words = self.generator.generate(int(self.n.get()))

        self.results_frame()


    #Help functions
    def set_grids(self,frame):
        '''
            Shorthand function to populate the frame grid.
        '''
        for child in frame.winfo_children():
            child.grid_configure(padx=2,pady=2)


    def run(self):
        '''
            Shorthand function to run the app
        '''
        self.mainloop()