


def calc() -> int:
    """ A simple calculator

    Args: 
        num1: The first digit to work on.
        operator: The operation sign to be carried out.
        num2: The second digit to work on.
    Returns: 
        The result of the operation carried out!
    """
#Error handling for inputs
    try:
        num1 = int(input("Enter 1st digit: "))
    except ValueError:
        print("Error.Enter only digits!")
        return
    operator = input("Enter operator (eg +,-,*,** or /): ")

    if operator not in ("+", "-", "/", "*", "**"):
        print("Invalid operator!")
        return
    
    try:
        num2 = int(input("Enter 2nd digit: "))
    except ValueError:
        print("Error. Enter only digits!")
        return
   
#processing

    if operator == "*":
        ans =  num1*num2
        print(ans)
        
 
    elif operator == "/":
        try:
            ans =  num1/num2
            print(ans)
        except ZeroDivisionError:
            print("Error! Division by Zero not allowed.")

    elif operator == "+":
        ans =  num1+num2
        print(ans)

    elif operator == "-":
        ans =  num1-num2
        print(ans)

    elif operator =="**":
        ans = num1**num2
        print(ans)
    else:
        return
calc()     
