import json

# 读取 JSON 文件
with open('D:/pythonProject/python_job/长春大学.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# 提取所有的 name
names = [person['name'] for person in data]

# 显示结果
for name in names:
    print(name)
print(names)