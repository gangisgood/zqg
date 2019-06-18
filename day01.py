print('Hello world')

def zqg(num):
    return num * 10



if __name__=="__main__":
    print(zqg(10))

pip install requests selenium beautifulsoup4 pyquery pymysql pymongo redis flask django==1.11 jupyter
import requests
response = requests.get('http://www.baidu.com')
print(response)