import tkinter as tk
from tkinter import messagebox
import datetime as dt

def calculate_age():
    try:
        day = int(day_entry.get())
        month = int(month_entry.get())
        year = int(year_entry.get())

        birthdate = dt.datetime(year, month, day)
        current_time = dt.datetime.now()

        age = current_time - birthdate
        age_in_seconds = age.total_seconds()
        age_in_minutes = age_in_seconds / 60
        age_in_hours = age_in_minutes / 60
        age_in_days = age.days
        age_in_weeks = age_in_days / 7
        age_in_months = age_in_days / 30.44  # An average month has 30.44 days
        age_in_years = age_in_months / 12

        leap_years = count_leap_years(year, current_time.year)

        age_output.config(text=f"Age in seconds: {age_in_seconds:.2f}\n"
                                f"Age in minutes: {age_in_minutes:.2f}\n"
                                f"Age in hours: {age_in_hours:.2f}\n"
                                f"Age in days: {age_in_days}\n"
                                f"Age in weeks: {age_in_weeks:.2f}\n"
                                f"Age in months: {age_in_months:.2f}\n"
                                f"Age in years: {age_in_years:.2f}\n"
                                f"Leap years crossed: {leap_years}")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid date.")

def count_leap_years(start_year, end_year):
    return sum(1 for year in range(start_year, end_year + 1) if is_leap_year(year))

def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False

def clear_entries():
    day_entry.delete(0, "end")
    month_entry.delete(0, "end")
    year_entry.delete(0, "end")
    age_output.config(text="")

app = tk.Tk()
app.title("Age Calculator")

frame = tk.Frame(app)
frame.pack(padx=10, pady=10)

day_label = tk.Label(frame, text="Day:")
day_label.grid(row=0, column=0)

day_entry = tk.Entry(frame)
day_entry.grid(row=0, column=1)

month_label = tk.Label(frame, text="Month:")
month_label.grid(row=1, column=0)

month_entry = tk.Entry(frame)
month_entry.grid(row=1, column=1)

year_label = tk.Label(frame, text="Year:")
year_label.grid(row=2, column=0)

year_entry = tk.Entry(frame)
year_entry.grid(row=2, column=1)

calculate_button = tk.Button(frame, text="Calculate Age", command=calculate_age)
calculate_button.grid(row=3, column=0, columnspan=2, pady=10)

clear_button = tk.Button(frame, text="Clear", command=clear_entries)
clear_button.grid(row=4, column=0, columnspan=2, pady=10)

age_output = tk.Label(frame, text="", justify="left")
age_output.grid(row=5, column=0, columnspan=2)

app.mainloop()
