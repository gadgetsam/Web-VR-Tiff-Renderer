from flask import Flask, render_template
app = Flask(__name__)
import tkinter as tk
from tkinter import filedialog
import urllib



@app.route('/')
def homepage():
    return render_template('index.html')
@app.after_request
def add_header(r):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers['Cache-Control'] = 'public, max-age=0'
    return r
def start():
    app.run(debug=False, use_reloader=False, port=8080)






if __name__ == "__main__":
    app.run(debug=True, use_reloader=True, port=8080)