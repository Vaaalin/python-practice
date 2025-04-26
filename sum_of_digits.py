"""number(int):a non-negativeinteger
this function calculates the sum of all digits in a number.
For example, if the number is 123, the sum is 1 + 2 + 3 = 6."""
def sum_of_digits(number):
    number=abs(number)
    total=0
    while number >0:
        total=total+number %10
        number//=10
    return total