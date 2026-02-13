def avg(*num):
    total=0
    count=len(num)
    for data in num:
        total=total+data

    #print(total)

    average=total/count
    print(average)

avg(10,20,30,40)

