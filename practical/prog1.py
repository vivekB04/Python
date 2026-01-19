'''
1  2  3  4 
5  6  7  8
9  10 11 12                        User input
13 14 15 16
'''

row=int(input("Enter no. of rows="))
num=1
for i in range(row):
    for j in range(row):
        print(num,end="\t")
        num+=1
    print()
     
