num1 = (input("Enter 1st digit: "))
operator = input("Enter operator: ")
num2 = (input("Enter 2nd digit: "))



def calc(num1:int, operator, num2:int) -> int:
    """ A simple calculator

    Args: 
        num1: The first digit to work on.
        operator: The operation sign to be carried out.
        num2: The second digit to work on.
    Returns: 
        The result of the operation carried out!
    """

    if operator == "*":
        try:
            ans =  int(num1)*int(num2)
            print(ans)
        except ValueError:
            print ("Error! 1st and 2nd digits should be integers!")
        return 
    elif operator == "x":
        try:
            ans =  int(num1)*int(num2)
            print(ans)
        except ValueError:
            print ("Error! 1st and 2nd digits should be integers!")
        return 
    elif operator == "/":
        try:
            ans =  int(num1)/int(num2)
            print(ans)
        except ValueError:
            print ("Error! 1st and 2nd digits should be integers!")
        return
    elif operator == "+":
        try:
            ans =  int(num1)+int(num2)
            print(ans)
        except ValueError:
            print ("Error! 1st and 2nd digits should be integers!")
        return
    elif operator == "-":
        try:
            ans =  int(num1)-int(num2)
            print(ans)
        except ValueError:
            print ("Error! 1st and 2nd digits should be integers!")
        return
    
    else:
        print("Invalid Operator!")
        return
(calc(num1,operator,num2))     
# try:
#     (calc(num1,operator,num2))
# except TypeError:
#     print("oops!")
# except ValueError:
#     print("oops")