from tkinter import *
import webbrowser

def button_click():
    """A function that handles the opening of the browser"""
    google_url = "https://www.google.com/search?q=what+happens+if+i+google+google&rlz=1C1CHBD_deDE975DE975&sxsrf=APq-WBt-2OM4liygKi-1KT30481AV4N3wQ%3A1644866162363&ei=cqoKYrXjFaar9u8PztaO2AQ&ved=0ahUKEwi15L368__1AhWmlf0HHU6rA0sQ4dUDCA8&uact=5&oq=what+happens+if+i+google+google&gs_lcp=Cgdnd3Mtd2l6EAMyBQgAEIAEMgYIABAWEB4yBggAEBYQHjoHCAAQRxCwAzoICAAQgAQQsAM6BAgjECdKBQg8EgExSgQIQRgASgQIRhgAUKYGWNAVYLUWaAFwAXgAgAFZiAGPBJIBATeYAQCgAQHIAQnAAQE&sclient=gws-wiz"

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
