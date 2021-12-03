#Creates the UI for the application
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from functions import find_change_in_time, find_final_velocity, find_accceleration, find_initial_velocity

root = Tk()

#Labels
final_velocity_label = Label (root, text='Final Velocity')
initial_velocity_label = Label (root, text='Initial Velocity', padx='1i')
change_in_time_label = Label (root, text='Change in Time', padx='1i')
acceleration_label = Label (root, text="Acceleration")
looking_for_label = Label (root, text='Looking For')

#Entry Boxes
final_velocity = Entry(root)
initial_velocity = Entry(root)
change_in_time = Entry(root)
acceleratio = Entry(root)
looking_for = Entry(root)

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

#buttons
quit = Button(root, text='Quit', command=quit)
converter = Button(root, text='Convert', command=convert)

#Put it on the page
final_velocity_label.grid(row='0', column='0')
initial_velocity_label.grid(row='0', column='1')
change_in_time_label.grid(row='0', column='2')
acceleration_label.grid(row='0', column='3')
looking_for_label.grid(row= '2', column='0')
final_velocity.grid(row='1', column='0')
initial_velocity.grid(row='1', column='1')
change_in_time.grid(row='1', column='2')
acceleratio.grid(row='1', column='3')
looking_for.grid(row='3', column='0')
quit.grid(row='4', column='3')
converter.grid(row='4', column='2')

root.mainloop()