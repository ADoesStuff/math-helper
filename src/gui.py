from tkinter import *

class AppWindow:
    def __init__(self, man):
        self.val_man = man
        self.init_window()
        self.init_gui(self.window)
        self.add_action_listeners()

    def init_window(self):
        self.window = Tk()
        self.window.geometry("100x100")
        #Removed so generated bin runs without needing res/
        #nikon_icon = PhotoImage(file="res/icon.png")
        #self.window.iconphoto(True, nikon_icon)
        self.window.title("Math Helper")

    def init_gui(self, window):
        self.question_label = Label(window)
        self.question_label.pack()
        self.result_label = Label(window)
        self.result_label.pack()
        self.answer_input = Entry()
        self.answer_input.pack()
        self.score_label = Label(window, text="Score: 0")
        self.score_label.pack()
        self.check_answer_button = Button(window, text="Check answer :D")
        self.check_answer_button.pack(side = BOTTOM)
        self.skip_button = Button(window, text="Skip :[")
        self.skip_button.pack(side = BOTTOM)

    def set_visible(self):
        self.next_question()
        self.window.mainloop()

    def add_action_listeners(self):
        self.check_answer_button.config(command=self.check_answer)
        self.skip_button.config(command=self.next_question)

    # Gets two new random numbers and shows question to given label
    def next_question(self):
        vals = self.val_man.randomize()
        txt = f"{vals[0]} x {vals[1]}"
        self.question_label.config(text=txt)

    # Checks ansewr from given input and shows results to given output
    # If question is correct, next answer is shown
    def check_answer(self):
        answer = 0
        try:
            answer = int(self.answer_input.get())
        except:
            answer = 0
        if self.val_man.check(answer):
            self.result_label.config(text="Correct :)", foreground="green")
            self.next_question()
            self.score_label.config(text=f"Score: {self.val_man.get_score()}")
            self.answer_input.delete(0, 'end')
        else:
            self.result_label.config(text="Wrong :(", foreground="red")
