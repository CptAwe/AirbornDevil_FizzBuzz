
F = 0
B = 0

def fizzbuzz(start, end):
    """
    Plays the game Fizzbuzz and returns a list of the results.
    It does NOT make any sanity checks.
    """

    output = []
    for i in range(start, end+1):
        if i==0:
            output.append(i)
        elif i%F==0 and i%B==0 :
            output.append("FizzBuzz")
        elif i%F==0 :
            output.append("Fizz")
        elif i%B==0:
            output.append("Buzz")
        elif i%B==0:
            output.append("Buzz")
        else:
            output.append(i)
    
    return output

# FizzBuzz(0, 10)



