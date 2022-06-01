from tkinter import *
from tkcalendar import Calendar
import datetime
 
# Create Object
root = Tk()
 
# Set geometry
root.geometry("400x400")
 
# Add Calendar
cal = Calendar(root, selectmode = 'day',
            year = 2020, month = 5,
            day = 22)
 
cal.pack(pady = 20)
 
# method to add days
def add_days():
 
    date_1 = datetime.datetime.strptime(cal.get_date(), "%m/%d/%y")
 
    end_date = date_1 + datetime.timedelta(days=int(days.get()))
 
    converted_date.config(text=f"Date: {end_date.strftime('%m/%d/%Y')}")
 
# method to subtract days
def subtract_days():
 
    date_1 = datetime.datetime.strptime(cal.get_date(), "%m/%d/%y")
 
    end_date = date_1 - datetime.timedelta(days=int(days.get()))
 
    converted_date.config(text=f"Date: {end_date.strftime('%m/%d/%Y')}")
 
frame1 = Frame()
frame2 = Frame()
 
frame1.pack()
frame2.pack()
 
# making label
Label(frame1, text="Days", bd=1, bg="white", width=20, relief="solid",
      font="italic 10 bold").pack(side=LEFT)
 
# making spinbox
days = Spinbox(frame1, from_= 0, to = 10000000, font="italic 10")
days.pack(pady=20,padx=10)
 
# making buttons
Button(frame2, text = "Add Days",
    command = add_days,font="italic 15").pack(side=LEFT)
Button(frame2, text = "Subtract Days",
    command = subtract_days,font="italic 15").pack(padx=10)
 
# making label
converted_date = Label(text="Date: ", bd=2, bg="white",relief="solid",
                       font="italic 10 bold", width=30)
converted_date.pack(pady=20)
 
# Execute Tkinter
root.mainloop()