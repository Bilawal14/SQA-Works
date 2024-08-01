from tkinter import*

def clicl_me():
    print(i.get())

root = Tk()

i = StringVar()
c1 = Checkbutton(root, text="item 1", variable=i, offvalue="unchecked", onvalue="checked")
c2 = Checkbutton(root, text="item 2", variable=i, offvalue="unchecked")

c1.pack()
c2.pack()

button = Button(root, text="click me", command=clicl_me)
button.pack()
root.geometry("300x300+120+120")
root.mainloop()