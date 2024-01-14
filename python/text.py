import requests

print("——AI智能写作——")
t = input("请输入主题:")
n = int(input("请输入段数:"))
url = "https://api.pearktrue.cn/api/ai/write/"
params = {
    "text": t,
    "page": n
}
print("请稍等")
response = requests.get(url, params=params)
data = response.json()

print(data['data'])