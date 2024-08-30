from tkinter import *
#from control import Controls
from Engine import UI


class Window:
    def __init__(self, master):
        self.master = master
        self.master.title('ToC The Game! V1')
        self.master.geometry('1200x300')
        self.master.configure(bg='#fff6e0')

        u = UI(self.master)
        u.update()


    

root = Tk()
win = Window(root)
#root.after(0, Window.update(win))
root.mainloop()
