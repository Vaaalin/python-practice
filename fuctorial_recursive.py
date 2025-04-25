"""fuctorial can never be negative"""
def fuctorial_recursive(n):
    if n<0:
        raise ValueError("no negative")
    if n<=1:
        return 1
    else: 
        return n*fuctorial_recursive(n-1)
