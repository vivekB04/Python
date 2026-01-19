a,b,c=10,5,3

print("a =",a,"b =",b,"c =",c)

result1=a+b*c
print("a + b * c =",a,'+',b,'*',c,'=',result1,"\n")

result2=(a+b)*c
print("(a + b) * c = (",a,'+',b,') *',c,'=',result2,"\n")

result3=a**b//c
print("a ** b // c =",a,'**',b,'//',c,'=',result3,"\n")

result4=a < b and b > c or a == 10
print("= a < b and b > c or a == 10")
print("= 10<5 and 5>3 or 10==10")
print("= false and true or true")
print("= false or true")
print("= ",result4)

