import numpy as np


productos = ['Producto A', 'Producto B', 'Producto C', 'Producto D', 'Producto E']
almacenes = ['Norte', 'Sur', 'Este', 'Oeste', 'Centro', 'Costero']

inventario = np.array([
[450, 320, 580, 290, 410],
[380, 350, 520, 310, 390],
[420, 310, 550, 280, 420],
[390, 340, 510, 320, 380],
[460, 330, 590, 300, 430],
[410, 360, 540, 290, 400]
])

# Precios unitarios ($)
precios = np.array([45, 65, 38, 72, 55])

# Costos de almacenamiento mensual por unidad ($)
costos_almacenamiento = np.array([2.5, 3.8, 2.0, 4.2, 3.0])

# Demanda mensual estimada por producto (unidades)
demanda_mensual = np.array([2200, 1800, 3000, 1600, 2300])


# Tareas de análisis: Nivel 1 - Analisis de Stock

# 1) Stock total de cada producto
stock_total_por_producto = inventario.sum(axis=0)

# 2) Inventario total de cada almacén
stock_total_por_almacen = inventario.sum(axis=1)

# 3) Almacén con mayor volumen total
indice_max_almacen = inventario.sum(axis=1).argmax()
almacen_mayor_volumen = almacenes[indice_max_almacen]

# 4) Producto con menor stock total
indice_min_producto = inventario.sum(axis=0).argmin()
producto_menor_stock = productos[indice_min_producto]


print("1) Stock total por producto:")
for producto, stock in zip(productos, stock_total_por_producto):
    print(producto, ":", stock, "unidades")

print("\n2) Inventario total por almacén:")
for almacen, total in zip(almacenes, stock_total_por_almacen):
    print(almacen, ":", total, "unidades")

print("\n3) Almacén con mayor volumen total:", almacen_mayor_volumen, 
      "con", stock_total_por_almacen[indice_max_almacen], "unidades")

print("\n4) Producto con menor stock total:", producto_menor_stock, 
      "con", stock_total_por_producto[indice_min_producto], "unidades")


# Tareas de análisis: Nivel 2 - Analisis de Valor

# 5) Valor monetario total del inventario de cada almacén
valor_por_almacen = (inventario * precios).sum(axis=1)

# 6) Valor total por producto
valor_por_producto = stock_total_por_producto * precios

# 7) Almacén con mayor valor total
idx_max_valor = np.argmax(valor_por_almacen)
almacen_mayor_valor = almacenes[idx_max_valor]

# 8) Porcentaje del valor total por producto
valor_total = valor_por_producto.sum()
porcentaje_valor_producto = (valor_por_producto / valor_total) * 100.0

print("\n5) Valor total por almacén:")
for nombre, valor in zip(almacenes, valor_por_almacen):
    print(nombre, ":", valor)

print("\n6) Valor total por producto:")
for nombre, valor in zip(productos, valor_por_producto):
    print(nombre, ":", valor)

print("\n7) Almacén con mayor valor total:", almacen_mayor_valor)

print("\n8) Porcentaje del valor total por producto:")
for nombre, porcentaje in zip(productos, porcentaje_valor_producto):
    print(nombre, ":", f'{porcentaje:.2f} %')



# Tareas de análisis: Nivel 3 - Analisis de Suficiencia

# 9) Meses de cobertura por producto
meses_cobertura = stock_total_por_producto / demanda_mensual

# 10) Productos con riesgo de desabastecimiento (< 1 mes)
productos_riesgo = []
for i in range(len(productos)):
    if meses_cobertura[i] < 1:
        productos_riesgo.append(productos[i])

# 11) Productos con exceso de inventario (> 1.5 meses)
productos_exceso = []
for i in range(len(productos)):
    if meses_cobertura[i] > 1.5:
        productos_exceso.append(productos[i])

# 12) Costo mensual de almacenamiento
costo_mensual_por_producto = stock_total_por_producto * costos_almacenamiento
costo_mensual_por_almacen_y_producto = inventario * costos_almacenamiento

print("\n9) Meses de cobertura por producto (stock_total / demanda_mensual):")
for producto, meses in zip(productos, meses_cobertura):
    print(producto, ":", f'{meses:.2f}')

print("\n10) Productos en riesgo de desabastecimiento (< 1 mes):")
if productos_riesgo:
    for nombre in productos_riesgo:
        print(nombre)
else:
    print('-- No hay productos en riesgo de desabastecimiento')

print("\n11) Productos con exceso de inventario (> 1.5 meses):")
if productos_riesgo:
    for nombre in productos_exceso:
        print(nombre)
else:
    print('-- No hay productos con exceso de inventario')

print("\n12) Costo mensual de almacenamiento por producto:")
for producto, costo in zip(productos, costo_mensual_por_producto):
    print(producto, ":", costo)

print("\n12) Costo mensual de almacenamiento por almacén (detalle de cada producto):")
for i, almacen in enumerate(almacenes):
    print(almacen, ":", costo_mensual_por_almacen_y_producto[i])


# Tareas de análisis: Nivel 4 - Optimizacion y Visualizacion

# 13) Ranking de almacenes por valor de inventario
valor_por_almacen = (inventario * precios).sum(axis=1)
orden_desc = list(np.argsort(valor_por_almacen))
orden_desc.reverse()


# 14) Distribución óptima
porcentaje_optimo = np.ones(inventario.shape) * (1 / len(almacenes)) * 100

# 13) Ranking de almacenes por valor de inventario
print("\n13) Ranking de almacenes por valor de inventario:")
posicion = 1
for indice in orden_desc:
    print(posicion, "-", almacenes[indice], ":", valor_por_almacen[indice])
    posicion += 1

# 14) Distribución óptima del stock (porcentaje por almacén y producto)
print("\n14) Distribución óptima del stock (% por almacén y producto):")
for i, almacen in enumerate(almacenes):
    print(almacen, ':', porcentaje_optimo[i])



# ======= Nivel 5 ========

'''
¿Qué producto requiere reabastecimiento urgente? ¿Cuál puede reducirse?

# Ninguno, ninguno. Todos > 1 y < 1.5 meses


¿Qué almacén tiene el inventario más "eficiente" (balance valor/volumen)?

#  Almacen Oeste, con 1940 unidades, valor total $ 102.970, y valor/volumen de $ 53.08


¿Cómo usaron broadcasting de NumPy en sus cálculos?

# inventario * precios 
# inventario * costos_almacenamiento 
# stock_total_por_producto / demanda_mensual 


Si pudieran transferir stock entre almacenes, ¿qué movimientos harían?

# No hay datos que hagan referencia a costos especificos de cada almacen, capacidad total, 
# ni tampoco datos referentes a la utilidad geografica de cada almacen. 
# Por ende, responder esto no tendria sentido hasta tener estos datos relevantes.

'''

