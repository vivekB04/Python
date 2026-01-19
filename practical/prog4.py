'''
1  4  7
10 13 16
19 21 24
'''
row=int(input("Enter Rows="))
num=1
for i in range(row):

    for j in range(row):
        print(num,end="\t")
        num+=row
    print()



