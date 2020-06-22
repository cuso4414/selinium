import os
# os.mkdir("tesedir")
# print(os.listdir("./"))
# os.removedirs("tesedir")
# print(os.getcwd())

print(os.path.exists("b"))
if not os.path.exists("b"):
    os.mkdir("b")
if not os.path.exists("b/test.txt"):
    f = open("test.txt", "w")
    f.write("hello,os using")
    f.close()




