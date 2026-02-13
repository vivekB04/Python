ch1=input("enter char1 = ")
ch2= input("enter char2 = ")


if ord(ch1)%2==1 and ord(ch2)%2==1:
    sum=ord(ch1)+ord(ch2)
    print(sum)
else:
    print("sum is even")


#       OR
'''
a=ord(ch1)
b=ord(ch2)

if a%2==1 and b%2==1:
    sum=a+b
    print(sum)
else:
    print("sum is even")
'''
