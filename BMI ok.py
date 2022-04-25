a=float(input("vazn khod ra be Kg vared namaeid :"))
b=float(input("ghad khod ra be metr vared namaeid :"))

c=a/(b**2)

if c<18.5:
    Result="underweight"

if c>=18.5 and c<=24.9:
    Result="normal"

if c>=25 and c<=29.9:
    Result="overweight"

if c>=30 and c<=34.9:
    Result="obese"

if c>=35 :
    Result="xtremely obese"

print(Result)