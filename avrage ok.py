a=input("name : ")
b=input("Family : ")
C=float(input("nomre dars zaban : "))
d=float(input("nomre dars Riazi : "))
e=float(input("nomre dars Fizik : "))

avrage=(C+d+e)/3

if avrage>=17:
    result="khob"

if avrage<17 and avrage>=12 :
    result="Motevaset"

if avrage<12 :
    result="zaeif"

print(result)
