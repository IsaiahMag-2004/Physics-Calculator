#Creates the UI for the application
from tkinter import *
from tkinter import ttk
from typing import final

from functions import find_change_in_time, find_final_velocity, find_accceleration, find_initial_velocity

root = Tk()
def convert():
    vf = bool(final_velocity.get())
    vi = bool(initial_velocity.get())
    delta_t = bool(change_in_time.get())
    a = bool(acceleration.get())

    if vf == True and vi == True and a == True:
        vi = float(input("What is your intital velocity: "))
        vf = float(input("What is your final velocity: "))
        acceleration = float(input("What is your acceleration: "))
        change_in_time = round(find_change_in_time(vf, vi, acceleration), 2)
        print(f"Your change in time is {change_in_time}")
    elif vi == True and a == True and delta_t == True:
        vi = float(input("What is your intital velocity: "))
        acceleration = float(input("What is your acceleration: "))
        change_in_time = float(input("What is your change in time: "))
        final_velocity = round(find_final_velocity(vi, acceleration, change_in_time), 2)
        print(f"The final velocity is {final_velocity}")
    else:
        print("Thanks anyway")


#Labels
final_velocity_label = Label (root, text='Final Velocity')
final_velocity_label.grid(row='0', column='0')
initial_velocity_label = Label (root, text='Initial Velocity', padx='1i')
initial_velocity_label.grid(row='0', column='1')
change_in_time_label = Label (root, text='Change in Time', padx='1i')
change_in_time_label.grid(row='0', column='2')
acceleration_label = Label (root, text="Acceleration")
acceleration_label.grid(row='0', column='3')

#Entry Boxes
final_velocity = Entry(root)
final_velocity.grid(row='1', column='0')
initial_velocity = Entry(root)
initial_velocity.grid(row='1', column='1')
change_in_time = Entry(root)
change_in_time.grid(row='1', column='2')
acceleration = Entry(root)
acceleration.grid(row='1', column='3')


#buttons
quit = Button(root, text='Quit', command=quit)
quit.grid()

converter = Button(root, text='Convert', command=convert)
converter.grid()

#List
final_velocity_list = Listbox(root)
final_velocity_list.insert(1, "True")
final_velocity_list.insert(2, "False")
final_velocity_list.grid(row='3', column='0')

initial_velocity_list = Listbox(root)
initial_velocity_list.insert(1, "True")
initial_velocity_list.insert(2, "False")
initial_velocity_list.grid(row='3', column='1')

change_in_time_list = Listbox(root)
change_in_time_list.insert(1, "True")
change_in_time_list.insert(2, "False")
change_in_time_list.grid(row='3', column='2')

acceleration_list = Listbox(root)
acceleration_list.insert(1, "True")
acceleration_list.insert(2, "False")
acceleration_list.grid(row='3', column='3')

root.mainloop()