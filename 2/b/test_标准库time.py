import time
# print(time.asctime())
# print(time.time())
# # 1590896826.122824
# # 1590896902.924452
# # 时间戳 从纪元开始到现在的秒数
# print(time.localtime())
# print(time.strftime("%Y-%m-%d  %H:%M:%S", time.localtime()))


# 获取两天前的时间
now_timestamp = time.time()
two_day_before = now_timestamp - 60*60*24*2
time_tuple = time.localtime(two_day_before)
print(time.strftime("%Y-%m-%d  %H:%M:%S", time_tuple))