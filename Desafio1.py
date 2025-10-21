import numpy as np



lineas = ['Línea A', 'Línea B', 'Línea C', 'Línea D', 'Línea E']
turnos = ['D1-Mañana', 'D1-Tarde', 'D2-Mañana', 'D2-Tarde', 'D3-Mañana', 'D3-Tarde']

produccion = np.array([
    [145, 152, 138, 148, 155],
    [148, 149, 142, 151, 153],
    [142, 155, 135, 149, 158],
    [151, 148, 140, 152, 156],
    [147, 153, 137, 150, 157],
    [149, 151, 139, 153, 154]
])


# Nivel 1
promedios = produccion.mean(axis=0)
print("1) Promedios por línea:")
for i in range(len(lineas)):
    print(f"{lineas[i]}: {promedios[i]:.2f}")

totales_turno = produccion.sum(axis=1)
print("\n2) Producción total por turno:")
for i in range(len(turnos)):
    print(f"{turnos[i]}: {totales_turno[i]}")

indice_max = promedios.argmax()
print("\n3) línea con mejor desempeño:", lineas[indice_max])

indice_min = promedios.argmin()
print("\n4) línea con peor desempeño:", lineas[indice_min])

#Nivel 2
desviacion_estandar = produccion.std(axis=0)
print("\n5) Desviación estándar por línea:")
for i in range(len(lineas)):
    print(f"{lineas[i]}: {desviacion_estandar[i]:.2f}")

indice_consistente = desviacion_estandar.argmin()
print("\n6) Línea más consistente:", lineas[indice_consistente])

cumplen_meta = produccion >= 150
cumplimientos_por_linea = cumplen_meta.sum(axis=0)
print("\n7) Turnos que cumplieron la meta por línea:")
for i in range(len(lineas)):
    print(f"La {lineas[i]} cumplió la meta en {cumplimientos_por_linea[i]} turnos.")

porcentaje_cumplimiento = (cumplimientos_por_linea / 6) * 100
print("\n8) Porcentaje de cumplimiento de la meta por línea:")
for i in range(len(lineas)):
    print(f"{lineas[i]}: {porcentaje_cumplimiento[i]:.2f}%")

#Nivel 3
ranking = np.argsort(promedios)[::-1]
print("\n9) Ranking de líneas por producción promedio (de mayor a menor):")
for i in ranking:
    print(f"{lineas[i]}")

turno_max = totales_turno.argmax()
print("\n10) Turno con mayor producción total:", turnos[turno_max])

brecha = promedios.max() - promedios.min()
print(f"\n11) Brecha entre línea más prodcutiva ({lineas[indice_max]}) y línea menos productiva ({lineas[indice_min]}):", brecha, "unidades.")

#Nivel 4
#pendiente para semana que viene porque aún no lo vimos

#Nivel 5
#1. ¿Qué línea recomendarían auditar primero y por qué?
# Recomendaríamos auditar primero la línea C, ya que presentó un promedio de producción más bajo, 
# y no logró cumplir la meta de producción en ningún turno. Además, presentó una de las 
# mayores desviaciones estándar, por lo que su producción es menos consistente que la de otras líneas.
#2. ¿La variabilidad alta es siempre mala? ¿En qué casos podría ser aceptable?
# La variabilidad no es necesariamente negativa, podría ser aceptable en el caso de que 
# hubiese producción de productos distintos, cambios en la demanda o si se tratara de una etapa de prueba.
# 3. ¿Qué métodos de NumPy fueron más útiles para este análisis?
# Los métodos más útiles fueron los de arr.mean(axis=0) para calcular en promedio por 
# columnas y arr.argmax()/.argmin()