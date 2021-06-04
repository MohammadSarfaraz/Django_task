import requests
import json

URL ="http://127.0.0.1:8000/candidateapi/"
def get_data(id=None):
    data = {}
    if id is not None:
        data = {'id':id}
    json_data = json.dumps(data)
    r = requests.get(url=URL,data=json_data)
    print()
    data = r.json()
    avg_cand={}
    res_cand = []
    total_score = []

    for i in range(len(data)):
        if(data[i]['test_score1']<=10 and data[i]['test_score2']<=10 and data[i]['test_score3']<=10):
            avg_score = (data[i]['test_score1'] + data[i]['test_score2'] + data[i]['test_score3'])/3
            avg_cand=dict(data[i])
            avg_cand['avg_score']=round(avg_score,2)
            total_score.append(avg_score)
        else:
            print("Marks should not more than 10 for each test_score")
            break

        res_cand.append(avg_cand)
    print(res_cand)
    print("***************")

    for j in range(len(total_score)):
        if total_score[j] == max(total_score):
            print("Highest Marks Score Candidate ",data[j],"with avg",max(total_score))



def post_data():
    data = {
    'name':'Ajay',
    'email':'ajay@gmail.com',
    'test_score1' : 8,
    'test_score2': 9,
    'test_score3': 100,
    }

    json_data = json.dumps(data)

    r = requests.post(url = URL,data= json_data)
    data = r.json()
    print(data)


def update_data():
    data = {
        'id':3,
    'name':'Suresh',
    'email':'Suresh@gmail.com',
    'test_score1' : 10,
    'test_score2': 10,
    'test_score3': 10,
    }

    json_data = json.dumps(data)

    r = requests.put(url = URL,data= json_data)
    data = r.json()
    print(data)



def delete_data():
    data = { 'id': 2 }

    json_data = json.dumps(data)

    r = requests.delete(url = URL,data= json_data)
    data = r.json()
    print(data)

while (True):
    num = int(input("Enter Choice \n 1.Insert data in RestAPI \n 2.View Data of RestAPI \n 3.Update Data \n 4.Delete Data \n"))
    if num == 1:
        post_data()
    elif num == 2:
            get_data()
    elif(num == 3):
        update_data()
    elif (num == 4):
        delete_data()
    else:
        break
        
    





