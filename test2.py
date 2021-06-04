"""
Question2 
Setup a dict structure like this in python
Dict1: (this is a key, value pair of user id and username)
{
   “1” : “name1”,
   “2” : “name2”,
   “3” : “name3”
} etc.. 
Dict2: (this is a key value pair of user id and exam score) 
{
   “1” : 50,
   “2” : 60
   “3” : 70
}
These are just sample data assume there are hundreds of users 

Write a function in python in python, which will return maximum i.e function should return dictionary like
{
  “3” : 70
}


"""
dict1 = { "1" : "name1","2" : "name2","3" : "name3"}
dict2 = {"1": 50,
   "2" : 60,
   "3" : 70}

resultant_dict = {}

num = int(input('How many numbers of users: '))

def max_dict(num):    
    for n in range(num):
        id = input('Enter user id: ')
        name = input("Enter user name: ")
        exam = int(input("Enter Exam Score: "))
        dict1 [id] = name
        dict2 [id] = exam

    
    Keymax = max(dict2, key= lambda x: dict2[x])
    return Keymax

maxscore = max_dict(num)
resultant_dict[maxscore] = dict2[maxscore]
print("Return dictionary with max score of user_id \n",resultant_dict)
