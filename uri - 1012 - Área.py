a,b,c = input().split()
a = float(a)
b = float(b)
c = float(c)

triangulo = (a*c)/2
circulo = 3.14159*(c**2)
trapezio = ((a + b)*c)/2
quadrado = b*b
retangulo = a * b

print('TRIANGULO: {:.3f}\nCIRCULO: {:.3F}\nTRAPEZIO: {:.3f}\nQUADRADO: {:.3f}\nRETANGULO: {:.3f}'.format(triangulo,circulo,trapezio,quadrado,retangulo))
