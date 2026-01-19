'''
 - - - 1
 - - 2 3 
 - 4 5 6
 7 8 9 10
 '''
row =int(input("Enter no of rows:"))

num=1
for i in range(row):
    
    for sp in range(row-i-1):
         print(end="\t")

    for j in range(i+1):
        print(num,end="\t")
        num+=1

    print()


