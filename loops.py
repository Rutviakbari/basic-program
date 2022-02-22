#if else

a=150
b=135
if b>a:
    print("b is greater than a")
elif a==b:
    print("a and b are equal")
else:
    print("a is greter than b")
print("a") if a>b else print("b")
c=180
if a>b and c>a:
    print("both conditions are true")
if a>b or a>c:
    print("at least one of the conditions is true")

#while loop
i=1
while i<8:
    print(i)
    i += 1