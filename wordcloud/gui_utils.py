# Import libaries
import tkinter as tk
from tkinter import filedialog, simpledialog

# Function that asks user for output file location
def get_output_filepath_from_dialog(input_prompt):
    result = filedialog.asksaveasfilename(title=input_prompt, filetypes=[('Excel files', '*.xlsx')], defaultextension='.xlsx')
    if result is None:
        raise ValueError("Input not provided. Exiting.")
    return result 

# Dialog for multiple text inputs (can be string, int, float, etc.)
class MultiInputDialog(simpledialog.Dialog):
    def body(self, master):
        tk.Label(master, text="Reddit post link:").grid(row=0)
        tk.Label(master, text="Word cloud random state:").grid(row=1)
        tk.Label(master, text="Figure size length:").grid(row=2)
        tk.Label(master, text="Figure size width:").grid(row=3)

        self.entry1 = tk.Entry(master)
        self.entry2 = tk.Entry(master)
        self.entry3 = tk.Entry(master)
        self.entry4 = tk.Entry(master)

        self.entry1.grid(row=0, column=1)
        self.entry2.grid(row=1, column=1)
        self.entry3.grid(row=2, column=1)
        self.entry4.grid(row=3, column=1)

        return self.entry1

    def apply(self):
        input1 = self.entry1.get()
        input2 = self.entry2.get()
        input3 = self.entry3.get()
        input4 = self.entry4.get()
        
        self.result = (input1, int(input2), float(input3), float(input4))