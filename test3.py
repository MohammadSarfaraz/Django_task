"""
Question 3
Assume we have list like this
[0,0,0,1,1,1,0,0,0,1,1,0,1,1,1,1,0,0,1,1]
Basically a list of zero’s and one’s.
Write a python function to the number of maximum consecutive  one’s present in the array. 
E.g output for the above array would be 4

"""

def Max_Num(mylist,n):
    count = 0
    res = 0
    for i in range(n):
        if mylist[i] == 0:
            count = 0
        else:
            count +=1
            res = max(res,count)
    return res


lst = [0,0,0,1,1,1,0,0,0,1,1,0,1,1,1,1,0,0,1,1]
length = len(lst)
print(Max_Num(lst,length))