"""
Question1
    Use python lists and make an list of numbers.
   Write a function which returns sum of the list of numbers

"""
lst = []
num = int(input('How many numbers: '))
def sum_list(num):
    for n in range(num):
        numbers = int(input('Enter number '))
        lst.append(numbers)
    return lst
res = sum_list(num)    
print("Sum of numbers in given list is :", sum(res))
