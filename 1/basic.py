'''

给你一个整数数组 nums，请你返回其中位数为 偶数 的数字的个数。
https://home.testing-stdio.com/t/topic/1679
列表推导式:1. 要有for循环  2. 要有append
'''





def sort(nums):
    numssort = []
    for i in nums:
        if len(str(i)) % 2 == 0:
            numssort.append(i)
    return len(numssort)


num = [12, 345, 2, 6, 7896]
print(sort(num))
