# trabajo_estructuras_numpy_arrays

# DESAFÍO 1: Optimización de Líneas de Producción
Contexto Industrial
Eres analista de datos en una planta automotriz. La gerencia necesita identificar cuellos de
botella en 5 líneas de ensamblaje que operaron durante 6 turnos (3 días, 2 turnos/día).
Cada línea tiene una meta de 150 unidades por turno.
Datos Proporcionados
lineas=['Línea A', 'Línea B', 'Línea C', 'Línea D', 'Línea E']
turnos=['D1-Mañana', 'D1-Tarde', 'D2-Mañana', 'D2-Tarde', 'D3-Mañana', 'D3-Tarde']

### Opción 2: Si usan matriz directamente produccion = np.array([
[145, 152, 138, 148, 155],
[148, 149, 142, 151, 153],
[142, 155, 135, 149, 158],
[151, 148, 140, 152, 156],
[147, 153, 137, 150, 157],
[149, 151, 139, 153, 154] ])
Tareas de Análisis

### NIVEL 1: Análisis Básico (5 min)
1. Calcular la producción promedio de cada línea en los 6 turnos
2. Calcular la producción total de cada turno (suma de todas las líneas)
3. Identificar qué línea tiene el mejor desempeño promedio
4. Identificar qué línea tiene el peor desempeño promedio

### NIVEL 2: Análisis de Variabilidad (5 min)
5. Calcular la desviación estándar de cada línea (indica consistencia)
6. Identificar cuál línea es más consistente (menor desviación)
7. Calcular cuántos turnos cada línea cumplió la meta de 150 unidades
8. Calcular el porcentaje de cumplimiento de meta por línea

### NIVEL 3: Ranking y Ordenamiento (5 min)
9. Crear un ranking de líneas ordenadas por producción promedio (de mayor a
menor)
10. Identificar en qué turno se alcanzó la producción máxima total
11. Calcular la brecha entre la línea más productiva y la menos productiva

### NIVEL 4: Visualización (5 min)
12. Crear DOS gráficos: - Gráfico 1: Gráfico de barras comparando la producción
promedio de cada línea (incluir línea horizontal de la meta) -
Gráfico 2: Gráfico de líneas mostrando la evolución de producción de cada línea a
lo largo de los 6 turnos
Preguntas para la Presentación (5 min)
1. ¿Qué línea recomendarían auditar primero y por qué?
2. ¿La variabilidad alta es siempre mala? ¿En qué casos podría ser aceptable?
3. ¿Qué métodos de NumPy fueron más útiles para este análisis?



# DESAFÍO 2: Control de Calidad en Procesos
Térmicos
Contexto Industrial
Trabajas en una planta química donde 4 reactores deben mantener temperaturas
específicas. Se registraron temperaturas de cada hora durante un turno de 8 horas. Cada
reactor tiene un rango óptimo y las desviaciones causan defectos en el producto.
Datos Proporcionados

#### Rangos óptimos (min, max) por reactor
rangos_optimos = {
'Reactor 1': (218, 225),
'Reactor 2': (315, 320),
'Reactor 3': (185, 190),
'Reactor 4': (243, 250)
}
reactores = ['Reactor 1', 'Reactor 2', 'Reactor 3', 'Reactor 4']
horas = ['08:00', '09:00', '10:00', '11:00', '12:00', '13:00', '14:00', '15:00']
Datos adicionales
import numpy as np
import matplotlib.pyplot as plt
temperaturas = np.array([
[220, 315, 185, 245],
[222, 318, 188, 243],
[225, 320, 186, 248],
[219, 322, 190, 246],
[223, 317, 187, 250],
[221, 325, 189, 244],
[224, 319, 191, 247],
[218, 316, 184, 249]
])
Tareas de Análisis

### NIVEL 1: Estadísticas Básicas (5 min)
1. Calcular temperatura promedio, máxima y mínima de cada reactor
2. Calcular la desviación estándar de cada reactor
3. Identificar qué reactor tiene la mayor variabilidad térmica
4. Calcular el rango térmico (max - min) de cada reactor

### NIVEL 2: Análisis de Conformidad (5 min)
5. Para cada reactor, determinar cuántas horas estuvo dentro del rango óptimo
6. Calcular el porcentaje de conformidad de cada reactor
7. Identificar en qué hora específica cada reactor alcanzó su temperatura máxima
8 Crear una matriz booleana indicando si cada medición está dentro del rango óptimo

### NIVEL 3: Detección de Anomalías (5 min)
9. Identificar todas las mediciones fuera de especificación (reactor, hora, temperatura)
10. Calcular cuántos grados se desvió cada medición problemática del límite más
cercano
11. Ordenar los reactores por nivel de criticidad (mayor tiempo fuera de especificación)
12. Calcular la temperatura promedio por hora (todas los reactores) para detectar
patrones temporales

### NIVEL 4: Visualización (5 min)
13. Crear DOS gráficos:
- Gráfico 1: Gráfico de líneas mostrando la evolución de temperatura de los 4
reactores + bandas de rangos óptimos
- Gráfico 2: Gráfico de barras mostrando el porcentaje de conformidad de cada
reactor
Preguntas para la Presentación (5 min)
¿Qué reactor necesita intervención inmediata y por qué?
¿La desviación estándar baja siempre indica un buen proceso? Expliquen.
¿Observaron algún patrón temporal en las temperaturas?
¿Qué métodos de indexing/masking de NumPy utilizaron?


# DESAFÍO 3: Optimización de Inventario
Multi-Almacén
Contexto Industrial
Eres analista de logística de una cadena de distribución con 6 almacenes y 5 productos.
Necesitas optimizar el inventario considerando costos de almacenamiento, demanda y valor
del stock.
Datos Proporcionados
productos = ['Producto A', 'Producto B', 'Producto C', 'Producto D', 'Producto E']
almacenes = ['Norte', 'Sur', 'Este', 'Oeste', 'Centro', 'Costero']
Datos adicionales:
import numpy as np
import matplotlib.pyplot as plt
inventario = np.array([
[450, 320, 580, 290, 410],
[380, 350, 520, 310, 390],
[420, 310, 550, 280, 420],
[390, 340, 510, 320, 380],
[460, 330, 590, 300, 430],
[410, 360, 540, 290, 400]
])
#### Precios unitarios ($)
precios = np.array([45, 65, 38, 72, 55])
#### Costos de almacenamiento mensual por unidad ($)
costos_almacenamiento = np.array([2.5, 3.8, 2.0, 4.2, 3.0])
#### Demanda mensual estimada por producto (unidades)
demanda_mensual = np.array([2200, 1800, 3000, 1600, 2300])
Tareas de Análisis

### NIVEL 1: Análisis de Stock (5 min)
1. Calcular el stock total de cada producto (suma por columna)
2. Calcular el inventario total de cada almacén (suma por fila)
3. Identificar qué almacén tiene el mayor volumen de productos
4. Identificar qué producto tiene el menor stock total

### NIVEL 2: Análisis de Valor (7 min)
5. Calcular el valor monetario total del inventario de cada almacén
6. Calcular el valor total por producto (stock_total × precio)
7. Identificar el almacén con el mayor valor de inventario
8. Calcular qué porcentaje del valor total representa cada producto

### NIVEL 3: Análisis de Suficiencia (6 min)
9. Calcular cuántos meses de demanda cubre el stock actual de cada producto
10. Identificar productos con riesgo de desabastecimiento (< 1 mes de cobertura)
11. Identificar productos con exceso de inventario (> 1.5 meses de cobertura)
12. Calcular el costo mensual de almacenamiento por producto y por almacén

### NIVEL 4: Optimización y Visualización (7 min)
13. Crear un ranking de almacenes ordenados por valor de inventario
14. Calcular la distribución óptima (¿qué % del stock de cada producto debería tener
cada almacén?)
15. Crear TRES gráficos:
- Gráfico 1: Barras apiladas mostrando la composición de inventario de cada almacén
- Gráfico 2: Gráfico de barras comparando stock actual vs demanda mensual por
producto
- Gráfico 3: Gráfico circular (pie chart) mostrando la distribución del valor total por
producto

### Preguntas para la Presentación (5 min)
¿Qué producto requiere reabastecimiento urgente? ¿Cuál puede reducirse?
¿Qué almacén tiene el inventario más "eficiente" (balance valor/volumen)?
¿Cómo usaron broadcasting de NumPy en sus cálculos?
Si pudieran transferir stock entre almacenes, ¿qué movimientos harían?

# DESAFÍO 4: Análisis de Ventas y Tendencias de
Mercado
Contexto Industrial
Eres analista comercial de una empresa tecnológica. Debes analizar el desempeño de
ventas trimestrales de 6 productos durante 2023 y proyectar estrategias para 2024.
Datos Proporcionados
import numpy as np
import matplotlib.pyplot as plt
#### Matrices separadas: unidades vendidas
unidades = np.array([
[1250, 1380, 1420, 1650], # Alpha
[980, 1050, 1020, 1150], # Beta
[1560, 1680, 1590, 1820], # Gamma
[870, 920, 890, 1010], # Delta
[1340, 1450, 1480, 1620], # Epsilon
[760, 810, 780, 890] # Zeta
])
#### Ingresos ($)
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
Tareas de Análisis

#### NIVEL 1: Métricas de Desempeño (5 min)
1. Calcular las ventas totales anuales (unidades e ingresos) por producto
2. Calcular el precio promedio de cada producto por trimestre (ingresos/unidades)
3. Identificar qué producto generó mayores ingresos en el año
4. Calcular los ingresos totales por trimestre (suma todos los productos)

#### NIVEL 2: Análisis de Crecimiento (6 min)
5. Calcular el crecimiento porcentual de unidades entre Q1 y Q4 para cada producto
6. Calcular el crecimiento porcentual de ingresos entre Q1 y Q4 para cada producto
7. Identificar qué producto tuvo el mayor crecimiento en el año
8. Identificar qué producto tuvo crecimiento negativo (si hay alguno)
9. Calcular la tasa de crecimiento promedio trimestral de cada producto

#### NIVEL 3: Análisis de Rentabilidad (5 min)
10. Calcular el ingreso promedio por unidad de cada producto (indicador de
premium/económico)
11. Identificar el producto más "premium" (mayor ingreso por unidad)
12. Calcular qué porcentaje de los ingresos totales representa cada producto
13. Analizar la estacionalidad: ¿qué trimestre fue mejor para cada producto?

#### NIVEL 4: Proyecciones y Visualización (9 min)
14. Calcular una proyección lineal simple para Q1-2024 basada en la tendencia 2023
15. Identificar productos "estrella" (alto crecimiento + altos ingresos) vs "problema" (bajo
crecimiento + bajos ingresos)
16. Crear TRES gráficos:
- Gráfico 1: Gráfico de líneas múltiples mostrando evolución de ingresos por
producto
- Gráfico 2: Gráfico de barras agrupadas comparando crecimiento Q1-Q4 de
cada producto

Preguntas para la Presentación (5 min)
¿En qué 2 productos invertirían el presupuesto de marketing 2024? ¿Por qué?
¿Algún producto debería discontinuarse o rediseñarse?
¿Qué operaciones vectorizadas de NumPy les ahorraron tiempo?
¿Cómo explicarían la diferencia entre crecimiento en unidades vs ingresos?