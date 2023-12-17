
a = int(input("a: "))
b = int(input("b:"))
c = int(input("c: "))
print (f"{a}x^2 + {b}x + {c}")

delta = b**2 - 4*a*c

if delta < 0:
    print("reel kök yok")
if delta == 0:
    x = -b / (2*a)
    print("denklemin tek kökü var x=", x)
    
else: 
  x1 = (-b - delta**0.5) / (2*a)
  x2 = (-b + delta**0.5) / (2*a)
print("Birinci Kök: {}".format(x1))
print ("İkinci Kök: {}".format(x2)) 