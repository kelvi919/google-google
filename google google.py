from tkinter import *
import webbrowser

def button_click():
    """A function that handles the opening of the browser"""
    google_url = "http://www.google.com"

    # use your chrome file location for this to work
    webbrowser.open_new_tab(google_url)

root = Tk()
root.title("google introduction")

# setting up the window 
canvas = Canvas(root, height=100, width=300)

# text ontop of the google button
label = Label(root, text="what happens if you google google?", fg="black", font="Arial",)
label.pack()

# creating the button
google_button = Button(root, text="Google google", font=("Arial", 20), command=button_click, bg="grey")
google_button.pack(pady=30)


canvas.pack()
root.mainloop()
