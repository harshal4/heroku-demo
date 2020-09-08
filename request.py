import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'pclass':1, 'age':35, 'sibsp':0,'parch':2,'fare':100,'sex_male':1,'embarked_Q':0,'embarked_S':1})


print(r.json())