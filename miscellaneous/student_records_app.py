from tkinter import Tk, Button, Label, Entry, Text, END, NORMAL, DISABLED, font
from tkinter.messagebox import showinfo
from datetime import datetime
import csv

app = Tk()
app.title('Student Records')
app.geometry('1048x700')
# Create a custom font with your desired size and other attributes
custom_font = ('Helvetica', 24)
app.option_add("*Font", custom_font)

# Create Entry Fields
pid_label = Label(app, text='PantherID')
pid_label.grid(row=0, column=0)
pid_entry = Entry(app)
pid_entry.grid(row=0, column=1)
name_label = Label(app, text='Name')
name_label.grid(row=1, column=0)
name_entry = Entry(app)
name_entry.grid(row=1, column=1)
email_label = Label(app, text='Email')
email_label.grid(row=2, column=0)
email_entry = Entry(app)
email_entry.grid(row=2, column=1)

# Create Buttons
add_button = Button(app, text='Add Student')
add_button.grid(row=3, column=0, columnspan=2)
list_button = Button(app, text='List Students')
list_button.grid(row=4, column=0, columnspan=2)

# Create Textbox for Displaying Records
record_display = Text(app)
record_display.grid(row=5, column=0, columnspan=2)

# Define Button click event handlers
def add_student():
    pantherid = pid_entry.get()
    name = name_entry.get()
    email = email_entry.get()
    if pantherid == '' or name == '' or email == '':
        showinfo(message='Enter required info!')
        return
    try:
        with open('student_records.csv', 'a') as outfile:
            row = [pantherid, name, email]
            csv_writer = csv.writer(outfile)
            csv_writer.writerow(row)
            showinfo(message='Student record saved.')
    except:
        showinfo("Error during saving student record!")

    pid_entry.delete(0,END)
    name_entry.delete(0,END)
    email_entry.delete(0,END)

def list_students():
    records = []
    try:
        with open('student_records.csv','r') as infile:
            csv_reader = csv.reader(infile)
            for row in csv_reader:
                records.append(row)
    except:
        showinfo("Error during reading CSV.")

    record_display.delete(1.0, END)
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    record_display.insert(END, f'Student List as of {timestamp}\n')
    for record in records:
        record_display.insert(END,record)
        record_display.insert(END, "\n")
add_button.config(command=add_student)
list_button.config(command=list_students)
app.mainloop()
