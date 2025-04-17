import requests
url = 'https://irs.thsrc.com.tw/IMINT/'
# 自訂表頭
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36'
}
# 將自訂表頭加入 GET 請求中
r = requests.get(url, headers=headers)
print(r)
