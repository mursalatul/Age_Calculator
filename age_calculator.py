import tkinter as tk
import datetime as dt


# functions start
# input and process functions
def func_check():
    # cleaning display
    entry_sec.delete(0, "end")
    entry_min.delete(0, "end")
    entry_hour.delete(0, "end")
    entry_day.delete(0, "end")
    entry_week.delete(0, "end")
    entry_month.delete(0, "end")
    entry_year.delete(0, "end")

    # taking input
    day = int(entry_day_input.get())
    month = int(entry_month_input.get())
    year = int(entry_year_input.get())

    #tillday = dt.datetime.now().year
    try:
        if int(entry_tillday_input.get()) > 0:
            tillday = int(entry_tillday_input.get())
            tillmonth = int(entry_tillmonth_input.get())
            tillyear = int(entry_tillyear_input.get())
            current_time = dt.datetime(year=tillyear, month=tillmonth, day=tillday)
    except:
        current_time = dt.datetime.now()

    # calculating data
    my_birthdate = dt.datetime(day=day, month=month, year=year)
    #current_time = datetime.datetime.now()  # current_time is the time when program is running
    # output day
    my_days = (current_time.date() - my_birthdate.date()).days
    entry_day.insert(0, my_days)
    # output year
    my_years = current_time.year - my_birthdate.year
    entry_year.insert(0, my_years)
    # output hour
    my_hours = (my_days * 24) + current_time.time().hour
    entry_hour.insert(0, my_hours)
    # output min
    my_mins = (my_hours * 60) + current_time.time().minute
    entry_min.insert(0, my_mins)
    # output second
    my_secs = (my_mins * 60) + current_time.time().second
    entry_sec.insert(0, my_secs)
    # output week and month
    my_weeks = my_days // 7
    entry_week.insert(0, my_weeks)
    my_extra_days_after_weeks = my_days % 7
    my_months = my_days // 30
    entry_month.insert(0, my_months)
    my_extra_days_after_months = my_days % 30
    if my_extra_days_after_weeks != 0:
        if my_extra_days_after_weeks == 1:
            ddddd = "day"
        else:
            ddddd = "days"
        index_of_weeks = len(entry_week.get())
        entry_week.insert(index_of_weeks, f" + {my_extra_days_after_weeks} {ddddd}")
    if my_extra_days_after_months != 0:
        if my_extra_days_after_months == 1:
            dddd = "day"
        else:
            dddd = "days"
        index_of_months = len(entry_month.get())
        entry_month.insert(index_of_months, f" + {my_extra_days_after_months} {dddd}")


def func_clear():
    """Clear entries of input fields"""
    entry_day_input.delete(0, "end")
    entry_month_input.delete(0, "end")
    entry_year_input.delete(0, "end")
    entry_tillyear_input.delete(0, "end")
    entry_tillmonth_input.delete(0, "end")
    entry_tillyear_input.delete(0, "end")


def enter1(*args):
    """when enter will be clicked 1st time, focus will go to month field to take input"""
    entry_month_input.focus()


def enter2(*args):
    """when enter will be clicked 2nd time, focus will go to year field to take input"""
    entry_year_input.focus()

def enter3(*args):
    """when enter will be clicked 3rd time, focus will go to till day field to take input"""
    entry_tillday_input.focus()

def enter4(*args):
    """when enter will be clicked 4rt time, focus will go to till month field to take input"""
    entry_tillmonth_input.focus()

def enter5(*args):
    """when enter will be clicked 5th time, focus will go to till year field to take input"""
    entry_tillyear_input.focus()

def enter6(*args):
    """3rd time enter click = func_check()"""
    func_check()

def shift1(*args):
    """shift key will clear all birthday field and focus on day field"""
    entry_day_input.delete(0, "end")
    entry_month_input.delete(0, "end")
    entry_year_input.delete(0, "end")
    entry_day_input.focus()

def shift2(*args):
    """shift2 key will clear all the till inputs and focus on till day field"""
    entry_tillday_input.delete(0, "end")
    entry_tillmonth_input.delete(0, "end")
    entry_tillyear_input.delete(0, "end")
    entry_tillday_input.focus()

def update_current_time():
    """update the current time after 1 second"""
    current_time_label['text'] = dt.datetime.now().strftime("%H:%M:%S %d/%m/%Y")
    wn.after(1000, update_current_time)

#*** GUI ***

# universal constant variables
WINDOW_BG_COLOR = "#85C1E9"

# setup tkinter
wn = tk.Tk()
wn.geometry("500x600")
wn.minsize(550, 550)
wn.maxsize(550, 550)
wn.configure(bg=WINDOW_BG_COLOR)
wn.title("")

# day month year input section
# header
tk.Label(wn, text="Age Calculator", font=("bold", 20, "underline"), bg=WINDOW_BG_COLOR).grid(rowspan=1,column=2)

# day
tk.Label(wn, bg=WINDOW_BG_COLOR, text="Day", font=("bold", 16)).grid(row=2, column=1, padx=55)
entry_day_input = tk.Entry(wn, bg="#D4E6F1", width=7, relief="groove", font="bold")
entry_day_input.grid(row=3, column=1)
entry_day_input.focus()
entry_day_input.bind("<Return>", enter1)
entry_day_input.bind("<Shift_L>", shift1)
entry_day_input.bind("<Shift_R>", shift1)

# month
tk.Label(wn, bg=WINDOW_BG_COLOR, text="Month", font=("bold", 16)).grid(row=2, column=2, padx=55)
entry_month_input = tk.Entry(wn, bg="#D4E6F1", width=7, relief="groove", font="bold")
entry_month_input.grid(row=3, column=2)
entry_month_input.bind("<Return>", enter2)
entry_month_input.bind("<Shift_L>", shift1)
entry_month_input.bind("<Shift_R>", shift1)

# year
tk.Label(wn, bg=WINDOW_BG_COLOR, text="Year", font=("bold", 16)).grid(row=2, column=3, padx=55)
entry_year_input = tk.Entry(wn, bg="#D4E6F1", width=7, relief="groove", font="bold")
entry_year_input.grid(row=3, column=3)
entry_year_input.bind("<Return>", enter3)
entry_year_input.bind("<Shift_L>", shift1)
entry_year_input.bind("<Shift_R>", shift1)

# till
tk.Label(wn, bg=WINDOW_BG_COLOR, text="Till (Optional)", font=("bold", 13)).grid(row=4, column=2)
# till day input window
entry_tillday_input = tk.Entry(wn, bg ="#D4E6F1", width=5, relief="groove", font=("bold", 10))
entry_tillday_input.grid(row=5, column=1)
entry_tillday_input.bind("<Return>", enter4)
entry_tillday_input.bind("<Shift_L>", shift2)
entry_tillday_input.bind("<Shift_R>", shift2)

# till month input window
entry_tillmonth_input = tk.Entry(wn, bg="#D4E6F1", width=5, relief="groove", font=("bold", 10))
entry_tillmonth_input.grid(row=5, column=2)
entry_tillmonth_input.bind("<Return>", enter5)
entry_tillmonth_input.bind("<Shift_L>", shift2)
entry_tillmonth_input.bind("<Shift_R>", shift2)

# till year input window
entry_tillyear_input= tk.Entry(wn, bg="#D4E6F1", width=5, relief="groove", font=("bold", 10))
entry_tillyear_input.grid(row=5, column=3)
entry_tillyear_input.bind("<Return>", enter6)
entry_tillyear_input.bind("<Shift_L>", shift2)
entry_tillyear_input.bind("<Shift_R>", shift2)

tk.Label(wn, bg=WINDOW_BG_COLOR, ).grid(row=6, columnspan=3)

# CHECK and CLEAR button section
tk.Button(wn, bg="#FADBD8", text="CHECK", font=("bold", 18), relief="raised", activeforeground="#52BE80",
                        width=10, command=func_check).grid(row=7, column=1)
tk.Button(wn, bg="#FADBD8", text="CLEAR", font=("bold", 18), relief="raised", activeforeground="#E74C3C",
                        width=10, command=func_clear).grid(row=7, column=3)

tk.Label(wn, bg=WINDOW_BG_COLOR, ).grid(row=9, columnspan=3)

# output window
# sec
tk.Label(wn, bg=WINDOW_BG_COLOR, text="sec", font=("bold", 16)).grid(row=10, column=1)
entry_sec = tk.Entry(wn, width=30, relief="raised", font="bold")
entry_sec.grid(row=10, columnspan=4)

# min
tk.Label(wn, bg=WINDOW_BG_COLOR, text="min", font=("bold", 16)).grid(row=11, column=1)
entry_min = tk.Entry(wn, width=30, relief="raised", font="bold")
entry_min.grid(row=11, columnspan=4)

# hour
tk.Label(wn, bg=WINDOW_BG_COLOR, text="hour", font=("bold", 16)).grid(row=12, column=1)
entry_hour = tk.Entry(wn, width=30, relief="raised", font="bold")
entry_hour.grid(row=12, columnspan=4)

# day
tk.Label(wn, bg=WINDOW_BG_COLOR, text="day", font=("bold", 16)).grid(row=13, column=1)
entry_day = tk.Entry(wn, width=30, relief="raised", font="bold")
entry_day.grid(row=13, columnspan=4)

# week
tk.Label(wn, bg=WINDOW_BG_COLOR, text="week", font=("bold", 16)).grid(row=14, column=1)
entry_week = tk.Entry(wn, width=30, relief="raised", font="bold")
entry_week.grid(row=14, columnspan=4)

# month
tk.Label(wn, bg=WINDOW_BG_COLOR, text="month", font=("bold", 16)).grid(row=15, column=1)
entry_month = tk.Entry(wn, width=30, relief="raised", font="bold")
entry_month.grid(row=15, columnspan=4)

# year
tk.Label(wn, bg=WINDOW_BG_COLOR, text="year", font=("bold", 16)).grid(row=16, column=1)
entry_year = tk.Entry(wn, width=30, relief="raised", font="bold")
entry_year.grid(row=16, columnspan=4)

tk.Label(wn, bg=WINDOW_BG_COLOR, ).grid(row=17, columnspan=3)

# exit button

tk.Button(wn, text="EXIT", bg="#fc2c00", relief="raised", activebackground="#e35e17",command=exit).grid(row=18, column=2)

# current time and date
current_time_label = tk.Label(wn, font=(10), bg=WINDOW_BG_COLOR)
current_time_label.grid(row=18,column=3)
update_current_time()

wn.mainloop()
