'''
1 3 5
4 6 8
7 9 11
'''

row =int(input("Enter No. of Rows= "))
num=1
for i in range(row):
    num=i*row+1

    for j in range(row):
        print(num,end="\t")
        num+=2

    print()
   # num=num-row
