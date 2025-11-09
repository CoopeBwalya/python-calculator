#function adds two values
def add(a,b):
    return a + b
#Subtratracts two values
def subtract(a, b):
    return a - b
#Function multiplies two values
def multiply(a, b):
    return a * b
#Function divides two values
def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Error: Division by zero!")
        return None
#Function find the modulus of two numbers
def modulus(a, b):
    try:
        return a % b
    except ZeroDivisionError:
        print("Error: Modulus by zero!")
        return None
#Function gets the number input
def get_number_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")
        
history = []
#Fnction gets back the history input
def update_history(num1, op, num2, result):
    entry = f"{num1} {op} {num2} = {result}"
    history.append(entry)
#Function displays the history input
def display_history():
    if not history:
        print("No calculations yet.")
    else:
        print("\n--- Calculation History ---")()
        for h in history:
            print(h)()

def calculator():
    while True:
        print("\nOptions: +  -  *  /  %  history  clear  quit")
        choice = input("Choose operation: ").strip().lower()

        if choice in ['+', '-', '*', '/', '%']:
            x = get_number_input("Enter first number: ")
            y = get_number_input("Enter second number: ")

            if choice == '+':
                result = add(x, y)
            elif choice == '-':
                result = subtract(x, y)
            elif choice == '*':
                result = multiply(x, y)
            elif choice == '/':
                result = divide(x, y)
            else:  # %
                result = modulus(x, y)      

            print("Result:", result)
            update_history(x, choice, y, result)

        elif choice == "history":
            display_history()

        elif choice == "clear":
            history.clear()
            print("History cleared.")

        elif choice == "quit":
            print("Goodbye!")
            break

        else:memory = 0.0
#Function gets the memory 
def memory_add(val):
    global memory
    memory += val

def memory_subtract(val):
    global memory
    memory -= val
#Function recalls memory
def memory_recall():
    return memory
#fuunction clears memory
def memory_clear():
    global memory
    memory = 0.0

def exponent(base, power):
    return base ** power

def square_root(x):
    return "math".sqrt(x)
#interface of the calculator
import tkinter as tk

def append_value(value):
    current = display.get()
    display.delete(0, tk.END)
    display.insert(0, current + value)

def clear_display():
    display.delete(0, tk.END)

def calculate():
    try:
        result = eval(display.get())
        display.delete(0, tk.END)
        display.insert(0, str(result))
    except:
        display.delete(0, tk.END)
        display.insert(0, "Error")

# Create main window
root = tk.Tk()
root.title("Calculator")

# Display field
display = tk.Entry(root, width=25, font=("Arial", 18), borderwidth=2, relief="solid", justify="right")
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Button layout
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('C', 4, 2), ('+', 4, 3),
    ('=', 5, 0, 4)
]

for btn in buttons:
    text = btn[0]
    row = btn[1]
    col = btn[2]
    colspan = btn[3] if len(btn) == 4 else 1
    action = lambda x=text: append_value(x) if x not in ['C', '='] else (clear_display() if x == 'C' else calculate())
    tk.Button(root, text=text, width=5 * colspan, height=2, font=("Arial", 14), command=action).grid(row=row, column=col, columnspan=colspan, padx=5, pady=5)


root.mainloop()

