import matplotlib.pyplot as plt
import numpy as np

def vcuota(prestamo,i,n):
    return prestamo*(i * (1 + i)**n)/((1 + i)**n - 1)

prestamo = 4000000 #float(input("Ingrese el valor del prestamo ($): "))

i = 2 #float(input("Ingrese el valor de la tasa de interes (%): "))
i = i/100

n = 9 #int(input("Ingrese el numero de peridos (meses): "))

# Para construir una tabla primero realizo el encabezado
# \t\t es la tabulacion
print("#Cuota\t\tV. Cuota\t\tPago Int.\t\tAmortizacion\tSaldo")

# Necesito almancear una lista para no perder los datos
cuota = np.zeros(n + 1)
pagoint = np.zeros(n + 1)
amort = np.zeros(n + 1)
saldo = np.zeros(n + 1)

cuota0 = vcuota(prestamo,i,n)
cuota[:] = cuota0
saldo[0] = prestamo
# Como es un arreglo necesito moverme en toda la matriz
for j in range(1,n+1):
    pagoint[j] = saldo[j-1] * i
    amort[j] = cuota0 - pagoint[j]
    saldo[j] = saldo[j-1] - amort[j]

    print("{0}\t\t\t{1:.2f}\t\t{2:.2f}\t\t{3:.2f}\t\t{4:.2f}".format(j,cuota0,pagoint[j],amort[j],saldo[j]))

# Para Graficar
x = np.linspace(0,n,n+1)
plt.plot(x[1:n+1],amort[1:n+1],label="Amortizacion")
plt.plot(x[1:n+1],pagoint[1:n+1],label="Pago Intereses")
plt.plot(x[1:n+1],cuota[1:n+1],label="Valor Cuota")
plt.xlabel("Perido ($n$)")
plt.ylabel("Money")
plt.legend()
plt.title("Grafica")
plt.show()