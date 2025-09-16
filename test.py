"""Implicitly convert the input to accept float values, by default it accepts str"""
number = float(input("Provide a number: "))
"""A global variable to store the remainder once a number has been divided"""
found_number:float = 0
def main_func():
    """Number must be greater than 3.5 so that function can have a remainder"""
    if number < 3.5:
        return print("Number provide must be greater than 3.5")
    else:
        while number >= 3.5:
            
            # if (number / 2) < 3.5:
            #     print(number)
            
            found_number = number / 2
            print(found_number)
            break
    

if __name__ == "__main__":
    main_func()