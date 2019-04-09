from selenium import webdriver

driver = webdriver.Firefox()
data = driver.get('https://www.google.co.in')

'''
weburl = urllib.request.urlopen('http://172.16.73.12:8090/httpclient.html')

print("result code = " + str(weburl.getcode()))

data = weburl.read()
'''
print(data)