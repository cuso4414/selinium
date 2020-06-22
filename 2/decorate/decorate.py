def foo():
    print("ffffff")
    return "aaa"
#不带括号的函数。调用的结果是返回一个函数对象，不需要等待该函数执行完成
foo
#带括号的函数，调用的结果是返回一个值,返回return的值，如果没有return则返回一个None。必须要等待函数执行完成
foo()