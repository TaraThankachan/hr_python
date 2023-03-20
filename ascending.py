a=int(input('Enter First number:'))
b=int(input('Enter Second number:'))
c=int(input('Enter Third number:'))
a1=min(a,b,c)
a3 = max(a, b, c)
a2 = (a + b + c) - a1 - a3
print("Numbers in Ascending order:", a1, a2, a3)
