# x = 50
# def test():
#     global x
#     x = x+10
#     print(x)
# test()

# def test2(x,y):
#     print(x+y)
# test2(10,20)

# *args ot **kwargs
def test3(*args):
    sum = 0
    for ele in args:
        sum += ele
    print(sum)
test3(2,3,4,5,6)