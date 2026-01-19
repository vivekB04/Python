def avge():

    count=0
    total=0
    while count<5:
        marks=float(input(f"Enter marks for Subject{count+1}:"))

        total+=marks

        count+=1

    avg=total/count
    return avg

ret=avge()
print(ret)
