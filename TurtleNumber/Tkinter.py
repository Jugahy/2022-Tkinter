import tkinter

window = tkinter.Tk()


def createNewWindow():
    window.destroy()
    SecondWindow = tkinter.Tk()


buttonExample = tkinter.Button(window,
                               text="Create new window",
                               command=createNewWindow)
buttonExample.pack()

window.mainloop()