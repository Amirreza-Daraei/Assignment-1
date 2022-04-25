import math


a = int(input("add aval ra vared konid"))
b = int(input("add dovom ra vared koinid"))

op = input("amalgar mashin hesab ro type konid")

if op == "+" :
    result = a + b

if op == "-":
    result = a- b

if op == "*":
    result = a * b

if op == "/":
    result = a/ b

if op == "radical":
    r = input ("add aval ra entekhab konam ya dovom?")

    if r == "1":
         result = math.sqrt(a)

    if r == "2":
        result = math.sqrt(b)

if op =="sin":
    s = input ("add aval ra entekhab konam ya dovom?")

    if s == "1":
        result = math.sin(math.radians(a))
    if s == "2":
        result = math.sin(math.radians(b))

if op =="cos":
    c = input ("add aval ra entekhab konam ya dovom?")

    if c == "1":
        result = math.cos(math.radians(a))
    if c == "2":
        result = math.cos(math.radians(b))

if op =="tan":
    t = input ("add aval ra entekhab konam ya dovom?")

    if t == "1":
        result = math.tan(math.radians(a))
    if t == "2":
        result = math.tan(math.radians(b))

if op =="cot":
    co = input ("add aval ra entekhab konam ya dovom?")

    if co == "1":
        result = math.sin(math.radians(a))/math.cos(math.radians(a))
    if co == "2":
        result = math.sin(math.radians(b))/math.cos(math.radians(b))

if op == "!":
    f = input ("add aval ra entekhab konam ya dovom?")    

    if f == "1":
        result = math.factorial(a)

    if f == "2":
        result = math.factorial(b)

print(result)