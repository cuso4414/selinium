import urllib.request

response = urllib.request.urlopen('http://www.baidu.com')
print(response.status)
print(response.read())
print(response.headers)


# import math
#
# print(math.ceil(5.5))
# print(math.floor(5.1))
# print(math.sqrt(36))