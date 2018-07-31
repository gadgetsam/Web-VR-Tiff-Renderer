from flask import Flask, render_template
app = Flask(__name__)
import tkinter as tk
from tkinter import filedialog
import urllib



@app.route('/')
def homepage():
    return render_template('index.html')

def start():
    app.run(debug=True, use_reloader=False, port=80)





