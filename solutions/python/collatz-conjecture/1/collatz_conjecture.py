def steps(number):
    count=0
    if number<=0:
        raise ValueError("Only positive integers are allowed")
    else:
        while number!=1:
            number = collatz(number)
            count=count+1

    return count
    pass

def collatz(num):
    if (num%2==0):
        return num//2
    else:
        return (3*num + 1)