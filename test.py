import requests

BASE = 'http://127.0.0.1:5000/'

# data = [{"likes": 10, "name": "yerrrr", "views": 10030},
#         {"likes": 1054, "name": "video 2", "views": 340}, 
#         {"likes": 1032342, "name": "namgddd", "views": 1}]

# for i in range(len(data)):
#     response = requests.put(BASE + "video/" + str(i), data[i])
#     print(response.json())

response = requests.patch(BASE + "video/2", {"views": 99})
print(response.json())