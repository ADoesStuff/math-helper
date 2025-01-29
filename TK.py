from tkinter import *
from tkinter import ttk
import random
import time

god_damned_number_1 = random.randint(1, 10)
god_damned_number_2 = random.randint(1, 10)

def shitty_func():
    god_damned_number_1= random.randint(1, 10)
    god_damned_number_2= random.randint(1, 10)
    god_damned_label.config(text=f"{god_damned_number_1}*{god_damned_number_2}")





def crap():
    god_damned_answer = int(thing.get())
    if god_damned_answer == god_damned_number_1*god_damned_number_2:
        god_damned_label_2.config(text="correct", foreground="green")
    else:
        god_damned_label_2.config(text="wrong", foreground="red")





this = Tk()
this.title("shiii")
this.geometry("300x150")



god_damned_label = Label(this, text=f"{god_damned_number_1}*{god_damned_number_2}")
god_damned_label.pack()


god_damned_label_2 = Label(this, text="this label will show if your answer was correct")
god_damned_label_2.pack()




nikon = PhotoImage(file="v1-ultrakill.png")
this.iconphoto(True, nikon)





buttone = Button(this, text="submit your answer :D", command=crap)
buttone.pack(side = BOTTOM)

buttone_2 = Button(this, text="new question", command=shitty_func)
buttone_2.pack(side = BOTTOM)


thing = Entry()
thing.pack()


this.mainloop()