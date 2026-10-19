x, y = map(int,input().split())
for i in range(1,x+1):
    if(i % 4 == 0):
        print("#" + (y-1)*("."))
    elif (i % 2 ==0):
        print((y-1)*(".") + "#")
    else:
        print("#" * y)