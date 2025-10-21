import numpy as np

# Matrices separadas: unidades vendidas
unidades = np.array([
[1250, 1380, 1420, 1650], # Alpha
[980, 1050, 1020, 1150], # Beta
[1560, 1680, 1590, 1820], # Gamma
[870, 920, 890, 1010], # Delta
[1340, 1450, 1480, 1620], # Epsilon
[760, 810, 780, 890] # Zeta
])
# Ingresos ($)
ingresos = np.array([
[56250, 62100, 63900, 74250],
[58800, 63000, 61200, 69000],
[54600, 58800, 55650, 63700],
[60900, 64400, 62300, 70700],
[60300, 65250, 66600, 72900],
[49400, 52650, 50700, 57850]
])
productos = ['Alpha', 'Beta', 'Gamma', 'Delta', 'Epsilon', 'Zeta']
trimestres = ['Q1', 'Q2', 'Q3', 'Q4']

#Nivel 1
totales_por_productos_unidades = unidades.sum(axis=1)
totales_por_productos_ingresos = ingresos.sum(axis=1)
print("\n1) Ventas totales anuales (en unidades e ingresos):")
for i in range(len(productos)):
    print(f"Ventas totales del producto {productos[i]}: {totales_por_productos_unidades[i]} unidades por ${totales_por_productos_ingresos[i]}.")

print("\n2) Precio promedio de cada producto por trimestre:")
for i in range(len(productos)):
    print(f"Producto {productos[i]}: {ingresos[i]/unidades[i]}.")

indice_max = totales_por_productos_ingresos.argmax()
print(f"\n3) El productos que más ingresos generó en el año fue {productos[indice_max]} con ${totales_por_productos_ingresos[indice_max]}.")

print("\n4) Ingresos totales por trimestre:")
ingresos_total_trimestre = ingresos.sum(axis=0)
for i in range(len(trimestres)):
    print(f"{trimestres[i]}: {ingresos_total_trimestre[i]}.")

#Nivel 2


