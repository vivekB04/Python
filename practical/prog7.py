'''
0  3  6
6  10 14
12 17 22
'''
row =int(input("Enter Row:"))

num=0
for i in range(row):
    num=(row*i)
    for j in range(row):
        print(num,end="\t")
        num+=row+i

    print()
