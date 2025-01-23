import requests 
url = 'http://127.0.0.1:5000/upload' 
file_path = r'D:\project\Manufacturing Defect Prediction API\manufacturing_defect_dataset.csv' 

with open(file_path, 'rb') as file: 
    response = requests.post(url, files={'file': file}) 
print(response.json()) 