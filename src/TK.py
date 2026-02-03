from tkinter import *
from random import randint

value1 = 0
value2 = 0

# Gets two new random numbers and shows question to given label
def next_question(question_output):
    # modify global vriables, don't define new onces.
    global value1, value2
    value1 = randint(1, 10)
    value2 = randint(1, 10)
    question_output.config(text=f"{value1} x {value2}")

# Checks ansewr from given input and shows results to given output
# If question is correct, next answer is shown
def check_answer(answer_input, result_output, question_output):
    answer = int(answer_input.get())
    if answer == (value1*value2):
        result_output.config(text="Correct :)", foreground="green")
        next_question(question_output)
        answer_input.delete(0, 'end')
    else:
        result_output.config(text="Wrong :(", foreground="red")
    
def init_gui(window):
    question_label = Label(window)
    question_label.pack()

    result_label = Label(window)
    result_label.pack()

    answer_input = Entry()
    answer_input.pack()

    nikon_icon = PhotoImage(file="res/icon.png")
    window.iconphoto(True, nikon_icon)

    # calls abstract function with correct parameters
    def nextQuestion():
        next_question(question_label)

    # calls abstract function with correct parameters
    def checkAnswer():
        check_answer(answer_input, result_label, question_label)

    check_answer_button = Button(window, text="Check answer :D", command=checkAnswer)
    check_answer_button.pack(side = BOTTOM)

    skip_button = Button(window, text="Skip :[", command=nextQuestion)
    skip_button.pack(side = BOTTOM)

    nextQuestion()

# init and config window
window = Tk()
window.title("Math Helper")
window.geometry("100x80")

init_gui(window)

window.mainloop()