'''
1 3 5
2 4 6
3 5 7
'''

rows=int(input("Enter the rows"))

num=1
for i in range(rows):
    num=i+1
    for j in range(rows):
        print(num,end="\t")
        num+=2
    print()


