import customtkinter as ctk
ctk.set_appearance_mode("dark")
app = ctk.CTk()
app.geometry("400x400")

label = ctk.CTkLabel(app, text="Hello, CustomTkinter!")
label.pack(pady=20)

button = ctk.CTkButton(app, text="Click Me")
button.pack(pady=20)

button = ctk.CTkButton(app, text="Click Me", command=lambda: print("Button clicked"))
button.pack()

button = ctk.CTkButton(app, text="Click Me", command=lambda: print("Button clicked"))
button.pack()

button = ctk.CTkButton(app, text="Click Me", command=lambda: print("Button clicked"))
button.pack()

button = ctk.CTkButton(app, text="Click Me", command=lambda: print("Button clicked"))
button.pack()

entry = ctk.CTkEntry(app)
entry.pack(pady=20)

app.mainloop()