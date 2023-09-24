import pandas as pd
df= pd.read_csv('C:/Users/54387/Downloads/hoteles.csv')

print(df['price_per_room'].max())
reservas_2017 = df[df['arrival_year'] == 2017]
reservas_2018 = df[df['arrival_year'] == 2018]

# Calcula el número total de reservas en cada año
total_reservas_2017 = len(reservas_2017)
total_reservas_2018 = len(reservas_2018)

# Calcula el incremento porcentual
incremento_porcentual = ((total_reservas_2018 - total_reservas_2017) / total_reservas_2017) * 100

# Imprime el incremento porcentual
print("El incremento porcentual en la cantidad de reservas entre 2017 y 2018 es:", incremento_porcentual, "%")

precio_promedio_por_mes = df.groupby('arrival_month')['price_per_room'].mean()

# Encuentra el mes con el precio promedio más alto
mes_max_precio_promedio = precio_promedio_por_mes.idxmax()

# Imprime el mes con el precio promedio más alto
print("El mes con el precio promedio por reserva más alto es:", mes_max_precio_promedio)

total_reservas = len(df)

# Filtra las reservas que se repiten (repeated_guest == 1)
reservas_repetidas = df[df['repeated_guest'] == 1]

# Calcula el total de reservas repetidas
total_reservas_repetidas = len(reservas_repetidas)

# Calcula el porcentaje de reservas que se repiten
porcentaje_reservas_repetidas = (total_reservas_repetidas / total_reservas) * 100

# Imprime el porcentaje
print("El porcentaje de reservas que se repiten sobre el total de reservas es:", porcentaje_reservas_repetidas, "%")

import pandas as pd

# Supongamos que tienes un DataFrame llamado 'df' con tus datos

# Filtra las filas para obtener solo los clientes que tienen hijos
clientes_con_hijos = df[df['no_of_children'] > 0]

# Agrupa los datos por mes y cuenta el número de reservas para cada mes
reservas_por_mes = clientes_con_hijos.groupby('arrival_month')['Booking_ID'].count()

# Encuentra el mes con el mayor número de reservas
mes_preferido_clientes_con_hijos = reservas_por_mes.idxmax()

# Imprime el mes preferido
print("El mes preferido por los clientes que tienen hijos es:", mes_preferido_clientes_con_hijos)
reservas_meal_plan_1 = df[df['type_of_meal_plan'] == 'Meal Plan 1']

# Agrupa los datos por tipo de cliente y cuenta el número de reservas para cada tipo
reservas_por_tipo_cliente = reservas_meal_plan_1.groupby('market_segment_type')['Booking_ID'].count()

# Encuentra el tipo de cliente con el mayor número de reservas
tipo_cliente_mas_reservas = reservas_por_tipo_cliente.idxmax()

# Imprime el tipo de cliente con más reservas con 'Meal Plan 1'
print("El tipo de cliente que utiliza 'Meal Plan 1' en el total de sus reservas es:", tipo_cliente_mas_reservas)

reservas_meal_plan_1 = df[df['type_of_meal_plan'] == 'Meal Plan 1']

# Contar la cantidad de reservas para cada plan de comidas
cantidad_por_plan_comidas = reservas_meal_plan_1['type_of_meal_plan'].value_counts()

# Imprimir la cantidad de cada plan de comidas
print(cantidad_por_plan_comidas)
