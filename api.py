import requests

inp=input("Enter").split()

years_exp = {"Age": inp[0],"Gender_Female":inp[1],"Gender_Male":inp[2]}

response = requests.post("http://127.0.0.1:12345/predict", json = years_exp)

print(response.json()[0])