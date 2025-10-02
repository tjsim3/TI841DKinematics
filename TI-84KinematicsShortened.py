import math

def get_num(prompt):
    return float(input(prompt))

def simple_plot(xi, vi, a, total_time):
    print("")
    print("POSITION vs TIME")
    print("================")
    
    # Calculate 5 key points
    times = [0, total_time/4, total_time/2, 3*total_time/4, total_time]
    
    print("Time -- Position")
    
    for t in times:
        x = xi + vi * t + 0.5 * a * t**2
        t_str = str(round(t,1))
        x_str = str(round(x,1))
        print(t_str + "       " + x_str)
    
    print("")
    print("Shape:")
    if a > 0.05:
        print("Curves up")
        print("   /")
        print("  /")
        print(" /")
    elif a < -0.05:
        print("Curves down")
        print("\\")
        print(" \\")
        print("  \\")
    else:
        print("Straight line")
        print("----")
    
    input("Press Enter...")

print("KINEMATICS CALC")
print("1: Position")
print("2: Velocity") 
print("3: Acceleration")
print("4: Time")

choice = int(input("Solve for: "))

# Store values for graphing
xi_val = 0
vi_val = 0
a_val = 0
t_val = 0
can_graph = False

if choice == 1:
    print("Final Position")
    print("Have xi,vi,a,t? (1=yes)")
    if int(input()) == 1:
        xi_val = get_num("xi: ")
        vi_val = get_num("vi: ")
        a_val = get_num("a: ")
        t_val = get_num("t: ")
        x = xi_val + vi_val*t_val + 0.5*a_val*t_val*t_val
        print("x = " + str(round(x,3)))
        can_graph = True

elif choice == 2:
    print("Final Velocity")
    sub = int(input("1=vi,a,t  2=vi,a,x: "))
    if sub == 1:
        vi_val = get_num("vi: ")
        a_val = get_num("a: ")
        t_val = get_num("t: ")
        v = vi_val + a_val*t_val
        print("v = " + str(round(v,3)))
        xi_val = 0
        can_graph = True
    elif sub == 2:
        vi_val = get_num("vi: ")
        a_val = get_num("a: ")
        x = get_num("distance: ")
        v = math.sqrt(vi_val*vi_val + 2*a_val*x)
        print("v = " + str(round(v,3)))
        if a_val != 0:
            t_val = (v - vi_val) / a_val
            xi_val = 0
            can_graph = True

elif choice == 3:
    print("Acceleration")
    sub = int(input("1=v,vi,t  2=v,vi,x: "))
    if sub == 1:
        vi_val = get_num("vi: ")
        v = get_num("v: ")
        t_val = get_num("t: ")
        a_val = (v-vi_val)/t_val
        print("a = " + str(round(a_val,3)))
        xi_val = 0
        can_graph = True
    elif sub == 2:
        vi_val = get_num("vi: ")
        v = get_num("v: ")
        x = get_num("distance: ")
        a_val = (v*v-vi_val*vi_val)/(2*x)
        print("a = " + str(round(a_val,3)))
        if a_val != 0:
            t_val = (v - vi_val) / a_val
            xi_val = 0
            can_graph = True

elif choice == 4:
    print("Time")
    sub = int(input("1=v,vi,a  2=x,vi,a: "))
    if sub == 1:
        vi_val = get_num("vi: ")
        v = get_num("v: ")
        a_val = get_num("a: ")
        t_val = (v-vi_val)/a_val
        print("t = " + str(round(t_val,3)))
        xi_val = 0
        can_graph = True
    elif sub == 2:
        x = get_num("distance: ")
        vi_val = get_num("vi: ")
        a_val = get_num("a: ")
        disc = vi_val*vi_val + 2*a_val*x
        if disc >= 0:
            t_val = (-vi_val + math.sqrt(disc))/a_val
            print("t = " + str(round(t_val,3)))
            xi_val = 0
            can_graph = True
        else:
            print("No solution")

# Ask if user wants to see graph
if can_graph and t_val > 0:
    graph_choice = int(input("Show graph? (1=yes 0=no): "))
    if graph_choice == 1:
        simple_plot(xi_val, vi_val, a_val, t_val)

print("Done")