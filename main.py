from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps =0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(text_timer, text ="00:00")
    label.config(text="Timer", fg=GREEN)
    check_box.config(text="")
    global reps
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- #

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global timer
    minutes = math.floor(count / 60)
    seconds = count % 60
    if count >=0:
        if seconds <= 9:
            seconds = f"0{seconds}"

        canvas.itemconfig(text_timer, text = f"{minutes}:{seconds}")
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer()
        mark = ""
        work_sessions = math.floor(reps/2)
        for t in range(work_sessions):
            mark += "✔"
        check_box.config(text=mark)


def start_timer():
    global reps
    reps+=1

    work_sec = WORK_MIN*60
    short_break_sec = SHORT_BREAK_MIN*60
    long_break_sec = LONG_BREAK_MIN*60
    if reps%2 == 0:
        if reps%8 ==0:
            count_down(long_break_sec)
            label.config(text="Break", fg= RED)
        else:
            count_down(short_break_sec)
            label.config(text="Break", fg = PINK)
    else:
        count_down(work_sec)
        label.config(text="Work", fg=GREEN)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50, bg= YELLOW)



#Timer
label = Label(text="Timer",bg=YELLOW, font=("Courier",20,"bold"),fg=GREEN)
label.grid(column=1, row = 0)

#Checkbox
# c1 = Checkbutton(window, onvalue=1, offvalue=0,)
# c1.grid(column = 1,row=3)
check_box = Label(fg=GREEN, bg=YELLOW)
check_box.grid(column = 1,row=3)


canvas = Canvas(width=200, height=224, bg=YELLOW ,highlightthickness=0)
photo_img = PhotoImage(file="tomato.png")
canvas.create_image(100,112, image=photo_img)
text_timer = canvas.create_text(100,130, text="00:00", fill="white", font=("Courier", 35,"bold"))
canvas.grid(column = 1, row = 1)

#Button to start
button1 = Button(text="Start",highlightthickness=0,command=start_timer )
button1.grid(column =0,row =2)

#Button to reset
button2 = Button(text="Reset",highlightthickness=0, command=reset_timer)
button2.grid(column = 2,row =2)

window.mainloop()