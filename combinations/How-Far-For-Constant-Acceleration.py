#All the combinations for how far for constant acceleration formula
#Origional: change_in_distance = (vi)*(delta_t)+(1/2)*(a)*(delta_t^2)



#origional In Python
def find_delta_d(vi, delta_t, a):
    initial_velocity = vi
    change_in_time = delta_t
    acceleration = a
    delta_d = initial_velocity * change_in_time + 0.5 * acceleration * change_in_time**2
    return (delta_d)    #The parenthasies are redundent
    

