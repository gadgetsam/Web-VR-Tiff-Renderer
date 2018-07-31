from readTiff import readTiff
import tkinter as tk
from main import start
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

file_path = filedialog.askopenfilename()
readTiff(file_path)
start()
