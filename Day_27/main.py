import tkinter

window = tkinter.Tk()
window.title("GUI Program")
window.geometry("500x500")
window.minsize(width=300, height=300)

# Label
my_label = tkinter.Label(text="Label", font=("Arial", 24, "bold"))
my_label.pack()


def click():
    my_label.config(text="Button Clicked")


button = tkinter.Button(text="Click me", command=click)
button.pack()

entry = tkinter.Entry(width=10)
entry.pack()

window.mainloop()
