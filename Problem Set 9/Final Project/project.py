from tkinter import Label, Button, StringVar, IntVar, Tk
from tkinter import messagebox
import random



# Function to count down the time
def countdown(time_left):
    if time_left > 0:
        mins, secs = divmod(time_left, 60) #divmod returns the quotient and the remainder
        time_format = '{:02d}:{:02d}'.format(mins, secs)

        if time_left <= 30 and time_left > 20:
            countdown_label.config(text=time_format, fg="#Ffff00")
        elif time_left <= 20 and time_left > 10:
            countdown_label.config(text=time_format, fg="#Ffa500")
        elif time_left <= 10:
            countdown_label.config(text=time_format, fg="#Ff0000")
        else:
            countdown_label.config(text=time_format, fg="#008000")

        clock.after(1000, countdown, time_left - 1) #update the time left every second
    else:
        activity = activity_var.get() #get the selected activity from the user
        pop_up(activity)

# Function to set the timer
def set_timer():
    total_time = timer_var.get() #get the total time from the user
    countdown(total_time * 60)
    start_button.config(state="disabled")


# Function to reset the timer
def reset():
    clock.after_cancel(countdown)
    activity_var.set(None)
    timer_var.set(None)
    countdown_label.config(text="00:00")
    countdown(0)
    #reset the buttons
    start_button.config(state="normal")
    for button in activity_buttons:
        button.config(state="normal")
    for button in timer_buttons:
        button.config(state="normal")


# Function to randomly change the button color
def change_button_color(button):
    hexadecimal = ["#" + ''.join([random.choice("ABCDEF0123456789") for _ in range(6)])]
    button.config(bg=hexadecimal)


# Function to randomly change the font color
def change_font_color(font):
    hexadecimal = ["#" + ''.join([random.choice("ABCDEF0123456789") for _ in range(6)])]
    font.config(fg=hexadecimal)


# Function to pop up a message box after the timer ends for each activity type
def pop_up(activity):
    if activity == "BATH\nTIME":
        messagebox.showinfo("Oh noo!", "Bath time is over!\nTime to get out of the tub!\n🛁🐥🤗👍")
    elif activity == "PLAY\nTIME":
        messagebox.showinfo("Oh noo!", "Play time is over!\nTime to clean up your toys!\n🪀🧩🚗🧸")
    elif activity == "TV\nTIME":
        messagebox.showinfo("Oh noo!", "TV time is over!\nTime to turn off the TV!\n📺📺📺📺")
    elif activity == "MEAL\nTIME":
        messagebox.showinfo("Oh noo!", "Meal time is over!\nTime to clean up your plate!\n🧼🧽🧼🍽️")
    elif activity == "NAP\nTIME":
        messagebox.showinfo("Oh noo!", "It's time for your nap!\n😴😴😴😴\nSweet dreams.")


# Main function
def main():
    global clock
    global countdown_label
    font_name = "comic sans ms"
    label_color = "#e1c0b6"
    clock = Tk()
    clock.geometry("800x800")
    clock.title("TODDLER FUN TIMER")
    clock.resizable(1, 1)
    clock["bg"] = "#e1c0b6"
    clock.columnconfigure(0, weight=2)
    clock.columnconfigure(1, weight=2)
    clock.columnconfigure(2, weight=2)
    clock.columnconfigure(3, weight=2)
    clock.columnconfigure(4, weight=2)
    clock.rowconfigure(0, weight=2)
    clock.rowconfigure(1, weight=4)
    clock.rowconfigure(3, weight=2)
    clock.rowconfigure(4, weight=4)
    clock.rowconfigure(5, weight=1)
    clock.rowconfigure(7, weight=2)
    clock.rowconfigure(8, weight=4)


    # Activity selection buttons and label configuration
    global activity_var
    activity_var = StringVar(value=None)
    activity_label = Label(clock, text="What are we doing?", font=(font_name, 16), bg=label_color)
    change_font_color(activity_label)
    activity_label.grid(row=0, column=0, columnspan=5, pady=(10, 0))
    activities = ["BATH\nTIME", "PLAY\nTIME", "TV\nTIME", "MEAL\nTIME", "NAP\nTIME"]


    # Create buttons for each activity
    global activity_buttons
    activity_buttons = []
    for i, interval in enumerate(activities):
        activity_button = Button(clock, text=interval, font=(font_name, 16), command=lambda interval=interval: activity_var.set(interval))
        activity_button.grid(row=1, column=i, sticky="nsew")
        change_button_color(activity_button)
        activity_buttons.append(activity_button)  # Add each button to the activity_buttons list

    # Function to disable the activity button after the user selects an activity
    def disable_activity_button(*args):
        for button in activity_buttons:
            if activity_var.get() is not None:
                button.config(state="disabled")
            else:
                button.config(state="normal")
    activity_var.trace_add("write", disable_activity_button)



    # Timer interval selection buttons and label configuration
    global timer_var
    timer_var = IntVar(value=None)
    timer_label = Label(clock, text="How many minutes?", font=(font_name, 16), bg=label_color)
    change_font_color(timer_label)
    timer_label.grid(row=3, column=0, columnspan=5, pady=(10, 0))
    timer_intervals = [1, 2, 3, 4, 5]


    # Create buttons for each timer interval
    global timer_buttons
    timer_buttons = []
    for i, interval in enumerate(timer_intervals):
        timer_button = Button(clock, text=str(interval), font=(font_name, 16), command=lambda interval=interval: timer_var.set(interval))
        timer_button.grid(row=4, column=i, sticky="nsew")
        change_button_color(timer_button)
        timer_buttons.append(timer_button)  # Add each button to the timer_buttons list

    # Function to disable the timer button after the user selects a timer interval
    def disable_timer_button(*args):
        for button in timer_buttons:
            if timer_var.get() is not None:
                button.config(state="disabled")
            else:
                button.config(state="normal")
    timer_var.trace_add("write", disable_timer_button)



    # Start button configuration
    global start_button
    start_button = Button(clock, text="Start!", font=(font_name, 16), command=set_timer, state="disabled")
    start_button.grid(row=7, column=1, columnspan=3, sticky = "nsew")
    change_button_color(start_button)

    # Function to enable the start button after the user selects an activity and a timer interval
    def enable_start_button(*args):
        if activity_var.get() is not None and timer_var.get() in [1, 2, 3, 4, 5]:
            start_button.config(state="normal")
        else:
            start_button.config(state="disabled")

    # Bind the function to changes in activity_var and timer_var
    activity_var.trace_add("write", enable_start_button)
    timer_var.trace_add("write", enable_start_button)


    # Countdown label configuration
    countdown_label = Label(clock, text="00:00", font=(font_name, 120), bg=label_color)
    countdown_label.grid(row=8, column=0, columnspan=5, sticky="ns")


    # Reset button configuration
    reset_button = Button(clock, text="Reset", font=(font_name, 16), command=reset)
    reset_button.grid(row=10, column=4, columnspan=2, sticky="ew")
    change_button_color(reset_button)


    # Run the main loop
    clock.mainloop()

# Run the main function
if __name__ == "__main__":
    main()
