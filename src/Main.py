def find_change_in_time (vf, vi, a):
	change_in_time = (vf - vi) / a
	return (change_in_time)
def find_final_velocity (vi, a, delta_t):
	final_velocity = vi + a * delta_t
	return (final_velocity)
def find_accceleration (vf, vi, delta_t):
	acceleration = (vf - vi) / delta_t
	return (acceleration)
def find_initial_velocity (vf, a, delta_t):
	inital_velocity = (a - vf) / delta_t
	return (inital_velocity)

vi = bool(input("(True/False) Do you have your intital velocity"))
acceleration = bool(input("(True/False) Do you have your acceleration"))
vf = bool(input("(True/False) Do you have your final velocity?"))
delta_t = bool(input("(True/False) Do you have your change in time?"))

if vf == True and vi == True and acceleration == True:
	vi = float(input("What is your intital velocity: "))
	vf = float(input("What is your final velocity: "))
	acceleration = float(input("What is your acceleration: "))
	change_in_time = round(find_change_in_time(vf, vi, acceleration), 2)
	print(f"Your change in time is {change_in_time}")
elif vi == True and acceleration == True and delta_t == True:
	vi = float(input("What is your intital velocity: "))
	acceleration = float(input("What is your acceleration: "))
	change_in_time = float(input("What is your change in time: "))
	final_velocity = round(find_final_velocity(vi, acceleration, change_in_time), 2)
	print(f"The final velocity is {final_velocity}")
else:
	print("Thanks anyway")

