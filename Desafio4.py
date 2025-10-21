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
print("\n5) Crecimiento porcentual de unidades entre Q1 y Q4 para cada producto:")
crecimientos_u = []
for i in range(len(productos)):
    q1 = unidades[i][0]
    q4 = unidades[i][3]
    crecimiento_u = ((q4 - q1) / q1) * 100
    crecimientos_u.append(crecimiento_u)
    print(f"{productos[i]}: {crecimiento_u:.2f}%")

print("\n6) Crecimiento porcentual de ingreso entre Q1 y Q4 para cada producto:")
crecimientos_i = []
for i in range(len(productos)):
    q1 = ingresos[i][0]
    q4 = ingresos[i][3]
    crecimiento_i = ((q4 - q1) / q1) * 100
    crecimientos_i.append(crecimiento_i)
    print(f"{productos[i]}: {crecimiento_i:.2f}%")

crecimiento_i_array = np.array(crecimientos_i)
indice_max_i = crecimiento_i_array.argmax()

print(f"\n7) El producto que más crecimiento tuvo en el año fue {productos[indice_max_i]} con {crecimiento_i_array[indice_max_i]:.2f}% en ingresos y unidades.")

print("\n8) Ningún producto tuvo crecimiento negativo.")

tasa_crecimiento_trimestral = []
for i in range(len(productos)):
    tasas = []
    for t in range(1, 4):
        tasa = (unidades[i][t] - unidades[i][t - 1]) / unidades[i][t - 1]
        tasas.append(tasa)
        
    tasa_crecimiento_trimestral.append(np.mean(tasas) * 100)

print("\n9) Tasa de crecimiento promedio trimestral por producto:")
for i in range(len(productos)):
    print(f"{productos[i]}: {tasa_crecimiento_trimestral[i]:.2f}%")

#Nivel 3
ingreso_total = ingresos.sum(axis=1)
unidades_total = unidades.sum(axis=1)
ingreso_promedio_por_unidad = ingreso_total / unidades_total
print("\n10) Ingreso promedio por unidad:")
for i in range(len(productos)):
    print(f"{productos[i]}: ${ingreso_promedio_por_unidad[i]:.2f}")

indice_premium = ingreso_promedio_por_unidad.argmax()
print(f"\n11) Producto más premium: {productos[indice_premium]} (${ingreso_promedio_por_unidad[indice_premium]:.2f} por unidad)")


total_ingresos = ingresos.sum()
porcentaje_ingresos = (ingreso_total / total_ingresos) * 100
print("\n12) Porcentaje del ingreso total por producto:")
for i in range(len(productos)):
    print(f"{productos[i]}: {porcentaje_ingresos[i]:.2f}%")

mejor_trimestre = ingresos.argmax(axis=1)
print("\n13) Mejor trimestre por producto:")
for i in range(len(productos)):
    print(f"{productos[i]}: {trimestres[mejor_trimestre[i]]}")


#Nivel 4
#pendiente para semana que viene porque aún no lo vimos





# ========= Nivel 5 ========
'''
¿En qué 2 productos invertirían el presupuesto de marketing 2024? ¿Por qué?

# Información escasa sobre los productos. Depende de la rentabilidad de cada uno (margen %), 
# objetivos de la empresa, canibalización entre productos, saturación de mercado y/o demanda, 
# capacidad actual de la empresa de vender sin publicidad, etc.


¿Algún producto debería discontinuarse o rediseñarse?

# Imposible de definir sin datos sobre rentabilidad y competencia.


¿Qué operaciones vectorizadas de NumPy les ahorraron tiempo?

# unidades.sum(axis=1) e ingresos.sum(axis=1) ## Total por producto
# ingresos.sum(axis=0)  ## Total por trimestre
# np.argmax()


¿Cómo explicarían la diferencia entre crecimiento en unidades vs ingresos?

# Proporcional, porque en este ejercicio el precio de los productos 
# es constante durante todos los trimestres. Ingreso = P x Q 
# ## P constante, I(f) / I(i) = Q(f) / Q(i) 

'''

