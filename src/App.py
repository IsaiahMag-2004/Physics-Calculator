#Creates the UI for the application
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from typing import Collection
from functions import find_change_in_time, find_final_velocity, find_accceleration, find_initial_velocity

root = Tk()
root.title("Physics Calculator")

#Labels
final_velocity_label = Label (root, text='Final Velocity')
initial_velocity_label = Label (root, text='Initial Velocity', padx='1i')
change_in_time_label = Label (root, text='Change in Time', padx='1i')
acceleration_label = Label (root, text="Acceleration")
looking_for_label = Label (root, text='Looking For')
change_in_distance_label = Label (root, text='Change in Distance')
#Entry Boxes
final_velocity = Entry(root)
initial_velocity = Entry(root)
change_in_time = Entry(root)
acceleratio = Entry(root)
looking_for = Entry(root)
change_in_distance = Entry(root)
spacer_column_zero = Frame(root, height='1.27cm', width='3i')
spacer_column_one = Frame(root, height='1.27cm', width='3i')

#Button Function Creation
def convert():
    formula = looking_for.get()
    formula.lower()

    if formula == 'delta t':
        vi = float(initial_velocity.get())
        vf = float(final_velocity.get())
        acceleration = float(acceleratio.get())
        change_in_time = round(find_change_in_time(vf, vi, acceleration), 2)
        messagebox.showinfo( "Change In Time", change_in_time)
    elif formula == 'final velocity':
        vi = float(initial_velocity.get())
        acceleration = float(acceleratio.get())
        change_in_time = float(change_in_time.get())
        messagebox.showinfo("Initial Velocity", change_in_time)
        find_accceleration(vi, acceleration, change_in_time)
    elif formula == 'acceleration':
        vi = float(initial_velocity.get())
        vf = float(final_velocity.get())
        change_in_time = float(change_in_time.get())
        acceleration = find_accceleration(vf, vi, change_in_time)
        messagebox.showinfo("Acceleration", acceleration)
    else:
        vf = float(final_velocity.get())
        change_in_time = float(change_in_time.get())
        acceleration = float(acceleratio.get())
        initial_velocity = find_initial_velocity(vf, acceleration, change_in_time)
        messagebox.showinfo("Initial Velocity", initial_velocity)
#buttons
quit = Button(root, text='Quit', command=quit)
converter = Button(root, text='Convert', command=convert)

#Put it on the page
looking_for_label.grid(row= '4', column='0')
looking_for.grid(row='5', column='0')
final_velocity_label.grid(row='0', column='1')
final_velocity.grid(row='1', column='1')
initial_velocity_label.grid(row='2', column='1')
initial_velocity.grid(row='3', column='1')
change_in_time_label.grid(row='4', column='1')
change_in_time.grid(row='5', column='1')
acceleration_label.grid(row='6', column='1')
acceleratio.grid(row='7', column='1')
change_in_distance_label.grid(row='8', column='1')
change_in_distance.grid(row='9', column='1')
quit.grid(row='8', column='0')
converter.grid(row='9', column='0')
spacer_column_zero.grid(row='10', column='0')
spacer_column_one.grid(row='10', column='1')

root.mainloop()