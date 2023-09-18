def funcao(x):
   y = (-x**2) + (25*x)
   return y
x = 0
delta = 0.001
Area = 0
while x<25:
    f = funcao(x)
    area = f * delta
    Area += area
    x+=delta
print(Area)