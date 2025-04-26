'''Q1. culculating the sum of all elements
it should return int/floats'''
def sum(numbers):
    total =0
    for num in numbers:
        total= total + num
    return total
if __name__ == "__main__":
    print(sum([1, 2, 3, 4, 5]))   #i think it should print 15