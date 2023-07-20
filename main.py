entero = 3
cadena = "Hola"
flotante = 5.1
booleano = True
concatenacion = cadena + " " + str(entero) + " " + str(flotante) + " " + str(booleano)
print(concatenacion)
"""
Enteros
Una gran ventaja de Python es que ya no nos tenemos que preocupar de esto, 
ya que por debajo se encarga de asignar más o menos memoria al número, 
y podemos representar prácticamente cualquier número.

Flotantes
Los float a diferencia de los int tienen unos valores mínimo y máximos que pueden representar. 
La mínima precisión es 2.2250738585072014e-308 y la máxima 1.7976931348623157e+308.
"""
n = 20
resultado = 0
for i in range(0,n,2):
  resultado+=i
print(resultado)
