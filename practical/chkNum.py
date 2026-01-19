def digitCount(x):
    count=0
    while x>0:
        x//=10
        count+=1
    return count
#-----------------------------
def sepNum(x):
    
    while x>0:
        rem=x%10
        print(rem)
        x//=10
#-----------------------------
def reve(x):
    rev=0
    while x>0:
        rem=x%10
        rev=rev*10+rem
        x//=10
    print(rev)
#-----------------------------
def isPalindrome(x):
    if x == reve(x):
        return "is a Palindrome "
    else:
        return "Not a Palindrome"
#-----------------------------
def isPrime(x):
    i=2
    while i < num and num % i != 0:
        i += 1

    if num >1 and num!=0:
        print("is prime number")
    else:
        print("is not a prime num")
#-----------------------------

choice=int(input('''****************************************************************
ENTER YOUR CHOICE:
        1.DIGITCOUNT
        2.SEPERATE DIGIT
        3.REVERSE NUMBER
        4.Palindrome
        5.Prime Number
****************************************************************
YOUR CHOICE IS: '''))

num=int(input("Enter The Number: "))

match choice:
    case 1:
        print(digitCount(num))
    case 2:
        sepNum(num)
    case 3:
        reve(num)
    case 4:
        print(isPalindrome(num))
    case 5:
        isPrime(num)
