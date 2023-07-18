import requests

url = "http://www.cmd5.com/api.ashx"
email = "xxxx"
key = "xxxx"
hash_value = input("请输入md5: ")

params = {
    "email": email,
    "key": key,
    "hash": hash_value
}

response = requests.get(url, params=params)
content = response.text

print("解密结果:", content)
