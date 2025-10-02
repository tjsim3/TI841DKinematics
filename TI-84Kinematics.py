import math

def clear_screen():
    print("\n" * 10)

def get_float_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")

def main_menu():
    clear_screen()
    print("KINEMATICS CALCULATOR")
    print("=" * 20)
    print("Variables:")
    print("xi = initial position")
    print("x  = final position") 
    print("vi = initial velocity")
    print("v  = final velocity")
    print("a  = acceleration")
    print("t  = time")
    print()
    print("What do you want to solve for?")
    print("1. Initial position (xi)")
    print("2. Final position (x)")
    print("3. Initial velocity (vi)")
    print("4. Final velocity (v)")
    print("5. Acceleration (a)")
    print("6. Time (t)")
    print("0. Exit")
    
    choice = input("Enter choice (0-6): ")
    return choice

def solve_xi():
    clear_screen()
    print("SOLVING FOR INITIAL POSITION (xi)")
    print("Choose available variables:")
    print("1. Have: x, vi, a, t")
    print("2. Have: x, vi, v, t")
    print("3. Have: x, v, vi, a")
    
    choice = input("Choice: ")
    
    if choice == "1":
        x = get_float_input("Final position (x): ")
        vi = get_float_input("Initial velocity (vi): ")
        a = get_float_input("Acceleration (a): ")
        t = get_float_input("Time (t): ")
        
        xi = x - vi*t - 0.5*a*t**2
        print("\nUsing: x = xi + vi*t + 0.5*a*t²")
        print("Initial position (xi) = " + str(round(xi, 4)))
        
    elif choice == "2":
        x = get_float_input("Final position (x): ")
        vi = get_float_input("Initial velocity (vi): ")
        v = get_float_input("Final velocity (v): ")
        t = get_float_input("Time (t): ")
        
        xi = x - 0.5*(vi + v)*t
        print("\nUsing: x = xi + 0.5*(vi + v)*t")
        print("Initial position (xi) = " + str(round(xi, 4)))
        
    elif choice == "3":
        x = get_float_input("Final position (x): ")
        v = get_float_input("Final velocity (v): ")
        vi = get_float_input("Initial velocity (vi): ")
        a = get_float_input("Acceleration (a): ")
        
        if a == 0:
            print("Error: Cannot solve when a = 0")
            return
        
        xi = x - (v**2 - vi**2)/(2*a)
        print("\nUsing: v² = vi² + 2*a*(x - xi)")
        print("Initial position (xi) = " + str(round(xi, 4)))
    
    input("\nPress Enter to continue...")

def solve_x():
    clear_screen()
    print("SOLVING FOR FINAL POSITION (x)")
    print("Choose available variables:")
    print("1. Have: xi, vi, a, t")
    print("2. Have: xi, vi, v, t")
    print("3. Have: xi, v, vi, a")
    
    choice = input("Choice: ")
    
    if choice == "1":
        xi = get_float_input("Initial position (xi): ")
        vi = get_float_input("Initial velocity (vi): ")
        a = get_float_input("Acceleration (a): ")
        t = get_float_input("Time (t): ")
        
        x = xi + vi*t + 0.5*a*t**2
        print("\nUsing: x = xi + vi*t + 0.5*a*t²")
        print("Final position (x) = " + str(round(x, 4)))
        
    elif choice == "2":
        xi = get_float_input("Initial position (xi): ")
        vi = get_float_input("Initial velocity (vi): ")
        v = get_float_input("Final velocity (v): ")
        t = get_float_input("Time (t): ")
        
        x = xi + 0.5 * (vi + v) * t
        print("\nUsing: x = xi + 0.5*(vi + v)*t")
        print("Final position (x) = " + str(round(x, 4)))
        
    elif choice == "3":
        xi = get_float_input("Initial position (xi): ")
        v = get_float_input("Final velocity (v): ")
        vi = get_float_input("Initial velocity (vi): ")
        a = get_float_input("Acceleration (a): ")
        
        if a == 0:
            print("Error: Cannot solve when a = 0")
            return
        
        x = (v**2 - vi**2)/(2*a) + xi
        print("\nUsing: v² = vi² + 2*a*(x - xi)")
        print("Final position (x) = " + str(round(x, 4)))
    
    input("\nPress Enter to continue...")

def solve_vi():
    clear_screen()
    print("SOLVING FOR INITIAL VELOCITY (vi)")
    print("Choose available variables:")
    print("1. Have: x, xi, a, t")
    print("2. Have: v, a, t")
    print("3. Have: v, a, xi, x")
    
    choice = input("Choice: ")
    
    if choice == "1":
        x = get_float_input("Final position (x): ")
        xi = get_float_input("Initial position (xi): ")
        a = get_float_input("Acceleration (a): ")
        t = get_float_input("Time (t): ")
        
        if t == 0:
            print("Error: Cannot solve when t = 0")
            return
        
        vi = (x - xi - 0.5*a*t**2)/t
        print("\nUsing: x = xi + vi*t + 0.5*a*t²")
        print("Initial velocity (vi) = " + str(round(vi, 4)))
        
    elif choice == "2":
        v = get_float_input("Final velocity (v): ")
        a = get_float_input("Acceleration (a): ")
        t = get_float_input("Time (t): ")
        
        vi = v - a*t
        print("\nUsing: v = vi + a*t")
        print("Initial velocity (vi) = " + str(round(vi, 4)))
        
    elif choice == "3":
        v = get_float_input("Final velocity (v): ")
        a = get_float_input("Acceleration (a): ")
        xi = get_float_input("Initial position (xi): ")
        x = get_float_input("Final position (x): ")
        
        discriminant = v**2 - 2*a*(x - xi)
        if discriminant < 0:
            print("Error: No real solution (negative under square root)")
            return
        
        vi = math.sqrt(discriminant)
        print("\nUsing: v² = vi² + 2*a*(x - xi)")
        print("Initial velocity (vi) = " + str(round(vi, 4)))
    
    input("\nPress Enter to continue...")

def solve_v():
    clear_screen()
    print("SOLVING FOR FINAL VELOCITY (v)")
    print("Choose available variables:")
    print("1. Have: vi, a, t")
    print("2. Have: vi, a, xi, x")
    
    choice = input("Choice: ")
    
    if choice == "1":
        vi = get_float_input("Initial velocity (vi): ")
        a = get_float_input("Acceleration (a): ")
        t = get_float_input("Time (t): ")
        
        v = vi + a*t
        print("\nUsing: v = vi + a*t")
        print("Final velocity (v) = " + str(round(v, 4)))
        
    elif choice == "2":
        vi = get_float_input("Initial velocity (vi): ")
        a = get_float_input("Acceleration (a): ")
        xi = get_float_input("Initial position (xi): ")
        x = get_float_input("Final position (x): ")
        
        discriminant = vi**2 + 2*a*(x - xi)
        if discriminant < 0:
            print("Error: No real solution (negative under square root)")
            return
        
        v = math.sqrt(discriminant)
        print("\nUsing: v² = vi² + 2*a*(x - xi)")
        print("Final velocity (v) = " + str(round(v, 4)))
    
    input("\nPress Enter to continue...")

def solve_a():
    clear_screen()
    print("SOLVING FOR ACCELERATION (a)")
    print("Choose available variables:")
    print("1. Have: v, vi, t")
    print("2. Have: v, vi, xi, x")
    
    choice = input("Choice: ")
    
    if choice == "1":
        v = get_float_input("Final velocity (v): ")
        vi = get_float_input("Initial velocity (vi): ")
        t = get_float_input("Time (t): ")
        
        if t == 0:
            print("Error: Cannot solve when t = 0")
            return
        
        a = (v - vi)/t
        print("\nUsing: v = vi + a*t")
        print("Acceleration (a) = " + str(round(a, 4)))
        
    elif choice == "2":
        v = get_float_input("Final velocity (v): ")
        vi = get_float_input("Initial velocity (vi): ")
        xi = get_float_input("Initial position (xi): ")
        x = get_float_input("Final position (x): ")
        
        if (x - xi) == 0:
            print("Error: Cannot solve when x = xi")
            return
        
        a = (v**2 - vi**2)/(2*(x - xi))
        print("\nUsing: v² = vi² + 2*a*(x - xi)")
        print("Acceleration (a) = " + str(round(a, 4)))
    
    input("\nPress Enter to continue...")

def solve_t():
    clear_screen()
    print("SOLVING FOR TIME (t)")
    print("Choose available variables:")
    print("1. Have: v, vi, a")
    print("2. Have: x, xi, vi, a")
    
    choice = input("Choice: ")
    
    if choice == "1":
        v = get_float_input("Final velocity (v): ")
        vi = get_float_input("Initial velocity (vi): ")
        a = get_float_input("Acceleration (a): ")
        
        if a == 0:
            print("Error: Cannot solve when a = 0")
            return
        
        t = (v - vi)/a
        print("\nUsing: v = vi + a*t")
        print("Time (t) = " + str(round(t, 4)))
        
    elif choice == "2":
        x = get_float_input("Final position (x): ")
        xi = get_float_input("Initial position (xi): ")
        vi = get_float_input("Initial velocity (vi): ")
        a = get_float_input("Acceleration (a): ")
        
        if a == 0:
            if vi == 0:
                print("Error: Cannot solve when both a = 0 and vi = 0")
                return
            t = (x - xi)/vi
            print("\nUsing: x = xi + vi*t (when a = 0)")
            print("Time (t) = " + str(round(t, 4)))
        else:
            discriminant = vi**2 + 2*a*(x - xi)
            if discriminant < 0:
                print("Error: No real solution (negative under square root)")
                return
            
            t = (-vi + math.sqrt(discriminant))/a
            print("\nUsing: x = xi + vi*t + 0.5*a*t²")
            print("Time (t) = " + str(round(t, 4)))
    
    input("\nPress Enter to continue...")

# Main program loop
while True:
    choice = main_menu()
    
    if choice == "1":
        solve_xi()
    elif choice == "2":
        solve_x()
    elif choice == "3":
        solve_vi()
    elif choice == "4":
        solve_v()
    elif choice == "5":
        solve_a()
    elif choice == "6":
        solve_t()
    elif choice == "0":
        clear_screen()
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
        input("Press Enter to continue...")