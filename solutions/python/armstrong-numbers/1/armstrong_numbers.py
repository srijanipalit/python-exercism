#MY SOLUTION (complicated)

#function which returns 1 followed by a certain number of zeroes
def divisor(zeroes):
    prod = 1
    for i in range(zeroes):
        prod = prod*10
    return prod


def is_armstrong_number(number):
    
    number_saved = number
    num_string = str(number)
    num_digits = len(num_string)
    
    #initialise array of length num_digits
    d = [0] * num_digits
    d[0] = number%10

    for i in range(num_digits-1,0,-1): #runs from 0 to num_digits-2
        d[i] = number//divisor(i)
        number = number - (d[i] * divisor(i))

    sum = 0
    for i in range(num_digits):
        sum = sum + d[i]**num_digits

    if sum == number_saved:
        return True
    else:
        return False

#PYTHONIC SOLUTION (easy)
"""
def is_armstrong_number(number):
    # Convert the number to a string to get its digits and number of digits
    num_str = str(number)
    num_digits = len(num_str)
    
    total_sum = 0
    # Iterate through each character in the string
    for digit_char in num_str:
        # Convert the digit character back to an integer
        digit = int(digit_char)
        # Add the digit raised to the power of the number of digits to the total sum
        total_sum += digit ** num_digits
        
    # An Armstrong number is equal to the calculated sum
    return total_sum == number
"""

    
    
        
        
