import math

# Kinematic equations for 1D motion
#---------- BIG 4 EQUATIONS ----------#

# Equation 1: x = xi + vi*t + 0.5*a*t^2
def eq1_solve_x(xi, vi, a, t):
    return xi + vi * t + 0.5 * a * t**2

def eq1_solve_vi(x, xi, a, t):
    if t == 0:
        return None
    return (x - xi - 0.5 * a * t**2) / t

def eq1_solve_a(x, xi, vi, t):
    if t == 0:
        return None
    return 2 * (x - xi - vi * t) / (t**2)

def eq1_solve_t(x, xi, vi, a):
    if a == 0:
        if vi == 0:
            return None
        return (x - xi) / vi
    discriminant = vi**2 + 2 * a * (x - xi)
    if discriminant < 0:
        return None
    return (-vi + math.sqrt(discriminant)) / a

def eq1_solve_xi(x, vi, a, t):
    return x - vi * t - 0.5 * a * t**2

# Equation 2: v = vi + a*t
def eq2_solve_v(vi, a, t):
    return vi + a * t

def eq2_solve_vi(v, a, t):
    return v - a * t

def eq2_solve_a(v, vi, t):
    if t == 0:
        return None
    return (v - vi) / t

def eq2_solve_t(v, vi, a):
    if a == 0:
        return None
    return (v - vi) / a

# Equation 3: v^2 = vi^2 + 2*a*(x-xi)
def eq3_solve_v(vi, a, xi, x):
    discriminant = vi**2 + 2 * a * (x - xi)
    if discriminant < 0:
        return None
    return math.sqrt(discriminant)

def eq3_solve_vi(v, a, xi, x):
    discriminant = v**2 - 2 * a * (x - xi)
    if discriminant < 0:
        return None
    return math.sqrt(discriminant)

def eq3_solve_a(v, vi, xi, x):
    if (x - xi) == 0:
        return None
    return (v**2 - vi**2) / (2 * (x - xi))

def eq3_solve_x(v, vi, a, xi):
    if a == 0:
        return None
    return (v**2 - vi**2) / (2 * a) + xi

def eq3_solve_xi(v, vi, a, x):
    if a == 0:
        return None
    return x - (v**2 - vi**2) / (2 * a)

# Equation 4: x = xi + 0.5*(vi+v)*t
def eq4_solve_x(xi, vi, v, t):
    return xi + 0.5 * (vi + v) * t

def eq4_solve_xi(x, vi, v, t):
    return x - 0.5 * (vi + v) * t

def eq4_solve_vi(x, xi, v, t):
    if t == 0:
        return None
    return 2 * (x - xi) / t - v

def eq4_solve_v(x, xi, vi, t):
    if t == 0:
        return None
    return 2 * (x - xi) / t - vi

def eq4_solve_t(x, xi, vi, v):
    if (vi + v) == 0:
        return None
    return 2 * (x - xi) / (vi + v)

def Main():
    print("1D Kinematics Calculator")
    print("Variables: xi (initial position), x (final position), vi (initial velocity), v (final velocity), a (acceleration), t (time)")
    
    variables = ["xi", "x", "vi", "v", "a", "t"]
    
    # Ask user which variable to solve for and which is missing
    while True:
        solve_for = input("\nEnter the variable to solve for (xi, x, vi, v, a, t): ").strip()
        missing = input("Enter the missing variable (xi, x, vi, v, a, t): ").strip()
        if solve_for in variables and missing in variables and solve_for != missing:
            break
        print("Invalid input. Please enter valid and distinct variables.")
    
    # Define all possible equations and what they can solve
    equations = [
        # Equation 1: x = xi + vi*t + 0.5*a*t^2
        {"func": eq1_solve_x, "needs": ["xi", "vi", "a", "t"], "solves": "x", "name": "Equation 1"},
        {"func": eq1_solve_xi, "needs": ["x", "vi", "a", "t"], "solves": "xi", "name": "Equation 1"},
        {"func": eq1_solve_vi, "needs": ["x", "xi", "a", "t"], "solves": "vi", "name": "Equation 1"},
        {"func": eq1_solve_a, "needs": ["x", "xi", "vi", "t"], "solves": "a", "name": "Equation 1"},
        {"func": eq1_solve_t, "needs": ["x", "xi", "vi", "a"], "solves": "t", "name": "Equation 1"},
        
        # Equation 2: v = vi + a*t
        {"func": eq2_solve_v, "needs": ["vi", "a", "t"], "solves": "v", "name": "Equation 2"},
        {"func": eq2_solve_vi, "needs": ["v", "a", "t"], "solves": "vi", "name": "Equation 2"},
        {"func": eq2_solve_a, "needs": ["v", "vi", "t"], "solves": "a", "name": "Equation 2"},
        {"func": eq2_solve_t, "needs": ["v", "vi", "a"], "solves": "t", "name": "Equation 2"},
        
        # Equation 3: v^2 = vi^2 + 2*a*(x-xi)
        {"func": eq3_solve_v, "needs": ["vi", "a", "xi", "x"], "solves": "v", "name": "Equation 3"},
        {"func": eq3_solve_vi, "needs": ["v", "a", "xi", "x"], "solves": "vi", "name": "Equation 3"},
        {"func": eq3_solve_a, "needs": ["v", "vi", "xi", "x"], "solves": "a", "name": "Equation 3"},
        {"func": eq3_solve_x, "needs": ["v", "vi", "a", "xi"], "solves": "x", "name": "Equation 3"},
        {"func": eq3_solve_xi, "needs": ["v", "vi", "a", "x"], "solves": "xi", "name": "Equation 3"},
        
        # Equation 4: x = xi + 0.5*(vi+v)*t
        {"func": eq4_solve_x, "needs": ["xi", "vi", "v", "t"], "solves": "x", "name": "Equation 4"},
        {"func": eq4_solve_xi, "needs": ["x", "vi", "v", "t"], "solves": "xi", "name": "Equation 4"},
        {"func": eq4_solve_vi, "needs": ["x", "xi", "v", "t"], "solves": "vi", "name": "Equation 4"},
        {"func": eq4_solve_v, "needs": ["x", "xi", "vi", "t"], "solves": "v", "name": "Equation 4"},
        {"func": eq4_solve_t, "needs": ["x", "xi", "vi", "v"], "solves": "t", "name": "Equation 4"},
    ]
    
    equation_found = False
    
    # Find suitable equation
    for eq_info in equations:
        if eq_info["solves"] != solve_for:
            continue
        
        # Check if this equation requires the missing variable
        if missing in eq_info["needs"]:
            continue
        
        # This equation can work - get the required inputs
        print(f"\nUsing {eq_info['name']} to solve for {solve_for}")
        print(f"Required variables: {[var for var in eq_info['needs'] if var != solve_for]}")
        
        args = []
        input_vars = []
        for var in eq_info["needs"]:
            if var == solve_for:
                continue  # Skip the variable we're solving for
            try:
                value = float(input(f"Enter the value for {var}: "))
                args.append(value)
                input_vars.append(f"{var}={value}")
            except ValueError:
                print("Invalid input. Please enter a number.")
                return
        
        # Calculate result
        try:
            result = eq_info["func"](*args)
            
            if result is None:
                print("Error: Cannot solve with these values (division by zero or invalid calculation).")
                return
            
            print(f"\nSolution:")
            print(f"Given: {', '.join(input_vars)}")
            print(f"Using {eq_info['name']}: {solve_for} = {result:.6f}")
            equation_found = True
            break
            
        except Exception as e:
            print(f"Error in calculation: {e}")
            return
    
    if not equation_found:
        print("No suitable equation found for that combination. Please try again.")

# Main execution loop
while True:
    try:
        Main()
        
        # Ask if user wants to continue
        continue_calc = input("\nDo another calculation? (y/n): ").strip().lower()
        if continue_calc != 'y' and continue_calc != 'yes':
            print("Goodbye!")
            break
        print("\n" + "="*50)
        
    except KeyboardInterrupt:
        print("\nGoodbye!")
        break
    except Exception as e:
        print(f"An error occurred: {e}")
        print("Please try again.\n")