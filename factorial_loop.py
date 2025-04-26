"""it cant be for negativess ......so we have to make sure it doestnt try anything that is <0 since 0!=1 so we kinda need to start with that 
we added a raise value to make sure we rememebrr it can not be negative"""
def factorial_loop(n):
    if n<0:
        raise ValueError("not for negative numbers")
    result = 1
    for i in range(1,n+1):
        result*=i
        return result