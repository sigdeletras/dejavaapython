"""
Tipos JAVA
int i = 10;
double d = 3.14;
char c1 = 'a';
char c2 = 65;
boolean encontrado = true;
String mensaje = "Bienvenido a Java";
final double PI =3.1415926536;
"""

i = 10
d = 3.14
c1 = 'a'  # En Python no existe el tipo char.
encontrado = True  # En Java true o false (minúscula)
mensaje = 'Bienvenido a Python'
PI = 3.1415926536 # Constante

# Con la función type() obtenemos el tipo de la variable.

print(type(i))
print('La variable i es de tipo entero (int) y su valor es: ', i)

print(type(d))
print('La variable d es de tipo coma flotante (float) y su valor es: ', d)

print(type(c1))
print('La variable c1 es de tipo cadena (str) su valor es: ', c1)

print(type(encontrado))
print('La variable encontrado es de tipo booleano (bool) y su valor es: ', encontrado)

print(type(mensaje))
print('La variable mensaje es de tipo cadena (str) y su valor es: ',  mensaje)

print(type(PI))
print('La variable PI es una constante de tipo coma flotante (float) y su valor es: ', PI)
