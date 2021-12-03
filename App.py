#Creates the UI for the application
from tkinter import *
from tkinter import ttk
from typing import final

root = Tk()
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


root.mainloop()