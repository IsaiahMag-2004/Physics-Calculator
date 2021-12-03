#File that contains all the formula combinatiosn so that if one is changed on Main.py it dosnt effect App.py, and allows for alot easier tinkering so i know where the issue is if one ariases
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

