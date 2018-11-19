def fun_1():
    global result
    print(result)


def fun_2():
    result = 20
    print(result)


result = 30
print(result)
fun_1()
fun_2()
print(result)
