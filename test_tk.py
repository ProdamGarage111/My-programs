import tkinter
root = tkinter.Tk()
def get_entry_data():
    entry_data = entry.get()
    print(entry_data)
def on_button_click():
    label.config(text="Button clicked!")
root.title("My Tkinter App")
root.geometry("400x300")
label = tkinter.Label(root, text="Hello, Tkinter!")
label.pack()
button = tkinter.Button(root, text="Click Me", command=get_entry_data)
button.pack()
entry = tkinter.Entry(root)
entry.pack()
root.mainloop()
