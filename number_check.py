'''just like in c++ we use %2 and if divisible by 2 it should do even and if it has a remainder its odd...we ask This function checks if a number is even or odd.
so It basically  provides additional information about the number.
'''
def number_check(numbers):
    if numbers %2==0:
        return "even"
    else:
        return "odd"

user_num=int(input("Enter a number:"))
print(number_check(user_num))