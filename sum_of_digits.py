def sum_of_digits(number):
    number=abs(number)
    total=0
    while number >0:
        total=total+number %10
        number//=10
    return total